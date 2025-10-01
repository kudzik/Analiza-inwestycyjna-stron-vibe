# TODO

## 🛠️ Lista To Do: Aplikacja Inwestor Pro (MVP)

### Faza 1: Konfiguracja i Środowisko (Setup)

| Status | Krok    | Zadanie                                                                                              | Priorytet |
| :----: | :------ | :--------------------------------------------------------------------------------------------------- | :-------- |
|   ✅   | **1.1** | Utwórz plik `.gitignore`.                                                                            | Wysoki    |
|   ✅   | **1.2** | Utwórz wirtualne środowisko Pythona i aktywuj je.                                                    | Wysoki    |
|   ✅   | **1.3** | Zainstaluj wymagane biblioteki: `requests`, `beautifulsoup4`, `openai`, `python-dotenv`, `argparse`. | Wysoki    |
|   ✅   | **1.4** | Stwórz plik `requirements.txt` i `setup.py` (jeśli planujesz dystrybucję).                           | Wysoki    |
|   ✅   | **1.5** | Utwórz plik konfiguracji środowiska **`.env`** i dodaj zmienną `OPENAI_API_KEY`.                     | Wysoki    |
|   ✅   | **1.6** | Zainicjuj główny plik aplikacji, np. `inwestor_pro.py`.                                              | Wysoki    |

---

### Faza 2: Moduł Interfejsu Linii Komend (CLI)

| Status | Krok    | Zadanie                                                                                   | Priorytet |
| :----: | :------ | :---------------------------------------------------------------------------------------- | :-------- |
|   🔄   | **2.1** | Zaimplementuj funkcję parsowania argumentów (za pomocą `argparse`).                       | Wysoki    |
|   ⏳   | **2.2** | Ustaw obowiązkowy argument `--url` dla adresu strony do analizy.                          | Wysoki    |
|   ⏳   | **2.3** | Dodaj walidację, aby upewnić się, że podany argument `--url` jest poprawnym formatem URL. | Średni    |
|   ⏳   | **2.4** | Zaimplementuj funkcję ładowania klucza API z pliku `.env`.                                | Wysoki    |

---

### Faza 3: Moduł Pobierania i Czyszczenia Danych (Scraping & Cleaning)

| Status | Krok    | Zadanie                                                                                                      | Priorytet |
| :----: | :------ | :----------------------------------------------------------------------------------------------------------- | :-------- |
|   ⏳   | **3.1** | Zaimplementuj funkcję `fetch_html(url)` używającą **`requests`** do pobrania zawartości strony.              | Wysoki    |
|   ⏳   | **3.2** | Zaimplementuj funkcję `clean_and_extract_text(html_content)`.                                                | Wysoki    |
|   ⏳   | **3.3** | W funkcji czyszczącej, użyj **`BeautifulSoup`** do:                                                          | Wysoki    |
|        |         | a. Usunięcia skryptów (`<script>`) i stylów (`<style>`).                                                     |           |
|        |         | b. Usunięcia elementów nieistotnych dla treści (np. `<nav>`, `<footer>`, reklamy).                           |           |
|        |         | c. Ekstrakcji czystego, widocznego tekstu.                                                                   |           |
|   ⏳   | **3.4** | Zaimplementuj prostą logikę do usuwania linków zewnętrznych/partnerskich, jeśli występują w pobranej treści. | Średni    |

---

### Faza 4: Moduł Analizy (OpenAI API Integration) ✅ UKOŃCZONA

| Status | Krok    | Zadanie                                                                                                                               | Priorytet |
| :----: | :------ | :------------------------------------------------------------------------------------------------------------------------------------ | :-------- |
|   ✅   | **4.1** | Zdefiniuj szczegółowy **System Prompt** dla modelu **`gpt-4-mini`**.                                                                  | Wysoki    |
|        |         | _Prompt musi zawierać wymagania:_                                                                                                     |           |
|        |         | a. **Ton:** Sprzedażowy i perswazyjny.                                                                                                |           |
|        |         | b. **Struktura:** Wygenerowanie wymaganych sekcji (Podsumowanie Inwestycyjne, Ryzyka, Propozycje Wartości, Kluczowe Dane, Kategorie). |           |
|        |         | c. **Format Wyjściowy:** Czysty Markdown.                                                                                             |           |
|        |         | d. **Język:** Polski.                                                                                                                 |           |
|   ✅   | **4.2** | Zaimplementuj funkcję `generate_brochure(text_content, api_key)` do wywołania API OpenAI.                                             | Wysoki    |
|   ✅   | **4.3** | Zaimplementuj obsługę błędów API (np. brak klucza, przekroczony limit, błąd serwera).                                                 | Wysoki    |

---

### Faza 5: Generowanie Wyniku i Testowanie (Output & Testing) ✅ UKOŃCZONA

| Status | Krok    | Zadanie                                                                                                          | Priorytet |
| :----: | :------ | :--------------------------------------------------------------------------------------------------------------- | :-------- |
|   ✅   | **5.1** | Zaimplementuj funkcję `save_markdown_file(filename, content)`.                                                   | Wysoki    |
|   ✅   | **5.2** | Ustaw logiczne nazewnictwo plików wyjściowych (np. `broszura_[nazwa_domeny].md`).                                | Średni    |
|   ✅   | **5.3** | Stwórz i wykonaj test integracyjny: Uruchom aplikację na przynajmniej **trzech różnych stronach internetowych**. | Wysoki    |
|   ✅   | **5.4** | **Weryfikacja jakości:** Sprawdź, czy wygenerowane broszury spełniają wymagania PRD (ton, sekcje, język polski). | Wysoki    |
|   ✅   | **5.5** | Ostateczna refaktoryzacja i linting kodu.                                                                        | Średni    |

---

## 📋 Dodatkowe zadania

### Dokumentacja

| Status | Zadanie                     | Priorytet |
| :----: | :-------------------------- | :-------- |
|   ✅   | Aktualizacja README.md      | Wysoki    |
|   ⏳   | Utworzenie dokumentacji API | Średni    |
|   ⏳   | Przewodnik użytkownika      | Średni    |
|   ⏳   | Przykłady użycia            | Średni    |

### Testy

| Status | Zadanie               | Priorytet |
| :----: | :-------------------- | :-------- |
|   ⏳   | Testy jednostkowe     | Wysoki    |
|   ⏳   | Testy integracyjne    | Wysoki    |
|   ⏳   | Testy wydajności      | Średni    |
|   ⏳   | Testy jakości wyjścia | Wysoki    |

### Optymalizacja

| Status | Zadanie                       | Priorytet |
| :----: | :---------------------------- | :-------- |
|   ⏳   | Optymalizacja promptów OpenAI | Średni    |
|   ⏳   | Cache'owanie wyników          | Niski     |
|   ⏳   | Obsługa większych stron       | Średni    |

---

## 🎯 Następne kroki

1. **Priorytet 1**: Dokończenie Fazy 2 (CLI)
2. **Priorytet 2**: Implementacja Fazy 3 (Web Scraping)
3. **Priorytet 3**: Integracja z OpenAI API (Faza 4)
4. **Priorytet 4**: Testowanie i optymalizacja (Faza 5)

---

**Legenda statusów:**

- ✅ Ukończone
- 🔄 W trakcie
- ⏳ Oczekujące
- ❌ Zablokowane
