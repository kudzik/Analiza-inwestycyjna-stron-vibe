# Inwestor Pro

Narzędzie do automatycznej analizy stron internetowych i generowania perswazyjnych broszur inwestycyjnych w języku polskim.

## Opis

Inwestor Pro to aplikacja CLI napisana w Pythonie, która automatycznie analizuje pojedynczą stronę internetową i generuje perswazyjną broszurę inwestycyjną w formacie Markdown, wykorzystując API OpenAI.

## Funkcjonalności

- **Web Scraping**: Pobieranie treści z pojedynczej strony internetowej
- **Czyszczenie danych**: Usuwanie elementów nawigacyjnych, reklam i nieistotnych treści
- **Analiza AI**: Przetwarzanie przez OpenAI z perswazyjnym tonem
- **Generowanie broszury**: Strukturalny plik Markdown z sekcjami:
  - Tytuł broszury
  - Podsumowanie inwestycyjne
  - Propozycje wartości
  - Kluczowe dane
  - Kategorie/obszary
  - Kluczowe ryzyka

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone <repository-url>
cd Analiza-inwestycyjna-stron-vibe
```

2. Utwórz wirtualne środowisko:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# lub
source venv/bin/activate  # Linux/Mac
```

3. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

4. Skonfiguruj zmienne środowiskowe:

```bash
# Skopiuj plik env.example do .env i uzupełnij klucz API
copy env.example .env
```

5. Edytuj plik `.env` i dodaj swój klucz OpenAI:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Użycie

```bash
python inwestor_pro.py --url https://example.com
python inwestor_pro.py --url https://startup.pl --output broszura_startup.md
python inwestor_pro.py --url https://company.com --verbose
```

### Parametry

- `--url` (wymagany): URL strony internetowej do analizy
- `--output` (opcjonalny): Nazwa pliku wyjściowego (domyślnie: broszura\_[domena].md)
- `--verbose` (opcjonalny): Wyświetl szczegółowe informacje o procesie

## Wymagania

- Python 3.8+
- Klucz API OpenAI
- Połączenie internetowe

## Struktura projektu

```
├── docs/
│   ├── PRD.md          # Dokument Wymagań Produktu
│   └── TODO.md         # Lista zadań
├── inwestor_pro.py     # Główny plik aplikacji
├── requirements.txt    # Zależności Python
├── setup.py           # Konfiguracja pakietu
├── env.example        # Przykład konfiguracji środowiska
└── README.md          # Ten plik
```

## Status rozwoju

Projekt jest obecnie w fazie rozwoju. Funkcjonalności są implementowane zgodnie z planem w `docs/TODO.md`.

### Ukończone fazy:

- ✅ Faza 1: Konfiguracja i środowisko
- 🔄 Faza 2: Moduł interfejsu CLI (w trakcie)

## Licencja

MIT License

## Wsparcie

W przypadku problemów lub pytań, utwórz issue w repozytorium.
