# Inwestor Pro

Narzędzie do automatycznej analizy stron internetowych i generowania perswazyjnych broszur inwestycyjnych w języku polskim.

## Opis

Inwestor Pro to aplikacja CLI napisana w Pythonie, która automatycznie analizuje pojedynczą stronę internetową i generuje perswazyjną broszurę inwestycyjną w formacie Markdown, wykorzystując API OpenAI.

## Funkcjonalności

- **Web Scraping**: Pobieranie treści z pojedynczej strony internetowej
- **Analiza podstron**: Automatyczne wykrywanie i pobieranie treści z podstron w obrębie tej samej domeny
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

### Wymagania systemowe

- Python 3.8 lub nowszy
- Klucz API OpenAI
- Połączenie internetowe

### Krok po kroku

1. **Sklonuj repozytorium:**

```bash
git clone https://github.com/your-username/Analiza-inwestycyjna-stron-vibe.git
cd Analiza-inwestycyjna-stron-vibe
```

2. **Utwórz wirtualne środowisko:**

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# lub
source venv/bin/activate  # Linux/Mac
```

3. **Zainstaluj zależności:**

```bash
pip install -r requirements.txt
```

4. **Skonfiguruj zmienne środowiskowe:**

```bash
# Skopiuj plik env.example do .env i uzupełnij klucz API
copy env.example .env  # Windows
# lub
cp env.example .env    # Linux/Mac
```

5. **Edytuj plik `.env` i dodaj swój klucz OpenAI:**

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Użycie

### Podstawowe użycie

```bash
python inwestor_pro.py --url https://example.com
```

Aplikacja automatycznie:

1. Pobiera zawartość strony internetowej
2. Wykrywa i pobiera treść z podstron w obrębie tej samej domeny
3. Czyści HTML i ekstraktuje tekst z wszystkich stron
4. Usuwa reklamy, skrypty i linki zewnętrzne
5. Łączy treść z głównej strony i podstron
6. Generuje broszurę inwestycyjną używając AI
7. Zapisuje wynik do pliku w strukturze `wyniki/YYYY-MM-DD/`

### Zaawansowane opcje

```bash
# Z niestandardową nazwą pliku wyjściowego
python inwestor_pro.py --url https://startup.pl --output broszura_startup

# Z ograniczeniem liczby podstron do analizy
python inwestor_pro.py --url https://company.com --max-subpages 3

# Z szczegółowymi informacjami o procesie
python inwestor_pro.py --url https://company.com --verbose

# Pomoc
python inwestor_pro.py --help
```

### Struktura plików wyjściowych

Aplikacja automatycznie tworzy strukturę katalogów:

```
wyniki/
└── 2025-10-01/          # Data generowania
    ├── broszura_example_com.md
    ├── broszura_startup_pl.md
    └── moja_broszura.md
```

Pliki są zapisywane w katalogu `wyniki/YYYY-MM-DD/` gdzie `YYYY-MM-DD` to data generowania broszury.

### Weryfikacja jakości

Aplikacja została przetestowana na różnych typach stron internetowych:

1. **Strony HTML** (example.com) - Standardowe strony internetowe
2. **API JSON** (httpbin.org/json) - Strony zwracające dane JSON
3. **Serwisy API** (jsonplaceholder.typicode.com) - Dokumentacja API
4. **Literatura** (httpbin.org/html) - Strony z treścią literacką

Wszystkie wygenerowane broszury spełniają wymagania:

- ✅ **Ton sprzedażowy i perswazyjny**
- ✅ **Wszystkie wymagane sekcje** (Tytuł, Podsumowanie, Propozycje Wartości, Kluczowe Dane, Kategorie, Ryzyka)
- ✅ **Język polski**
- ✅ **Format Markdown**
- ✅ **Struktura katalogów z datą**

### Parametry

| Parametr         | Typ    | Wymagany | Opis                                                     |
| ---------------- | ------ | -------- | -------------------------------------------------------- |
| `--url`          | string | ✅       | URL strony internetowej do analizy                       |
| `--output`       | string | ❌       | Nazwa pliku wyjściowego (domyślnie: `broszura_[domena]`) |
| `--max-subpages` | int    | ❌       | Maksymalna liczba podstron do analizy (domyślnie: 5)     |
| `--verbose`      | flag   | ❌       | Wyświetl szczegółowe informacje o procesie               |

## Przykład wyjścia

Wygenerowana broszura zawiera następujące sekcje:

```markdown
# Analiza Inwestycyjna: [Nazwa Firmy] – Wyjątkowa Szansa Rynkowa

## Podsumowanie Inwestycyjne

[Perswazyjne uzasadnienie inwestycji w 3-4 zdaniach]

## Propozycje Wartości

- [Kluczowe korzyści i przewagi konkurencyjne]

## Kluczowe Dane

- [3-5 najważniejszych danych/faktów]

## Kategorie/Obszary

[Podział treści na logiczne kategorie biznesowe]

## Kluczowe Ryzyka

[2-3 potencjalne ryzyka wynikające z analizy]
```

## Struktura projektu

```
├── docs/
│   ├── PRD.md          # Dokument Wymagań Produktu
│   ├── TODO.md         # Lista zadań
│   └── TESTING.md      # Dokumentacja testów
├── inwestor_pro.py     # Główny plik aplikacji
├── test_inwestor_pro.py # Testy jednostkowe i integracyjne
├── requirements.txt    # Zależności Python
├── setup.py           # Konfiguracja pakietu
├── env.example        # Przykład konfiguracji środowiska
├── .gitignore         # Pliki ignorowane przez Git
├── htmlcov/           # Raporty pokrycia kodu (HTML)
└── README.md          # Ten plik
```

## Rozwój

### Status projektu

Projekt jest obecnie w fazie rozwoju MVP. Funkcjonalności są implementowane zgodnie z planem w `docs/TODO.md`.

#### Ukończone fazy

- ✅ **Faza 1**: Konfiguracja i środowisko
- ✅ **Faza 2**: Moduł interfejsu CLI
- ✅ **Faza 3**: Moduł pobierania i czyszczenia danych
- ✅ **Faza 4**: Moduł analizy (OpenAI API)
- ✅ **Faza 5**: Generowanie wyniku i testowanie
- ✅ **Testy**: Kompletny zestaw testów jednostkowych i integracyjnych

### Wkład w rozwój

1. Fork repozytorium
2. Utwórz branch dla nowej funkcjonalności (`git checkout -b feature/nowa-funkcjonalnosc`)
3. Commit zmiany (`git commit -am 'Dodaj nową funkcjonalność'`)
4. Push do branch (`git push origin feature/nowa-funkcjonalnosc`)
5. Utwórz Pull Request

### Testowanie

```bash
# Uruchom testy jednostkowe i integracyjne
python test_inwestor_pro.py

# Uruchom testy z pokryciem kodu
coverage run test_inwestor_pro.py
coverage report
coverage html  # Generuje raport HTML w htmlcov/

# Sprawdź jakość kodu
pylint inwestor_pro.py
mypy inwestor_pro.py
```

#### Wyniki testów

- **✅ 36/36 testów przechodzi pomyślnie**
- **📊 Pokrycie kodu: 92%**
- **🎯 Główny moduł: 84% pokrycia**
- **🧪 Testy: 97% pokrycia**

#### Kategorie testów

1. **Testy walidacji URL** (5 testów)

   - Prawidłowe URL HTTPS/HTTP
   - Nieprawidłowe URL
   - Case-insensitive
   - Localhost i adresy IP

2. **Testy CLI** (6 testów)

   - Wyświetlanie pomocy
   - Prawidłowe argumenty
   - Nieprawidłowe argumenty
   - Flagi opcjonalne

3. **Testy Web Scraping** (9 testów)

   - Pobieranie HTML z prawidłowych URL
   - Obsługa błędów sieciowych
   - Czyszczenie HTML i ekstraktowanie tekstu
   - Usuwanie skryptów, stylów i reklam
   - Filtrowanie linków zewnętrznych

4. **Testy AI** (7 testów)

   - Generowanie system prompt
   - Ładowanie klucza API
   - Generowanie broszury inwestycyjnej
   - Obsługa błędów API
   - Walidacja danych wejściowych

5. **Testy operacji na plikach** (5 testów)

   - Zapisywanie plików w strukturze katalogów
   - Tworzenie katalogów z datą
   - Obsługa błędów zapisu
   - Walidacja nazw plików
   - Testy z różnymi typami zawartości

6. **Testy integracyjne** (2 testy)
   - Import modułów
   - Struktura aplikacji

## Rozwiązywanie problemów

### Częste problemy

**Problem**: `ModuleNotFoundError: No module named 'openai'`
**Rozwiązanie**: Upewnij się, że aktywowałeś wirtualne środowisko i zainstalowałeś zależności:

```bash
source venv/bin/activate  # lub venv\Scripts\activate na Windows
pip install -r requirements.txt
```

**Problem**: `OpenAI API key not found`
**Rozwiązanie**: Sprawdź, czy plik `.env` istnieje i zawiera poprawny klucz API:

```bash
cat .env  # Linux/Mac
type .env  # Windows
```

**Problem**: `Connection error`
**Rozwiązanie**: Sprawdź połączenie internetowe i poprawność URL.

### Logi debugowania

Użyj flagi `--verbose` aby zobaczyć szczegółowe informacje o procesie:

```bash
python inwestor_pro.py --url https://example.com --verbose
```

## Licencja

MIT License - zobacz plik [LICENSE](LICENSE) dla szczegółów.

## Wsparcie

- **Issues**: [GitHub Issues](https://github.com/your-username/Analiza-inwestycyjna-stron-vibe/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/Analiza-inwestycyjna-stron-vibe/discussions)
- **Email**: kudzik@outlook.com

## Changelog

### v1.0.0 (Planowane)

- Pierwsza wersja MVP
- Podstawowa funkcjonalność analizy stron
- Generowanie broszur inwestycyjnych
- Interfejs CLI

---

**Inwestor Pro** - Automatyzacja analizy inwestycyjnej stron internetowych 🚀
