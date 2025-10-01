#!/usr/bin/env python3
"""
Inwestor Pro - Narzędzie do automatycznej analizy stron internetowych
i generowania perswazyjnych broszur inwestycyjnych w języku polskim.

Autor: Inwestor Pro Team
Wersja: 1.0.0
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

# Importy będą dodane w kolejnych fazach
# import requests
# from bs4 import BeautifulSoup
# import openai
# from dotenv import load_dotenv


def main():
    """
    Główna funkcja aplikacji - punkt wejścia dla CLI.
    """
    parser = argparse.ArgumentParser(
        description="Inwestor Pro - Generator perswazyjnych broszur inwestycyjnych",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Przyklady uzycia:
  python inwestor_pro.py --url https://example.com
  python inwestor_pro.py --url https://startup.pl --output broszura_startup.md
        """,
    )

    parser.add_argument(
        "--url", required=True, help="URL strony internetowej do analizy"
    )

    parser.add_argument(
        "--output", help="Nazwa pliku wyjsciowego (domyslnie: broszura_[domena].md)"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Wyswietl szczegolowe informacje o procesie",
    )

    args = parser.parse_args()

    # Walidacja URL
    if not is_valid_url(args.url):
        print("Blad: Podany URL nie jest prawidlowy.")
        sys.exit(1)

    print("Inwestor Pro v1.0.0")
    print(f"Analizuje strone: {args.url}")

    # TODO: Implementacja w kolejnych fazach
    print(
        "Aplikacja jest w fazie rozwoju. Funkcjonalnosci beda dodane w kolejnych krokach."
    )

    return 0


def is_valid_url(url: str) -> bool:
    """
    Sprawdza czy podany string jest prawidlowym URL.

    Args:
        url: String do sprawdzenia

    Returns:
        bool: True jesli URL jest prawidlowy, False w przeciwnym razie
    """
    import re

    # Prosty regex do walidacji URL
    url_pattern = re.compile(
        r"^https?://"  # http:// lub https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # domena
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # IP
        r"(?::\d+)?"  # opcjonalny port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return bool(url_pattern.match(url))


if __name__ == "__main__":
    sys.exit(main())
