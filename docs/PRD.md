# Dokument Wymagań Produktu (PRD)

## 1. Nazwa Produktu i Wersja

**Nazwa:** Inwestor Pro (Wersja 1.0 - MVP)
**Właściciel Produktu:** Artur Kud (kudzik@outlook.com)
**Data:** 2025-10-01

---

## 2. Cel i Uzasadnienie Biznesowe (Goal & Rationale)

### 2.1. Problem

Analitycy inwestycyjni spędzają zbyt dużo czasu na ręcznym przeglądaniu stron internetowych spółek i projektów, aby wyłuskać kluczowe informacje, co spowalnia proces decyzyjny i tworzenie materiałów sprzedażowych.

### 2.2. Cel

Stworzenie narzędzia w Pythonie, które **automatyzuje ekstrakcję, analizę i podsumowanie kluczowych danych** z pojedynczej strony internetowej w celu błyskawicznego wygenerowania **perswazyjnej broszury inwestycyjnej** w języku polskim.

### 2.3. Użytkownik Docelowy (Persona)

**Analityk Inwestycyjny:** Osoba potrzebująca szybkich, zwięzłych i ukierunkowanych na sprzedaż podsumowań, które można wykorzystać jako bazę do komunikacji z klientami i partnerami.

---

## 3. Zakres Produktu (Scope)

Aplikacja będzie narzędziem działającym w linii komend (CLI), które na podstawie pojedynczego adresu URL generuje plik broszury w formacie Markdown, korzystając z API OpenAI.

---

## 4. Funkcjonalności i Wymagania (Features & Requirements)

### 4.1. Wymagania Funkcjonalne (FR - Functional Requirements)

| ID        | Funkcjonalność                       | Opis                                                                                                                                                    | Priorytet |
| :-------- | :----------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------- |
| **FR1.0** | **Pobieranie Danych (Web Scraping)** | Aplikacja musi pobrać zawartość **podstawowej, pojedynczej strony** podanej przez użytkownika.                                                          | Wysoki    |
| **FR1.1** | **Obsługa Linków Zewnętrznych**      | Aplikacja **nie może** analizować ani pobierać treści z podstron, których URL nie należy do głównej domeny lub wygląda na linki partnerskie/zewnętrzne. | Średni    |
| **FR2.0** | **Interfejs CLI**                    | Użytkownik musi mieć możliwość uruchomienia aplikacji z wiersza poleceń, podając wymagany URL (np. `python inwestor_pro.py --url https://przyklad.pl`). | Wysoki    |
| **FR3.0** | **Analiza z OpenAI**                 | Aplikacja musi przesłać pobrany tekst do API OpenAI (model **`gpt-4-mini`**).                                                                           | Wysoki    |
| **FR3.1** | **Wymagania Językowe**               | Otrzymany wynik musi być **w języku polskim**.                                                                                                          | Wysoki    |
| **FR3.2** | **Ton i Styl**                       | Generowana broszura musi mieć **ton profesjonalny, analityczny i perswazyjny**, ukierunkowany na zachęcanie do inwestycji/zakupu.                       | Wysoki    |
| **FR4.0** | **Generowanie Broszury**             | Aplikacja musi zapisać wynik analizy w **pliku Markdown (.md)**.                                                                                        | Wysoki    |

### 4.2. Struktura Generowanej Broszury

Wygenerowany plik Markdown musi zawierać następujące **11 szczegółowych sekcji**, bazujące na analizie strony:

- **Tytuł Broszury:** Profesjonalny, atrakcyjny tytuł zachęcający do inwestycji
- **Executive Summary:** Zwięzłe podsumowanie (4-5 zdań) z kluczowymi informacjami inwestycyjnymi
- **Analiza Rynku i Pozycji:** Analiza pozycji firmy/projektu na rynku
- **Propozycje Wartości:** Wypunktowane kluczowe korzyści i przewagi konkurencyjne
- **Kluczowe Metryki i Dane:** Najważniejsze dane finansowe, statystyki, osiągnięcia
- **Analiza Podstron:** Podsumowanie kluczowych informacji z przeanalizowanych podstron
- **Model Biznesowy:** Opis sposobu generowania przychodów i strategii rozwoju
- **Zespół i Kompetencje:** Informacje o zespole, doświadczeniu i kompetencjach
- **Ryzyka i Wyzwania:** 3-4 potencjalne ryzyka z oceną ich wpływu
- **Perspektywy Rozwoju:** Plany rozwoju, cele strategiczne i potencjał wzrostu
- **Rekomendacja Inwestycyjna:** Końcowa rekomendacja z uzasadnieniem

---

## 5. Wymagania Techniczne (Technical Requirements)

### 5.1. Stos Technologiczny (Tech Stack)

- **Język Programowania:** Python
- **Pobieranie Danych:** Biblioteki `requests` (do pobierania HTML) i `BeautifulSoup` (do parowania HTML).
- **Analiza:** Oficjalna biblioteka `openai` dla Pythona.
- **Interfejs:** Biblioteka `argparse` lub podobna do obsługi CLI.

### 5.2. Wdrożenie i Środowisko

- **Zarządzanie Zależnościami:** Użycie pliku `requirements.txt`.
- **Bezpieczeństwo Kluczy:** API Key OpenAI oraz ewentualne inne klucze muszą być przechowywane w **pliku środowiskowym `.env`** i ładowane za pomocą biblioteki `python-dotenv`.
- **Skalowalność:** Aplikacja jest przeznaczona do analizy **pojedynczych, podanych stron**; nie ma wymagań dotyczących wysokiej skalowalności, kolejek zadań (jak Celery) ani obsługi dużego ruchu.

### 5.3. Wymagania Ograniczające (Constraints)

- **Brak Captcha/JS:** Aplikacja nie musi obsługiwać dynamicznie ładowanych stron (JavaScript, SPA), ani mechanizmów Captcha. Ograniczenie to oznacza, że może nie działać poprawnie na wszystkich nowoczesnych stronach.
- **Zakres URL:** Analiza jest ograniczona do treści znalezionych w obrębie pierwszego, podanego URL.

---

## 6. Wymagania Dotyczące Sukcesu (Success Metrics)

| Metryka               | Cel                                                                                                                                          |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| **Czas Analizy**      | Poniżej 30 sekund od uruchomienia do wygenerowania pliku `.md`.                                                                              |
| **Trafność Sekcji**   | 90% generowanych broszur ma poprawne i kompletne sekcje (Ryzyka, Podsumowanie Inwestycyjne, Propozycje Wartości) zgodnie z treścią źródłową. |
| **Gotowość Językowa** | 100% wyników jest płynne i profesjonalne w języku polskim.                                                                                   |

---

## 7. Wymagania Implementacyjne (Implementation Notes)

- **Ekstrakcja Tekstu:** Konieczne jest **oczyszczenie** pobranego tekstu za pomocą `BeautifulSoup` z elementów nawigacyjnych, stopki, reklam i innych nieistotnych dla inwestycji tagów HTML (np. `nav`, `footer`, `script`, `style`).
- **Prompt Engineering:** Kluczowy jest **precyzyjny prompt** dla modelu `gpt-4-mini`, który:
  - Wymusza ton sprzedażowy/perswazyjny.
  - Jasno definiuje strukturę wyjściową w Markdown.
  - Instruuje model, aby skupił się na kluczowych danych inwestycyjnych.
