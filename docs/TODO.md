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

### Faza 2: Moduł Interfejsu Linii Komend (CLI) ✅ UKOŃCZONA

| Status | Krok    | Zadanie                                                                                   | Priorytet |
| :----: | :------ | :---------------------------------------------------------------------------------------- | :-------- |
|   ✅   | **2.1** | Zaimplementuj funkcję parsowania argumentów (za pomocą `argparse`).                       | Wysoki    |
|   ✅   | **2.2** | Ustaw obowiązkowy argument `--url` dla adresu strony do analizy.                          | Wysoki    |
|   ✅   | **2.3** | Dodaj walidację, aby upewnić się, że podany argument `--url` jest poprawnym formatem URL. | Średni    |
|   ✅   | **2.4** | Zaimplementuj funkcję ładowania klucza API z pliku `.env`.                                | Wysoki    |

---

### Faza 3: Moduł Pobierania i Czyszczenia Danych (Scraping & Cleaning) ✅ UKOŃCZONA

| Status | Krok    | Zadanie                                                                                                      | Priorytet |
| :----: | :------ | :----------------------------------------------------------------------------------------------------------- | :-------- |
|   ✅   | **3.1** | Zaimplementuj funkcję `fetch_html(url)` używającą **`requests`** do pobrania zawartości strony.              | Wysoki    |
|   ✅   | **3.2** | Zaimplementuj funkcję `clean_and_extract_text(html_content)`.                                                | Wysoki    |
|   ✅   | **3.3** | W funkcji czyszczącej, użyj **`BeautifulSoup`** do:                                                          | Wysoki    |
|        |         | a. Usunięcia skryptów (`<script>`) i stylów (`<style>`).                                                     |           |
|        |         | b. Usunięcia elementów nieistotnych dla treści (np. `<nav>`, `<footer>`, reklamy).                           |           |
|        |         | c. Ekstrakcji czystego, widocznego tekstu.                                                                   |           |
|   ✅   | **3.4** | Zaimplementuj prostą logikę do usuwania linków zewnętrznych/partnerskich, jeśli występują w pobranej treści. | Średni    |
|   ✅   | **3.5** | **NOWE**: Dodaj analizę podstron z automatycznym wykrywaniem linków.                                         | Wysoki    |
|   ✅   | **3.6** | **NOWE**: Zaimplementuj funkcję `analyze_subpages_content()` do analizy treści podstron.                     | Wysoki    |
|   ✅   | **3.7** | **NOWE**: Dodaj wyodrębnianie kluczowych fraz z `extract_key_phrases()`.                                     | Średni    |

---

### Faza 4: Moduł Analizy (OpenAI API Integration) ✅ UKOŃCZONA

| Status | Krok    | Zadanie                                                                                                                           | Priorytet |
| :----: | :------ | :-------------------------------------------------------------------------------------------------------------------------------- | :-------- |
|   ✅   | **4.1** | Zdefiniuj szczegółowy **System Prompt** dla modelu **`gpt-4-mini`**.                                                              | Wysoki    |
|        |         | _Prompt musi zawierać wymagania:_                                                                                                 |           |
|        |         | a. **Ton:** Profesjonalny, analityczny i perswazyjny.                                                                             |           |
|        |         | b. **Struktura:** 11 szczegółowych sekcji (Executive Summary, Analiza Rynku, Model Biznesowy, Zespół, Perspektywy, Rekomendacja). |           |
|        |         | c. **Format Wyjściowy:** Czysty Markdown z nagłówkami ## i ###.                                                                   |           |
|        |         | d. **Język:** Polski biznesowy.                                                                                                   |           |
|   ✅   | **4.2** | Zaimplementuj funkcję `generate_brochure(text_content, api_key)` do wywołania API OpenAI.                                         | Wysoki    |
|   ✅   | **4.3** | Zaimplementuj obsługę błędów API (np. brak klucza, przekroczony limit, błąd serwera).                                             | Wysoki    |
|   ✅   | **4.4** | **NOWE**: Dodaj funkcję `enhance_brochure_formatting()` dla profesjonalnego formatowania.                                         | Wysoki    |

---

### Faza 5: Generowanie Wyniku i Testowanie (Output & Testing) ✅ UKOŃCZONA

| Status | Krok    | Zadanie                                                                                                          | Priorytet |
| :----: | :------ | :--------------------------------------------------------------------------------------------------------------- | :-------- |
|   ✅   | **5.1** | Zaimplementuj funkcję `save_markdown_file(filename, content)`.                                                   | Wysoki    |
|   ✅   | **5.2** | Ustaw logiczne nazewnictwo plików wyjściowych (np. `broszura_[nazwa_domeny].md`).                                | Średni    |
|   ✅   | **5.3** | Stwórz i wykonaj test integracyjny: Uruchom aplikację na przynajmniej **trzech różnych stronach internetowych**. | Wysoki    |
|   ✅   | **5.4** | **Weryfikacja jakości:** Sprawdź, czy wygenerowane broszury spełniają wymagania PRD (ton, sekcje, język polski). | Wysoki    |
|   ✅   | **5.5** | Ostateczna refaktoryzacja i linting kodu.                                                                        | Średni    |
|   ✅   | **5.6** | **NOWE**: Dodaj profesjonalne formatowanie z metadanymi i stopką.                                                | Wysoki    |
|   ✅   | **5.7** | **NOWE**: Zwiększ limit tokenów do 3000 dla lepszej jakości broszur.                                             | Średni    |

---

## 🚀 Ulepszenia v1.0.0 (UKOŃCZONE)

### Profesjonalne Broszury

| Status | Zadanie                                      | Priorytet |
| :----: | :------------------------------------------- | :-------- |
|   ✅   | Rozszerzenie struktury broszury do 11 sekcji | Wysoki    |
|   ✅   | Dodanie Executive Summary                    | Wysoki    |
|   ✅   | Dodanie Analizy Rynku i Pozycji              | Wysoki    |
|   ✅   | Dodanie Modelu Biznesowego                   | Wysoki    |
|   ✅   | Dodanie sekcji Zespół i Kompetencje          | Wysoki    |
|   ✅   | Dodanie Perspektyw Rozwoju                   | Wysoki    |
|   ✅   | Dodanie Rekomendacji Inwestycyjnej           | Wysoki    |

### Analiza Podstron

| Status | Zadanie                              | Priorytet |
| :----: | :----------------------------------- | :-------- |
|   ✅   | Automatyczne wykrywanie podstron     | Wysoki    |
|   ✅   | Pobieranie treści z podstron         | Wysoki    |
|   ✅   | Analiza treści podstron              | Wysoki    |
|   ✅   | Wyodrębnianie kluczowych fraz        | Średni    |
|   ✅   | Dedykowana sekcja "Analiza Podstron" | Wysoki    |

### Profesjonalne Formatowanie

| Status | Zadanie                                    | Priorytet |
| :----: | :----------------------------------------- | :-------- |
|   ✅   | Nagłówek z metadanymi                      | Wysoki    |
|   ✅   | Stopka z informacjami o źródle             | Wysoki    |
|   ✅   | Lepsze formatowanie Markdown               | Wysoki    |
|   ✅   | Zwiększenie limitów tokenów (3000)         | Średni    |
|   ✅   | Naprawienie problemów z kodowaniem Unicode | Wysoki    |

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

1. **Priorytet 1**: ✅ **UKOŃCZONE** - Wszystkie fazy MVP zostały zrealizowane
2. **Priorytet 2**: **Opcjonalne ulepszenia** - Cache'owanie, optymalizacja promptów
3. **Priorytet 3**: **Rozszerzenia** - Obsługa większych stron, dodatkowe formaty wyjściowe
4. **Priorytet 4**: **Monitoring** - Zbieranie metryk użycia i jakości broszur

---

**Legenda statusów:**

- ✅ Ukończone
- 🔄 W trakcie
- ⏳ Oczekujące
- ❌ Zablokowane
