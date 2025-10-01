#!/usr/bin/env python3
"""
Inwestor Pro - Narzędzie do automatycznej analizy stron internetowych
i generowania perswazyjnych broszur inwestycyjnych w języku polskim.

Autor: Inwestor Pro Team
Wersja: 1.0.0
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

import openai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def load_api_key() -> Optional[str]:
    """
    Ładuje klucz API OpenAI z pliku .env.

    Returns:
        str: Klucz API lub None jeśli nie znaleziono
    """
    try:
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("Blad: Nie znaleziono klucza OPENAI_API_KEY w pliku .env")
            return None
        return api_key
    except Exception as e:
        print(f"Blad podczas ladowania klucza API: {e}")
        return None


def save_markdown_file(filename: str, content: str) -> bool:
    """
    Zapisuje broszurę do pliku w strukturze katalogów wyniki/YYYY-MM-DD/.

    Args:
        filename: Nazwa pliku (bez rozszerzenia)
        content: Zawartość broszury do zapisania

    Returns:
        bool: True jeśli zapisano pomyślnie, False w przypadku błędu
    """
    try:
        # Utwórz strukturę katalogów: wyniki/YYYY-MM-DD/
        today = datetime.now().strftime("%Y-%m-%d")
        output_dir = Path("wyniki") / today
        output_dir.mkdir(parents=True, exist_ok=True)

        # Utwórz pełną ścieżkę do pliku
        if not filename.endswith(".md"):
            filename += ".md"

        output_path = output_dir / filename

        # Zapisz plik
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Broszura zapisana do pliku: {output_path}")
        return True

    except Exception as e:
        print(f"Blad podczas zapisywania pliku: {e}")
        return False


def get_system_prompt() -> str:
    """
    Zwraca system prompt dla modelu OpenAI.

    Returns:
        str: System prompt
    """
    return """Jesteś ekspertem w dziedzinie analizy inwestycyjnej i tworzenia 
perswazyjnych materiałów sprzedażowych. Twoim zadaniem jest przeanalizowanie 
treści strony internetowej i wygenerowanie profesjonalnej broszury 
inwestycyjnej w języku polskim.

BROSZURA MUSI ZAWIERAĆ NASTĘPUJĄCE SEKCJE:

1. **Tytuł Broszury** - Atrakcyjny, perswazyjny tytuł zachęcający do inwestycji
2. **Podsumowanie Inwestycyjne** - Krótkie (3-4 zdania) perswazyjne uzasadnienie, 
   dlaczego warto zainwestować
3. **Propozycje Wartości** - Wypunktowane kluczowe korzyści i przewagi 
   konkurencyjne
4. **Kluczowe Dane** - 3-5 najważniejszych danych/faktów ze strony 
   (osiągnięcia, wielkość rynku, statystyki)
5. **Kategorie/Obszary** - Podział treści na logiczne kategorie 
   biznesowe/technologiczne
6. **Kluczowe Ryzyka** - 2-3 potencjalne ryzyka wynikające z analizy treści

WYMAGANIA:
- Ton: Sprzedażowy i perswazyjny, ukierunkowany na zachęcanie do inwestycji
- Język: Profesjonalny polski
- Format: Czysty Markdown z nagłówkami ##
- Długość: Zwięzłe, ale kompletne sekcje
- Skupienie: Na kluczowych danych inwestycyjnych i korzyściach biznesowych

Przeanalizuj podaną treść i wygeneruj broszurę zgodnie z powyższymi 
wytycznymi."""


def generate_brochure(text_content: str, api_key: str) -> Optional[str]:
    """
    Generuje broszurę inwestycyjną używając OpenAI API.

    Args:
        text_content: Oczyszczony tekst do analizy
        api_key: Klucz API OpenAI

    Returns:
        str: Wygenerowana broszura w formacie Markdown lub None w przypadku błędu
    """
    if not text_content or not api_key:
        return None

    try:
        # Konfiguruj klienta OpenAI
        client = openai.OpenAI(api_key=api_key)

        # Przygotuj wiadomości
        messages = [
            {"role": "system", "content": get_system_prompt()},
            {
                "role": "user",
                "content": f"Przeanalizuj następującą treść strony internetowej "
                f"i wygeneruj broszurę inwestycyjną:\n\n{text_content}",
            },
        ]

        # Wywołaj API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=2000,
            temperature=0.7,
        )

        return response.choices[0].message.content

    except openai.AuthenticationError:
        print("Blad: Nieprawidlowy klucz API OpenAI")
        return None
    except openai.RateLimitError:
        print("Blad: Przekroczono limit zapytan do API OpenAI")
        return None
    except openai.APITimeoutError:
        print("Blad: Timeout podczas komunikacji z API OpenAI")
        return None
    except openai.APIError as e:
        print(f"Blad API OpenAI: {e}")
        return None
    except Exception as e:
        print(f"Nieoczekiwany blad podczas generowania broszury: {e}")
        return None


def main():
    """
    Główna funkcja aplikacji - punkt wejścia dla CLI.
    """
    parser = argparse.ArgumentParser(
        description="Inwestor Pro - Generator perswazyjnych broszur",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Przyklady uzycia:
  python inwestor_pro.py --url https://example.com
  python inwestor_pro.py --url https://startup.pl --output broszura.md
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
        print("Blad: Podany URL nie jest prawidlowy.", file=sys.stderr)
        sys.exit(1)

    print("Inwestor Pro v1.0.0")
    print(f"Analizuje strone: {args.url}")

    # Załaduj klucz API
    print("Ladowanie klucza API...")
    api_key = load_api_key()
    if not api_key:
        return 1

    # Pobierz zawartość strony
    print("Pobieranie zawartosci strony...")
    html_content = fetch_html(args.url)

    if not html_content:
        print("Blad: Nie udalo sie pobrac zawartosci strony.")
        return 1

    # Wyczyść i ekstraktuj tekst
    print("Czyszczenie i ekstraktowanie tekstu...")
    clean_text = clean_and_extract_text(html_content, args.url)

    if not clean_text:
        print("Blad: Nie udalo sie wyodrebnic tekstu ze strony.")
        return 1

    print(f"Pobrano i wyczyszczono {len(clean_text)} znakow tekstu.")

    if args.verbose:
        print(f"Przykladowy tekst: {clean_text[:200]}...")

    # Generuj broszurę inwestycyjną
    print("Generowanie broszury inwestycyjnej...")
    brochure = generate_brochure(clean_text, api_key)

    if not brochure:
        print("Blad: Nie udalo sie wygenerowac broszury.")
        return 1

    # Zapisz broszurę do pliku
    output_filename = (
        args.output or f"broszura_{urlparse(args.url).netloc.replace('.', '_')}"
    )

    if not save_markdown_file(output_filename, brochure):
        return 1

    print("Broszura inwestycyjna zostala wygenerowana pomyslnie!")
    return 0


def fetch_html(url: str, timeout: int = 30) -> Optional[str]:
    """
    Pobiera zawartość HTML strony internetowej.

    Args:
        url: URL strony do pobrania
        timeout: Timeout w sekundach (domyślnie 30)

    Returns:
        str: Zawartość HTML strony lub None w przypadku błędu
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        # Sprawdź czy odpowiedź to HTML
        content_type = response.headers.get("content-type", "").lower()
        if "text/html" not in content_type:
            print(
                f"Ostrzezenie: Strona nie zwraca HTML "
                f"(content-type: {content_type})"
            )

        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Blad podczas pobierania strony {url}: {e}")
        return None
    except Exception as e:
        print(f"Nieoczekiwany blad podczas pobierania strony: {e}")
        return None


def clean_and_extract_text(html_content: str, base_url: str = "") -> str:
    """
    Czyści HTML i ekstraktuje czysty tekst.

    Args:
        html_content: Zawartość HTML do oczyszczenia
        base_url: Bazowy URL do filtrowania linków zewnętrznych

    Returns:
        str: Oczyszczony tekst
    """
    if not html_content:
        return ""

    try:
        soup = BeautifulSoup(html_content, "html.parser")

        # Usuń niepotrzebne elementy
        for element in soup(
            [
                "script",
                "style",
                "nav",
                "footer",
                "header",
                "aside",
                "noscript",
                "iframe",
                "object",
                "embed",
            ]
        ):
            element.decompose()

        # Usuń elementy z klasami reklamowymi
        ad_pattern = re.compile(r"(ad|advertisement|banner|popup|modal)", re.I)
        for element in soup.find_all(class_=ad_pattern):
            element.decompose()

        # Usuń elementy z atrybutami reklamowymi
        banner_pattern = re.compile(r"(ad|advertisement|banner)", re.I)
        for element in soup.find_all(attrs={"id": banner_pattern}):
            element.decompose()

        # Usuń linki zewnętrzne jeśli podano base_url
        if base_url:
            base_domain = urlparse(base_url).netloc
            for link in soup.find_all("a", href=True):
                href = link.get("href")
                if href:
                    # Konwertuj względne linki na bezwzględne
                    absolute_url = urljoin(base_url, href)
                    parsed_href = urlparse(absolute_url)

                    # Jeśli link prowadzi poza domenę, usuń go
                    if parsed_href.netloc and parsed_href.netloc != base_domain:
                        link.decompose()

        # Usuń puste elementy
        for element in soup.find_all():
            if not element.get_text(strip=True) and not element.find_all():
                element.decompose()

        # Ekstraktuj tekst
        text = soup.get_text(separator=" ", strip=True)

        # Oczyść tekst z nadmiarowych białych znaków
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        return text

    except Exception as e:
        print(f"Blad podczas czyszczenia HTML: {e}")
        return ""


def is_valid_url(url: str) -> bool:
    """
    Sprawdza czy podany string jest prawidlowym URL.

    Args:
        url: String do sprawdzenia

    Returns:
        bool: True jesli URL jest prawidlowy, False w przeciwnym razie
    """
    # Sprawdź czy url nie jest None lub pusty
    if not url or not isinstance(url, str):
        return False

    # Prosty regex do walidacji URL
    url_pattern = re.compile(
        r"^https?://"  # http:// lub https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # IP
        r"(?::\d+)?"  # opcjonalny port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return bool(url_pattern.match(url))


if __name__ == "__main__":
    sys.exit(main())
