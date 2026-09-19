#!/usr/bin/env python3
"""
Retire TOUS les accents (é, è, à, ê, ô, ç, œ, æ...) des noms de fichiers
et dossiers dans data/, en utilisant `git mv` pour préserver l'historique.
Ça règle le problème à la racine : plus d'accents = plus de souci
d'encodage (NFC/NFD) entre ton OS et GitHub.

À lancer depuis la racine de ton dépôt (là où se trouve data/).

Usage :
    python3 remove_accents.py          # affiche ce qui serait renommé
    python3 remove_accents.py --apply  # effectue réellement les renommages
"""

import os
import subprocess
import sys
import unicodedata

ROOT = "data"

# Quelques caractères que la décomposition Unicode ne gère pas seule
EXTRA_MAP = {
    "œ": "oe", "Œ": "OE",
    "æ": "ae", "Æ": "AE",
    "ß": "ss",
    "ø": "o", "Ø": "O",
    "–": "-", "—": "-",   # tirets longs -> tiret simple
    "’": "'", "‘": "'",
    "…": "...",
}

def strip_accents(name: str) -> str:
    for src, dst in EXTRA_MAP.items():
        name = name.replace(src, dst)
    # Décompose (é -> e + accent combinant), puis supprime les marques
    # combinantes (catégorie Unicode "Mn" = accents détachés).
    nfkd = unicodedata.normalize("NFKD", name)
    return "".join(c for c in nfkd if unicodedata.category(c) != "Mn")

def git_mv(old_path, new_path):
    """Renomme via git mv. Si git refuse (dossier vide, non suivi...),
    bascule sur un simple renommage disque — sans perte, juste sans
    historique Git pour cet élément précis (rien à perdre s'il est vide)."""
    result = subprocess.run(
        ["git", "mv", old_path, new_path],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        try:
            os.rename(old_path, new_path)
            print(f"  (renommage disque simple, git mv indisponible ici)")
        except OSError as e:
            print(f"  ÉCHEC pour {old_path} : {e}")
            return False
    return True

def main():
    apply = "--apply" in sys.argv

    if not os.path.isdir(ROOT):
        print(f"Erreur : le dossier '{ROOT}' n'existe pas ici. "
              f"Lance ce script depuis la racine de ton dépôt.")
        sys.exit(1)

    # topdown=False : on renomme d'abord les éléments les plus profonds,
    # pour ne jamais casser un chemin en cours de route.
    changes = []
    for dirpath, dirnames, filenames in os.walk(ROOT, topdown=False):
        for name in filenames + dirnames:
            cleaned = strip_accents(name)
            if cleaned != name:
                old_full = os.path.join(dirpath, name)
                new_full = os.path.join(dirpath, cleaned)
                changes.append((old_full, new_full))

    if not changes:
        print("Rien à renommer — aucun accent trouvé.")
        return

    print(f"{len(changes)} élément(s) à renommer :\n")
    for old, new in changes:
        print(f"  {old}\n  → {new}\n")

    if not apply:
        print("Mode simulation (rien n'a été modifié).")
        print("Relance avec --apply pour effectuer les renommages :")
        print("  python3 remove_accents.py --apply")
        return

    print("Application des renommages via git mv...")
    ok, failed = 0, 0
    for old, new in changes:
        if git_mv(old, new):
            ok += 1
        else:
            failed += 1
    print(f"\n{ok} élément(s) renommé(s), {failed} échec(s).")
    print("N'oublie pas de committer et pousser :")
    print('  git commit -m "Retire les accents des noms de fichiers"')
    print("  git push")

if __name__ == "__main__":
    main()
