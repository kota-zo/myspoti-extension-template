#!/usr/bin/env python3
"""Builds extension.zip: the package Myspoti installs, the same files, order and dates every time.

Same layout as `myspoti-ext pack`: manifest.json and the script named by "main" first, then
the icon, LICENSE and README.md when present, at the root of the zip, nothing else (Myspoti
refuses a package with other files). Fixed order and dates, so a rebuild gives the same bytes, to compare
the sha256.

    python3 scripts/pack.py [output.zip]
"""
import hashlib
import json
import os
import sys
import zipfile

KEPT = ["icon.png", "LICENSE", "LICENSE.txt", "README.md"]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "extension.zip")
    with open(os.path.join(ROOT, "manifest.json"), encoding="utf-8") as f:
        manifest = json.load(f)
    names = ["manifest.json", manifest.get("main", "main.js")]
    if manifest.get("icon"):
        names.append(manifest["icon"])
    names += [n for n in KEPT if os.path.isfile(os.path.join(ROOT, n))]
    names = list(dict.fromkeys(names))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name in names:
            path = os.path.join(ROOT, name)
            if not os.path.isfile(path):
                sys.exit(f"{name} is missing")
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(path, "rb") as f:
                z.writestr(info, f.read())
    with open(out, "rb") as f:
        print(f"{out}  {len(names)} files  sha256 {hashlib.sha256(f.read()).hexdigest()}")


if __name__ == "__main__":
    main()
