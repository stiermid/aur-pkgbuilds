#!/usr/bin/env python3
"""
Check for upstream version updates across all AUR packages in this repo.

Merges all per-package .nvchecker.toml files into a single combined config
and runs nvchecker once, minimising network requests.

For each package directory:
  - Skips -git packages (they always track HEAD)
  - Warns if .nvchecker.toml is missing
  - Compares the fetched latest version with pkgver from .SRCINFO
  - Prints packages that have a new version available
"""

import json
import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).parent.resolve()

# Colours for terminal output
GREEN  = "\033[32m"
YELLOW = "\033[33m"
RED    = "\033[31m"
BOLD   = "\033[1m"
RESET  = "\033[0m"


def get_current_version(srcinfo: Path) -> str | None:
    """Return pkgver from .SRCINFO, or None if not found."""
    for line in srcinfo.read_text().splitlines():
        m = re.match(r"^\s*pkgver\s*=\s*(.+)$", line)
        if m:
            return m.group(1).strip()
    return None


def run_nvchecker(combined_config: str) -> list[dict]:
    """Write combined config to a temp file, run nvchecker once, return JSON entries."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False) as f:
        f.write(combined_config)
        tmp_path = f.name

    result = subprocess.run(
        ["nvchecker", "--logger", "json", "-c", tmp_path],
        capture_output=True,
        text=True,
    )
    Path(tmp_path).unlink(missing_ok=True)

    entries = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            pass

    if result.returncode not in (0, 3):
        stderr = result.stderr.strip()
        if stderr:
            print(f"{RED}nvchecker stderr:{RESET} {stderr}", file=sys.stderr)

    return entries


def build_combined_toml(pkg_dirs: list[Path]) -> tuple[str, dict[str, Path], list[str]]:
    """
    Merge all per-package .nvchecker.toml files.

    Returns:
      - combined TOML string (no [__config__] so nvchecker won't touch ver files)
      - mapping of package name → pkg_dir for packages that were included
      - list of warning strings for packages that were skipped
    """
    sections: list[str] = []
    included: dict[str, Path] = {}
    warnings: list[str] = []

    for pkg_dir in pkg_dirs:
        name = pkg_dir.name
        config = pkg_dir / ".nvchecker.toml"
        srcinfo = pkg_dir / ".SRCINFO"

        if name.endswith("-git"):
            continue

        if not config.exists():
            warnings.append(f"{YELLOW}WARN{RESET}  {name}: .nvchecker.toml missing — skipping")
            continue
        if not srcinfo.exists():
            warnings.append(f"{YELLOW}WARN{RESET}  {name}: .SRCINFO missing — skipping")
            continue

        try:
            data = tomllib.loads(config.read_text())
        except tomllib.TOMLDecodeError as e:
            warnings.append(f"{RED}ERROR{RESET} {name}: could not parse .nvchecker.toml — {e}")
            continue

        # Drop [__config__] if present; copy only the package entry sections
        for key, val in data.items():
            if key == "__config__":
                continue
            if not isinstance(val, dict):
                continue
            # Serialise section back to TOML manually (values are always str/bool)
            lines = [f'["{key}"]' if "." in key or "-" in key else f"[{key}]"]
            for k, v in val.items():
                if isinstance(v, bool):
                    lines.append(f"{k} = {'true' if v else 'false'}")
                else:
                    escaped = v.replace("\\", "\\\\").replace('"', '\\"')
                    lines.append(f'{k} = "{escaped}"')
            sections.append("\n".join(lines))
            included[key] = pkg_dir

    return "\n\n".join(sections) + "\n", included, warnings


def main() -> None:
    pkg_dirs = sorted(
        d for d in REPO_ROOT.iterdir()
        if d.is_dir() and (d / "PKGBUILD").exists()
    )

    if not pkg_dirs:
        print("No package directories found.")
        sys.exit(1)

    print(f"Checking {len(pkg_dirs)} packages in {REPO_ROOT}\n")

    combined_toml, included, warnings = build_combined_toml(pkg_dirs)

    for w in warnings:
        print(w)

    if not included:
        print("No packages to check.")
        return

    entries = run_nvchecker(combined_toml)

    # Index results by package name
    results: dict[str, dict] = {}
    errors: dict[str, list[str]] = {}
    for entry in entries:
        name = entry.get("name")
        if not name:
            continue
        if entry.get("version"):
            results[name] = entry
        elif entry.get("level") in ("error", "warning"):
            errors.setdefault(name, []).append(entry.get("event", "unknown error"))

    if warnings:
        print()

    for name, pkg_dir in sorted(included.items()):
        srcinfo = pkg_dir / ".SRCINFO"
        current = get_current_version(srcinfo)
        if current is None:
            print(f"{YELLOW}WARN{RESET}  {name}: could not parse pkgver from .SRCINFO")
            continue

        if name in results:
            latest = results[name]["version"]
            if latest != current:
                print(f"{GREEN}{BOLD}UPDATE{RESET} {name}: {current} → {latest}")
        elif name in errors:
            msgs = "; ".join(errors[name])
            print(f"{RED}ERROR{RESET} {name}: {msgs}")
        else:
            print(f"{RED}ERROR{RESET} {name}: nvchecker returned no version info")


if __name__ == "__main__":
    main()
