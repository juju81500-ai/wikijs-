#!/usr/bin/env python3
"""Wrapper de compatibilité : le script actif est dans 03-qualite-tests/."""

import runpy
import sys
from pathlib import Path

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "03-qualite-tests" / "verify-wiki.py"), run_name="__main__")
    sys.exit(0)
