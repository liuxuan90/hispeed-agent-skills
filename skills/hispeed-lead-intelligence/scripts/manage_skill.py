#!/usr/bin/env python3
"""Check or safely update the installed Hispeed Lead Intelligence Skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
import urllib.request
import zipfile


SKILL_NAME = "hispeed-lead-intelligence"
REPO = "liuxuan90/hispeed-agent-skills"
REF = "stable"
SOURCE_PATH = f"skills/{SKILL_NAME}"
MANIFEST_NAME = "release-manifest.json"
ROOT = Path(__file__).resolve().parents[1]
MAX_DOWNLOAD_BYTES = 25 * 1024 * 1024
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
IGNORED_LOCAL_PARTS = {"__pycache__", ".DS_Store", "Thumbs.db"}


def _version_tuple(value: str) -> tuple[int, int, int]:
    match = SEMVER.fullmatch(value)
    if not match:
        raise ValueError(f"invalid semantic version: {value!r}")
    return tuple(int(part) for part in match.groups())


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Hispeed-Skill-Updater/1.2", "Accept": "application/octet-stream"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        length = response.headers.get("Content-Length")
        if length and int(length) > MAX_DOWNLOAD_BYTES:
            raise ValueError("download is larger than the updater limit")
        data = response.read(MAX_DOWNLOAD_BYTES + 1)
    if len(data) > MAX_DOWNLOAD_BYTES:
        raise ValueError("download is larger than the updater limit")
    return data


def _remote_manifest() -> dict:
    url = f"https://raw.githubusercontent.com/{REPO}/{REF}/{SOURCE_PATH}/{MANIFEST_NAME}"
    return json.loads(_fetch_bytes(url).decode("utf-8"))


def _validate_manifest(manifest: dict) -> None:
    expected = {
        "skill": SKILL_NAME,
        "source_repo": REPO,
        "source_ref": REF,
        "source_path": SOURCE_PATH,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise ValueError(f"manifest {key} does not match the trusted source")
    _version_tuple(str(manifest.get("version", "")))
    if not isinstance(manifest.get("change_types", []), list):
        raise ValueError("manifest change_types must be a list")
    if not isinstance(manifest.get("review_before_update", False), bool):
        raise ValueError("manifest review_before_update must be true or false")
    files = manifest.get("files")
    if not isinstance(files, dict) or not files:
        raise ValueError("manifest has no file checksums")
    for name, digest in files.items():
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or name == MANIFEST_NAME:
            raise ValueError(f"unsafe manifest path: {name}")
        if not re.fullmatch(r"[0-9a-f]{64}", str(digest)):
            raise ValueError(f"invalid checksum for {name}")


def _package_files(root: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in IGNORED_LOCAL_PARTS for part in path.parts):
            continue
        relative = path.relative_to(root).as_posix()
        if relative == MANIFEST_NAME:
            continue
        result[relative] = path
    return result


def _verify_package(root: Path, manifest: dict) -> None:
    _validate_manifest(manifest)
    actual = _package_files(root)
    expected = manifest["files"]
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    if missing or extra:
        raise ValueError(f"package file mismatch; missing={missing}, extra={extra}")
    bad = [name for name, path in actual.items() if _sha256(path) != expected[name]]
    if bad:
        raise ValueError(f"checksum mismatch: {sorted(bad)}")


def _local_state(target: Path) -> tuple[str, list[str]]:
    manifest_path = target / MANIFEST_NAME
    if manifest_path.is_file():
        manifest = _read_json(manifest_path)
        version = str(manifest.get("version", "unknown"))
        try:
            _verify_package(target, manifest)
            return version, []
        except ValueError as exc:
            return version, [str(exc)]
    skill_file = target / "SKILL.md"
    if not skill_file.is_file():
        return "not-installed", []
    text = skill_file.read_text(encoding="utf-8")
    match = re.search(r"(?m)^\s*version:\s*[\"']?([^\s\"']+)", text)
    return (match.group(1) if match else "legacy-unknown"), ["legacy install has no release manifest"]


def _extract_remote_package(destination: Path) -> Path:
    archive = _fetch_bytes(f"https://codeload.github.com/{REPO}/zip/refs/heads/{REF}")
    archive_path = destination / "source.zip"
    archive_path.write_bytes(archive)
    output = destination / "extracted"
    output.mkdir()
    prefix_parts = PurePosixPath(SOURCE_PATH).parts
    with zipfile.ZipFile(archive_path) as bundle:
        for item in bundle.infolist():
            parts = PurePosixPath(item.filename).parts
            if len(parts) <= len(prefix_parts) + 1 or tuple(parts[1 : 1 + len(prefix_parts)]) != prefix_parts:
                continue
            relative = PurePosixPath(*parts[1 + len(prefix_parts) :])
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError("unsafe path in downloaded archive")
            mode = item.external_attr >> 16
            if mode & 0o170000 == 0o120000:
                raise ValueError("symbolic links are not allowed in the Skill package")
            target = output.joinpath(*relative.parts)
            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with bundle.open(item) as source, target.open("wb") as sink:
                shutil.copyfileobj(source, sink)
    return output


def _activate(staged: Path, target: Path, backup: Path, simulate_failure: bool = False) -> None:
    moved_old = False
    try:
        if target.exists():
            os.replace(target, backup)
            moved_old = True
        if simulate_failure:
            raise RuntimeError("simulated activation failure")
        os.replace(staged, target)
    except Exception:
        if target.exists():
            shutil.rmtree(target)
        if moved_old and backup.exists():
            os.replace(backup, target)
        raise


def _check(target: Path, remote: dict) -> int:
    local_version, warnings = _local_state(target)
    remote_version = str(remote["version"])
    print(f"INSTALLED_VERSION: {local_version}")
    print(f"STABLE_VERSION: {remote_version}")
    for warning in warnings:
        print(f"LOCAL_WARNING: {warning}")
    if local_version in {"not-installed", "legacy-unknown"}:
        print("UPDATE_AVAILABLE: YES")
    else:
        comparison = _version_tuple(remote_version) > _version_tuple(local_version)
        print(f"UPDATE_AVAILABLE: {'YES' if comparison else 'NO'}")
    notes = remote.get("release_notes", [])
    change_types = remote.get("change_types", [])
    if change_types:
        print(f"CHANGE_TYPES: {', '.join(change_types)}")
    print(f"REVIEW_BEFORE_UPDATE: {'YES' if remote.get('review_before_update') else 'NO'}")
    if notes:
        print("CHANGES:")
        for note in notes:
            print(f"- {note}")
    return 0


def _update(
    target: Path,
    remote: dict,
    force: bool,
    allow_downgrade: bool,
    accept_reviewed_changes: bool,
) -> int:
    if remote.get("review_before_update") and not accept_reviewed_changes:
        raise ValueError(
            "this release changes scripts, permissions, dependencies, or workflow; "
            "review the check output, then rerun with --accept-reviewed-changes"
        )
    local_version, warnings = _local_state(target)
    if warnings and local_version not in {"not-installed", "legacy-unknown"} and not force:
        raise ValueError("local Skill differs from its manifest; refusing to overwrite without --force")
    remote_version = str(remote["version"])
    if local_version not in {"not-installed", "legacy-unknown"}:
        local_tuple = _version_tuple(local_version)
        remote_tuple = _version_tuple(remote_version)
        if remote_tuple < local_tuple and not allow_downgrade:
            raise ValueError("stable version is older; use --allow-downgrade only for an intentional rollback")
        if remote_tuple == local_tuple and not force:
            print(f"ALREADY_CURRENT: {local_version}")
            return 0
    target = target.resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    os.chdir(target.parent)
    backup_root = target.parent / ".hispeed-skill-backups"
    backup_root.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="hispeed-skill-update-", dir=target.parent) as temporary:
        staged = _extract_remote_package(Path(temporary))
        downloaded_manifest = _read_json(staged / MANIFEST_NAME)
        if downloaded_manifest != remote:
            raise ValueError("stable manifest changed while downloading; run the update again")
        _verify_package(staged, downloaded_manifest)
        stamp = __import__("datetime").datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        backup = backup_root / f"{SKILL_NAME}-{local_version}-{stamp}"
        _activate(staged, target, backup)
    backups = sorted(backup_root.glob(f"{SKILL_NAME}-*"), key=lambda p: p.stat().st_mtime, reverse=True)
    for stale in backups[3:]:
        shutil.rmtree(stale)
    print(f"UPDATED_VERSION: {remote_version}")
    print(f"BACKUP_PATH: {backup if backup.exists() else 'none (fresh install)'}")
    print("RELOAD_REQUIRED: start a new Agent conversation or reload the Skill index")
    return 0


def _self_test() -> int:
    with tempfile.TemporaryDirectory(prefix="hispeed-updater-self-test-") as temporary:
        root = Path(temporary)
        target = root / SKILL_NAME
        staged = root / "staged"
        backup = root / "backup"
        target.mkdir()
        staged.mkdir()
        (target / "sentinel.txt").write_text("old", encoding="utf-8")
        (staged / "sentinel.txt").write_text("new", encoding="utf-8")
        try:
            _activate(staged, target, backup, simulate_failure=True)
        except RuntimeError:
            pass
        else:
            raise AssertionError("failure simulation did not fail")
        if (target / "sentinel.txt").read_text(encoding="utf-8") != "old":
            raise AssertionError("rollback did not restore the previous version")
    print("SELF_TEST_OK: activation failure restored the previous version")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("check", "update", "self-test"))
    parser.add_argument("--target", type=Path, default=ROOT, help=argparse.SUPPRESS)
    parser.add_argument("--force", action="store_true", help="replace a same-version or locally modified install")
    parser.add_argument("--allow-downgrade", action="store_true", help="allow intentional rollback to older stable")
    parser.add_argument(
        "--accept-reviewed-changes",
        action="store_true",
        help="confirm that flagged script, permission, dependency, or workflow changes were reviewed",
    )
    args = parser.parse_args()
    try:
        if args.action == "self-test":
            return _self_test()
        remote = _remote_manifest()
        _validate_manifest(remote)
        if args.action == "check":
            return _check(args.target, remote)
        return _update(
            args.target,
            remote,
            args.force,
            args.allow_downgrade,
            args.accept_reviewed_changes,
        )
    except Exception as exc:
        print(f"UPDATE_FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
