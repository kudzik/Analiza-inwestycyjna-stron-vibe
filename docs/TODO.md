# TODO

## 🛠️ Lista To Do: Aplikacja Inwestor Pro (MVP)

### Faza 1: Konfiguracja i Środowisko (Setup)

|  Status   | Krok    | Zadanie                                                                                              | Priorytet |
| :-------: | :------ | :--------------------------------------------------------------------------------------------------- | :-------- |
| $\square$ | **1.1** | Utwórz plik `.gitignore`.                                                                            | Wysoki    |
| $\square$ | **1.2** | Utwórz wirtualne środowisko Pythona i aktywuj je.                                                    | Wysoki    |
| $\square$ | **1.3** | Zainstaluj wymagane biblioteki: `requests`, `beautifulsoup4`, `openai`, `python-dotenv`, `argparse`. | Wysoki    |
| $\square$ | **1.4** | Stwórz plik `requirements.txt` i `setup.py` (jeśli planujesz dystrybucję).                           | Wysoki    |
| $\square$ | **1.5** | Utwórz plik konfiguracji środowiska **`.env`** i dodaj zmienną `OPENAI_API_KEY`.                     | Wysoki    |
| $\square$ | **1.6** | Zainicjuj główny plik aplikacji, np. `inwestor_pro.py`.                                              | Wysoki    |

---

### Faza 2: Moduł Interfejsu Linii Komend (CLI)

|  Status   | Krok    | Zadanie                                                                                   | Priorytet |
| :-------: | :------ | :---------------------------------------------------------------------------------------- | :-------- |
| $\square$ | **2.1** | Zaimplementuj funkcję parsowania argumentów (za pomocą `argparse`).                       | Wysoki    |
| $\square$ | **2.2** | Ustaw obowiązkowy argument `--url` dla adresu strony do analizy.                          | Wysoki    |
| $\square$ | **2.3** | Dodaj walidację, aby upewnić się, że podany argument `--url` jest poprawnym formatem URL. | Średni    |
| $\square$ | **2.4** | Zaimplementuj funkcję ładowania klucza API z pliku `.env`.                                | Wysoki    |

---

### Faza 3: Moduł Pobierania i Czyszczenia Danych (Scraping & Cleaning)

|  Status   | Krok    | Zadanie                                                                                                      | Priorytet |
| :-------: | :------ | :----------------------------------------------------------------------------------------------------------- | :-------- |
| $\square$ | **3.1** | Zaimplementuj funkcję `fetch_html(url)` używającą **`requests`** do pobrania zawartości strony.              | Wysoki    |
| $\square$ | **3.2** | Zaimplementuj funkcję `clean_and_extract_text(html_content)`.                                                | Wysoki    |
| $\square$ | **3.3** | W funkcji czyszczącej, użyj **`BeautifulSoup`** do:                                                          | Wysoki    |
|           |         | a. Usunięcia skryptów (`<script>`) i stylów (`<style>`).                                                     |           |
|           |         | b. Usunięcia elementów nieistotnych dla treści (np. `<nav>`, `<footer>`, reklamy).                           |           |
|           |         | c. Ekstrakcji czystego, widocznego tekstu.                                                                   |           |
| $\square$ | **3.4** | Zaimplementuj prostą logikę do usuwania linków zewnętrznych/partnerskich, jeśli występują w pobranej treści. | Średni    |

---

### Faza 4: Moduł Analizy (OpenAI API Integration)

|  Status   | Krok    | Zadanie                                                                                                                               | Priorytet |
| :-------: | :------ | :------------------------------------------------------------------------------------------------------------------------------------ | :-------- |
| $\square$ | **4.1** | Zdefiniuj szczegółowy **System Prompt** dla modelu **`gpt-4-mini`**.                                                                  | Wysoki    |
|           |         | _Prompt musi zawierać wymagania:_                                                                                                     |           |
|           |         | a. **Ton:** Sprzedażowy i perswazyjny.                                                                                                |           |
|           |         | b. **Struktura:** Wygenerowanie wymaganych sekcji (Podsumowanie Inwestycyjne, Ryzyka, Propozycje Wartości, Kluczowe Dane, Kategorie). |           |
|           |         | c. **Format Wyjściowy:** Czysty Markdown.                                                                                             |           |
|           |         | d. **Język:** Polski.                                                                                                                 |           |
| $\square$ | **4.2** | Zaimplementuj funkcję `generate_brochure(text_content, api_key)` do wywołania API OpenAI.                                             | Wysoki    |
| $\square$ | **4.3** | Zaimplementuj obsługę błędów API (np. brak klucza, przekroczony limit, błąd serwera).                                                 | Wysoki    |

---

### Faza 5: Generowanie Wyniku i Testowanie (Output & Testing)

|  Status   | Krok    | Zadanie                                                                                                          | Priorytet |
| :-------: | :------ | :--------------------------------------------------------------------------------------------------------------- | :-------- |
| $\square$ | **5.1** | Zaimplementuj funkcję `save_markdown_file(filename, content)`.                                                   | Wysoki    |
| $\square$ | **5.2** | Ustaw logiczne nazewnictwo plików wyjściowych (np. `broszura_[nazwa_domeny].md`).                                | Średni    |
| $\square$ | **5.3** | Stwórz i wykonaj test integracyjny: Uruchom aplikację na przynajmniej **trzech różnych stronach internetowych**. | Wysoki    |
| $\square$ | **5.4** | **Weryfikacja jakości:** Sprawdź, czy wygenerowane broszury spełniają wymagania PRD (ton, sekcje, język polski). | Wysoki    |
| $\square$ | **5.5** | Ostateczna refaktoryzacja i linting kodu.                                                                        | Średni    |
