#!/usr/bin/env python3
"""Build the KiCad PCM archive for this plugin and refresh packages.json.

Usage:
    python3 tools/build_pcm.py            # build + update packages.json
    python3 tools/build_pcm.py --no-index # build only

The produced archive has this layout (required by KiCad PCM):

    metadata.json
    plugins/
        __init__.py
        ViaStitching/
            ...
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
EXCLUDE_DIRS = {"__pycache__", ".git", ".github", "dist", "tools", ".idea", ".vscode"}
EXCLUDE_SUFFIXES = (".pyc", ".pyo", ".zip")


def load_metadata() -> dict:
    with open(os.path.join(ROOT, "metadata.json"), encoding="utf-8") as fp:
        return json.load(fp)


def collect_files() -> list[tuple[str, str]]:
    """Return (absolute_path, archive_path) pairs for files that belong in the package."""
    files: list[tuple[str, str]] = []

    meta = os.path.join(ROOT, "metadata.json")
    files.append((meta, "metadata.json"))

    plugins = os.path.join(ROOT, "plugins")
    for dirpath, dirnames, filenames in os.walk(plugins):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIRS)
        for name in sorted(filenames):
            if name.endswith(EXCLUDE_SUFFIXES):
                continue
            abs_path = os.path.join(dirpath, name)
            rel_path = os.path.relpath(abs_path, ROOT).replace(os.sep, "/")
            files.append((abs_path, rel_path))
    return files


def build_zip(version: str) -> tuple[str, int, int, str]:
    os.makedirs(DIST, exist_ok=True)
    zip_name = f"kicad-via-stitching-{version}-pcm.zip"
    zip_path = os.path.join(DIST, zip_name)
    if os.path.exists(zip_path):
        os.remove(zip_path)

    files = collect_files()
    install_size = 0
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for abs_path, arc_path in files:
            zf.write(abs_path, arc_path)
            install_size += os.path.getsize(abs_path)

    download_size = os.path.getsize(zip_path)
    sha256 = hashlib.sha256()
    with open(zip_path, "rb") as fp:
        for chunk in iter(lambda: fp.read(1024 * 1024), b""):
            sha256.update(chunk)

    return zip_path, download_size, install_size, sha256.hexdigest()


def make_index_entry(metadata: dict, version: str, download_url: str,
                     download_size: int, install_size: int, sha256: str) -> dict:
    entry = {
        "$schema": "https://go.kicad.org/pcm/schemas/v1",
        "name": metadata["name"],
        "description": metadata["description"],
        "description_full": metadata["description_full"],
        "identifier": metadata["identifier"],
        "type": metadata["type"],
        "author": metadata["author"],
        "maintainer": metadata["maintainer"],
        "license": metadata["license"],
        "resources": metadata["resources"],
        "tags": metadata["tags"],
        "versions": [],
    }
    current = dict(metadata["versions"][0])
    current.update(
        {
            "version": version,
            "download_url": download_url,
            "download_size": download_size,
            "install_size": install_size,
            "download_sha256": sha256,
        }
    )
    entry["versions"].append(current)
    return entry


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-index", action="store_true",
                        help="only build the archive, do not touch packages.json")
    parser.add_argument("--download-url", default=None,
                        help="override download URL (default: GitHub release asset for the version)")
    args = parser.parse_args()

    metadata = load_metadata()
    version = metadata["versions"][0]["version"]
    repo = metadata["resources"]["Github"].rstrip("/")
    download_url = args.download_url or (
        f"{repo}/releases/download/v{version}/kicad-via-stitching-{version}-pcm.zip"
    )

    zip_path, download_size, install_size, sha256 = build_zip(version)
    print(f"archive      : {zip_path}")
    print(f"version      : {version}")
    print(f"download_size: {download_size}")
    print(f"install_size : {install_size}")
    print(f"sha256       : {sha256}")

    if args.no_index:
        return 0

    index_path = os.path.join(ROOT, "packages.json")
    entry = make_index_entry(metadata, version, download_url,
                             download_size, install_size, sha256)
    with open(index_path, "w", encoding="utf-8") as fp:
        json.dump({"packages": [entry]}, fp, indent=4, ensure_ascii=False)
        fp.write("\n")
    print(f"index        : {index_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
