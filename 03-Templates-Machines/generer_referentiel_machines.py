#!/usr/bin/env python3
"""Genere Referentiel_Machines.md : une ligne par OS/version.

Colonnes automatiques : famille, nombre et lien des fiches simples/completes.
Colonnes manuelles (Role, Template, Statut, Notes) : laissees vides a la
creation puis conservees telles quelles a chaque regeneration.
Bibliotheque standard uniquement.
Usage : python3 03-Templates-Machines/generer_referentiel_machines.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "Referentiel_Machines.md"
SIMPLES, COMPLETES = "01-Fiches-Simples", "02-Fiches-Completes"
MANUAL = ["Rôle", "Template utilisé", "Statut", "Notes"]
FAMILLES = {
    "Debian": "Linux Debian", "Ubuntu": "Linux Debian", "Rocky-Linux": "Linux RedHat",
    "Alpine": "Linux léger", "Windows": "Windows", "Proxmox": "Hyperviseur",
    "VMware": "Hyperviseur", "TrueNAS": "Stockage", "OPNsense": "Pare-feu",
    "pfSense": "Pare-feu", "Transverses": "Transverse", "Logiciels": "Logiciel",
}


def count_by_key(section: str) -> dict[tuple[str, str], int]:
    counts: dict[tuple[str, str], int] = {}
    base = ROOT / section
    for md in base.rglob("*.md"):
        parts = md.relative_to(base).parts
        if len(parts) < 3 or md.name == "README.md":
            continue
        key = (parts[0], parts[1])
        counts[key] = counts.get(key, 0) + 1
    return counts


def read_manual() -> dict[str, list[str]]:
    saved: dict[str, list[str]] = {}
    if not OUT.exists():
        return saved
    for line in OUT.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or line.startswith("| OS") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 + len(MANUAL):
            saved[f"{cells[0]}/{cells[1]}"] = cells[-len(MANUAL):]
    return saved


def cell(section: str, key: tuple[str, str], n: int) -> str:
    return f"[{n}](../{section}/{key[0]}/{key[1]}/)" if n else ""


def main() -> None:
    simples, completes = count_by_key(SIMPLES), count_by_key(COMPLETES)
    saved = read_manual()
    lines = [
        "# Référentiel machines — OS, versions et couverture des fiches",
        "",
        "- **Tags** : `template`, `referentiel`, `index`",
        "",
        "Généré par `03-Templates-Machines/generer_referentiel_machines.py`. Les colonnes "
        "**Famille**, **Simples** et **Complètes** sont recalculées à chaque exécution. "
        "Les colonnes **Rôle**, **Template utilisé**, **Statut** et **Notes** se remplissent "
        "à la main et sont conservées à la régénération.",
        "",
        "| OS | Version | Famille | Simples | Complètes | " + " | ".join(MANUAL) + " |",
        "|---|---|---|---|---|" + "---|" * len(MANUAL),
    ]
    for key in sorted(set(simples) | set(completes)):
        manual = saved.get(f"{key[0]}/{key[1]}", [""] * len(MANUAL))
        row = [key[0], key[1], FAMILLES.get(key[0], ""),
               cell(SIMPLES, key, simples.get(key, 0)),
               cell(COMPLETES, key, completes.get(key, 0)), *manual]
        lines.append("| " + " | ".join(row) + " |")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(lines) - 7} lignes écrites dans {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
