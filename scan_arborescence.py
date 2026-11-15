#!/usr/bin/env python3
"""
Scanne l'arborescence du dossier dans lequel se trouve ce script
et l'exporte dans un fichier texte (arborescence.txt).

Usage :
    python3 scan_arborescence.py

Le script ignore les dossiers/fichiers cachés (ceux qui commencent par un point,
comme .git, .DS_Store...) et lui-même.
"""

import os
import sys

SCRIPT_NAME = os.path.basename(__file__)
OUTPUT_NAME = "arborescence.txt"
IGNORE_PREFIXES = (".",)  # ignore fichiers/dossiers cachés


def should_ignore(name: str) -> bool:
    return name.startswith(IGNORE_PREFIXES) or name in (SCRIPT_NAME, OUTPUT_NAME)


def scan_dir(path: str, prefix: str = "", lines=None):
    if lines is None:
        lines = []

    entries = [e for e in os.listdir(path) if not should_ignore(e)]
    # Dossiers d'abord, puis fichiers, ordre alphabétique dans chaque groupe
    entries.sort(key=lambda e: (not os.path.isdir(os.path.join(path, e)), e.lower()))

    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = (i == len(entries) - 1)
        connector = "└── " if is_last else "├── "
        is_dir = os.path.isdir(full_path)
        lines.append(f"{prefix}{connector}{entry}{'/' if is_dir else ''}")

        if is_dir:
            extension = "    " if is_last else "│   "
            scan_dir(full_path, prefix + extension, lines)

    return lines


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    root_name = os.path.basename(root)

    lines = [f"{root_name}/"]
    lines += scan_dir(root)

    output_path = os.path.join(root, OUTPUT_NAME)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Arborescence exportée dans : {output_path}")
    print()
    print("\n".join(lines))


if __name__ == "__main__":
    main()
