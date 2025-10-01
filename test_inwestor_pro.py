#!/usr/bin/env python3
"""
Testy jednostkowe i integracyjne dla aplikacji Inwestor Pro.

Autor: Inwestor Pro Team
Wersja: 1.0.0
"""

import os
import sys
import unittest
from datetime import datetime
from io import StringIO
from unittest.mock import patch

# Dodaj ścieżkę do modułu głównego
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from inwestor_pro import (  # noqa: E402
    clean_and_extract_text,
    combine_content_from_pages,
    fetch_html,
    fetch_subpage_content,
    find_subpage_links,
    generate_brochure,
    get_system_prompt,
    is_valid_url,
    load_api_key,
    main,
    save_markdown_file,
)


class TestURLValidation(unittest.TestCase):
    """Testy dla funkcji walidacji URL."""

    def test_valid_https_url(self):
        """Test prawidłowych URL HTTPS."""
        valid_urls = [
            "https://example.com",
            "https://www.example.com",
            "https://subdomain.example.com",
            "https://example.com/path",
            "https://example.com/path/to/page",
            "https://example.com/path?param=value",
            "https://example.com/path#fragment",
        ]

        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_valid_url(url), f"URL {url} powinien być prawidłowy")

    def test_valid_http_url(self):
        """Test prawidłowych URL HTTP."""
        valid_urls = [
            "http://example.com",
            "http://www.example.com",
            "http://localhost",
            "http://127.0.0.1",
            "http://192.168.1.1",
        ]

        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_valid_url(url), f"URL {url} powinien być prawidłowy")

    def test_invalid_urls(self):
        """Test nieprawidłowych URL."""
        invalid_urls = [
            "example.com",  # brak protokołu
            "ftp://example.com",  # nieprawidłowy protokół
            "https://",  # brak domeny
            "http://",  # brak domeny
            "not-a-url",  # nie jest URL
            "",  # pusty string
            "https://",  # tylko protokół
            "https://.com",  # nieprawidłowa domena
        ]

        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(
                    is_valid_url(url), f"URL {url} powinien być nieprawidłowy"
                )

    def test_case_insensitive(self):
        """Test czy walidacja jest case-insensitive."""
        urls = [
            "HTTPS://EXAMPLE.COM",
            "Http://Example.Com",
            "https://EXAMPLE.COM",
        ]

        for url in urls:
            with self.subTest(url=url):
                self.assertTrue(
                    is_valid_url(url),
                    f"URL {url} powinien być prawidłowy (case-insensitive)",
                )

    def test_localhost_and_ip(self):
        """Test URL z localhost i adresami IP."""
        valid_urls = [
            "http://localhost",
            "http://localhost:8080",
            "https://localhost",
            "http://127.0.0.1",
            "http://192.168.1.1:3000",
            "https://10.0.0.1",
        ]

        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_valid_url(url), f"URL {url} powinien być prawidłowy")


class TestCLI(unittest.TestCase):
    """Testy dla interfejsu CLI."""

    def setUp(self):
        """Przygotowanie do testów."""
        self.original_argv = sys.argv
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr

    def tearDown(self):
        """Czyszczenie po testach."""
        sys.argv = self.original_argv
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

    def test_help_message(self):
        """Test wyświetlania pomocy."""
        sys.argv = ["inwestor_pro.py", "--help"]

        with StringIO() as captured_output:
            sys.stdout = captured_output
            try:
                main()
            except SystemExit:
                pass  # argparse wywołuje sys.exit() dla --help

            output = captured_output.getvalue()
            self.assertIn("Inwestor Pro", output)
            self.assertIn("--url", output)
            self.assertIn("--output", output)
            self.assertIn("--verbose", output)

    def test_valid_url_argument(self):
        """Test z prawidłowym URL."""
        sys.argv = ["inwestor_pro.py", "--url", "https://example.com"]

        with StringIO() as captured_output:
            sys.stdout = captured_output
            test_result = main()
            self.assertEqual(test_result, 0)

            output = captured_output.getvalue()
            self.assertIn("Inwestor Pro v1.0.0", output)
            self.assertIn("Analizuje strone: https://example.com", output)

    def test_invalid_url_argument(self):
        """Test z nieprawidłowym URL."""
        sys.argv = ["inwestor_pro.py", "--url", "invalid-url"]

        with patch("sys.exit") as mock_exit:
            with StringIO() as captured_output:
                sys.stderr = captured_output
                try:
                    main()
                except SystemExit:
                    pass
                mock_exit.assert_called_with(1)

                output = captured_output.getvalue()
                self.assertIn("Blad: Podany URL nie jest prawidlowy.", output)

    def test_missing_url_argument(self):
        """Test bez argumentu URL."""
        sys.argv = ["inwestor_pro.py"]

        with patch("sys.exit") as mock_exit:
            with StringIO() as captured_output:
                sys.stderr = captured_output
                try:
                    main()
                except SystemExit:
                    pass  # argparse wywołuje sys.exit() dla błędów argumentów
                # argparse może zwrócić różne kody błędów w zależności od wersji
                self.assertTrue(mock_exit.called, "sys.exit() powinien być wywołany")

    def test_verbose_flag(self):
        """Test flagi verbose."""
        sys.argv = ["inwestor_pro.py", "--url", "https://example.com", "--verbose"]

        with StringIO() as captured_output:
            sys.stdout = captured_output
            test_result = main()
            self.assertEqual(test_result, 0)

            output = captured_output.getvalue()
            self.assertIn("Inwestor Pro v1.0.0", output)

    def test_output_argument(self):
        """Test argumentu output."""
        sys.argv = [
            "inwestor_pro.py",
            "--url",
            "https://example.com",
            "--output",
            "test.md",
        ]

        with StringIO() as captured_output:
            sys.stdout = captured_output
            test_result = main()
            self.assertEqual(test_result, 0)

            output = captured_output.getvalue()
            self.assertIn("Inwestor Pro v1.0.0", output)


class TestWebScraping(unittest.TestCase):
    """Testy dla funkcji web scrapingu."""

    def test_fetch_html_valid_url(self):
        """Test pobierania HTML z prawidłowego URL."""
        # Test z prostą stroną
        html = fetch_html("https://example.com")
        self.assertIsNotNone(html, "Powinien pobrać HTML")
        self.assertIn("html", html.lower(), "Powinien zawierać tagi HTML")

    def test_fetch_html_invalid_url(self):
        """Test pobierania HTML z nieprawidłowego URL."""
        html = fetch_html("https://nieistniejacastrona12345.com")
        self.assertIsNone(html, "Powinien zwrócić None dla nieprawidłowego URL")

    def test_fetch_html_timeout(self):
        """Test timeout podczas pobierania."""
        html = fetch_html("https://httpbin.org/delay/35", timeout=1)
        self.assertIsNone(html, "Powinien zwrócić None przy timeout")

    def test_clean_and_extract_text_basic(self):
        """Test podstawowego czyszczenia HTML."""
        html = "<html><body><h1>Test</h1><p>To jest test.</p></body></html>"
        text = clean_and_extract_text(html)
        self.assertIn("Test", text)
        self.assertIn("To jest test", text)
        self.assertNotIn("<h1>", text)
        self.assertNotIn("<p>", text)

    def test_clean_and_extract_text_remove_scripts(self):
        """Test usuwania skryptów i stylów."""
        html = """
        <html>
        <head><style>body { color: red; }</style></head>
        <body>
        <h1>Test</h1>
        <script>alert('test');</script>
        <p>Treść</p>
        </body>
        </html>
        """
        text = clean_and_extract_text(html)
        self.assertIn("Test", text)
        self.assertIn("Treść", text)
        self.assertNotIn("alert", text)
        self.assertNotIn("color: red", text)

    def test_clean_and_extract_text_remove_ads(self):
        """Test usuwania reklam."""
        html = """
        <html>
        <body>
        <h1>Test</h1>
        <div class="advertisement">Reklama</div>
        <div id="banner">Banner</div>
        <p>Treść</p>
        </body>
        </html>
        """
        text = clean_and_extract_text(html)
        self.assertIn("Test", text)
        self.assertIn("Treść", text)
        self.assertNotIn("Reklama", text)
        self.assertNotIn("Banner", text)

    def test_clean_and_extract_text_external_links(self):
        """Test usuwania linków zewnętrznych."""
        html = """
        <html>
        <body>
        <h1>Test</h1>
        <a href="https://example.com/page">Link wewnętrzny</a>
        <a href="https://external.com/page">Link zewnętrzny</a>
        <p>Treść</p>
        </body>
        </html>
        """
        text = clean_and_extract_text(html, "https://example.com")
        self.assertIn("Test", text)
        self.assertIn("Treść", text)
        self.assertNotIn("Link zewnętrzny", text)

    def test_clean_and_extract_text_empty(self):
        """Test z pustym HTML."""
        text = clean_and_extract_text("")
        self.assertEqual(text, "")

    def test_clean_and_extract_text_none(self):
        """Test z None."""
        text = clean_and_extract_text(None)
        self.assertEqual(text, "")


class TestAIFunctions(unittest.TestCase):
    """Testy dla funkcji AI."""

    def test_get_system_prompt(self):
        """Test generowania system prompt."""
        prompt = get_system_prompt()
        self.assertIsInstance(prompt, str)
        self.assertIn("analizy inwestycyjnej", prompt)
        self.assertIn("broszury", prompt)
        self.assertIn("Tytuł Broszury", prompt)
        self.assertIn("Podsumowanie Inwestycyjne", prompt)

    def test_load_api_key_missing(self):
        """Test ładowania klucza API gdy nie ma pliku .env."""
        with patch.dict(os.environ, {}, clear=True):
            with patch("inwestor_pro.load_dotenv"):
                api_key = load_api_key()
                self.assertIsNone(api_key)

    def test_load_api_key_invalid(self):
        """Test ładowania klucza API gdy jest pusty."""
        with patch.dict(os.environ, {"OPENAI_API_KEY": ""}, clear=True):
            with patch("inwestor_pro.load_dotenv"):
                api_key = load_api_key()
                self.assertIsNone(api_key)

    def test_load_api_key_valid(self):
        """Test ładowania klucza API gdy jest prawidłowy."""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key-123"}, clear=True):
            with patch("inwestor_pro.load_dotenv"):
                api_key = load_api_key()
                self.assertEqual(api_key, "test-key-123")

    @patch("openai.OpenAI")
    def test_generate_brochure_success(self, mock_openai):
        """Test pomyślnego generowania broszury."""
        # Mock odpowiedzi API
        mock_response = unittest.mock.MagicMock()
        mock_response.choices[0].message.content = (
            "# Test Broszura\n\nTo jest testowa broszura."
        )
        mock_client = unittest.mock.MagicMock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client

        result = generate_brochure("Test content", "test-key")

        self.assertIsNotNone(result)
        self.assertIn("Test Broszura", result)
        mock_openai.assert_called_once_with(api_key="test-key")

    def test_generate_brochure_empty_content(self):
        """Test generowania broszury z pustą treścią."""
        result = generate_brochure("", "test-key")
        self.assertIsNone(result)

    def test_generate_brochure_no_api_key(self):
        """Test generowania broszury bez klucza API."""
        result = generate_brochure("Test content", "")
        self.assertIsNone(result)

    @patch("openai.OpenAI")
    def test_generate_brochure_auth_error(self, mock_openai):
        """Test obsługi błędu autoryzacji."""
        mock_client = unittest.mock.MagicMock()
        mock_client.chat.completions.create.side_effect = Exception(
            "Authentication failed"
        )
        mock_openai.return_value = mock_client

        result = generate_brochure("Test content", "invalid-key")
        self.assertIsNone(result)

    @patch("openai.OpenAI")
    def test_generate_brochure_rate_limit_error(self, mock_openai):
        """Test obsługi błędu limitu zapytań."""
        mock_client = unittest.mock.MagicMock()
        mock_client.chat.completions.create.side_effect = Exception(
            "Rate limit exceeded"
        )
        mock_openai.return_value = mock_client

        result = generate_brochure("Test content", "test-key")
        self.assertIsNone(result)


class TestSubpageFunctionality(unittest.TestCase):
    """Testy dla funkcjonalności podstron."""

    def test_find_subpage_links_basic(self):
        """Test podstawowego wyszukiwania linków do podstron."""
        html = """
        <html>
        <body>
        <h1>Główna strona</h1>
        <a href="/about">O nas</a>
        <a href="/contact">Kontakt</a>
        <a href="https://external.com">Zewnętrzny link</a>
        <a href="#section">Kotwica</a>
        </body>
        </html>
        """

        links = find_subpage_links(html, "https://example.com")

        self.assertIn("https://example.com/about", links)
        self.assertIn("https://example.com/contact", links)
        self.assertNotIn("https://external.com", links)
        self.assertNotIn("https://example.com#section", links)

    def test_find_subpage_links_max_limit(self):
        """Test ograniczenia liczby linków."""
        html = """
        <html><body>
        <a href="/page1">Strona 1</a>
        <a href="/page2">Strona 2</a>
        <a href="/page3">Strona 3</a>
        <a href="/page4">Strona 4</a>
        <a href="/page5">Strona 5</a>
        <a href="/page6">Strona 6</a>
        </body></html>
        """

        links = find_subpage_links(html, "https://example.com", max_links=3)
        self.assertEqual(len(links), 3)

    def test_find_subpage_links_external_domain(self):
        """Test ignorowania linków zewnętrznych."""
        html = """
        <html><body>
        <a href="/internal">Wewnętrzny</a>
        <a href="https://other.com/page">Zewnętrzny</a>
        <a href="https://example.com/page">Tej samej domeny</a>
        </body></html>
        """

        links = find_subpage_links(html, "https://example.com")

        self.assertIn("https://example.com/internal", links)
        self.assertIn("https://example.com/page", links)
        self.assertNotIn("https://other.com/page", links)

    def test_find_subpage_links_file_extensions(self):
        """Test ignorowania plików z rozszerzeniami."""
        html = """
        <html><body>
        <a href="/page">Strona</a>
        <a href="/document.pdf">PDF</a>
        <a href="/image.jpg">Obraz</a>
        <a href="/style.css">CSS</a>
        </body></html>
        """

        links = find_subpage_links(html, "https://example.com")

        self.assertIn("https://example.com/page", links)
        self.assertNotIn("https://example.com/document.pdf", links)
        self.assertNotIn("https://example.com/image.jpg", links)
        self.assertNotIn("https://example.com/style.css", links)

    def test_find_subpage_links_empty_html(self):
        """Test z pustym HTML."""
        links = find_subpage_links("", "https://example.com")
        self.assertEqual(links, [])

    def test_find_subpage_links_no_base_url(self):
        """Test bez bazowego URL."""
        html = "<html><body><a href='/page'>Strona</a></body></html>"
        links = find_subpage_links(html, "")
        self.assertEqual(links, [])

    @patch("requests.get")
    def test_fetch_subpage_content_success(self, mock_get):
        """Test pomyślnego pobierania zawartości podstrony."""
        mock_response = unittest.mock.MagicMock()
        mock_response.headers = {"content-type": "text/html"}
        mock_response.text = "<html><body>Test content</body></html>"
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_subpage_content("https://example.com/page")

        self.assertIsNotNone(result)
        self.assertIn("Test content", result)
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_fetch_subpage_content_non_html(self, mock_get):
        """Test pobierania nie-HTML zawartości."""
        mock_response = unittest.mock.MagicMock()
        mock_response.headers = {"content-type": "application/json"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_subpage_content("https://example.com/api")

        self.assertIsNone(result)

    @patch("requests.get")
    def test_fetch_subpage_content_error(self, mock_get):
        """Test obsługi błędu podczas pobierania."""
        mock_get.side_effect = Exception("Connection error")

        result = fetch_subpage_content("https://example.com/page")

        self.assertIsNone(result)

    def test_combine_content_from_pages_basic(self):
        """Test podstawowego łączenia treści."""
        main_content = "Treść głównej strony"
        subpages_content = ["Treść podstrony 1", "Treść podstrony 2"]
        base_url = "https://example.com"

        result = combine_content_from_pages(main_content, subpages_content, base_url)

        self.assertIn("=== TREŚĆ GŁÓWNEJ STRONY (https://example.com) ===", result)
        self.assertIn("Treść głównej strony", result)
        self.assertIn("=== TREŚĆ PODSTRONY 1 ===", result)
        self.assertIn("Treść podstrony 1", result)
        self.assertIn("=== TREŚĆ PODSTRONY 2 ===", result)
        self.assertIn("Treść podstrony 2", result)

    def test_combine_content_from_pages_empty_subpages(self):
        """Test łączenia z pustymi podstronami."""
        main_content = "Treść głównej strony"
        subpages_content = ["", "Treść podstrony 2"]
        base_url = "https://example.com"

        result = combine_content_from_pages(main_content, subpages_content, base_url)

        self.assertIn("=== TREŚĆ GŁÓWNEJ STRONY (https://example.com) ===", result)
        self.assertIn("Treść głównej strony", result)
        self.assertNotIn("=== TREŚĆ PODSTRONY 1 ===", result)
        self.assertIn("=== TREŚĆ PODSTRONY 2 ===", result)
        self.assertIn("Treść podstrony 2", result)

    def test_combine_content_from_pages_no_subpages(self):
        """Test łączenia bez podstron."""
        main_content = "Treść głównej strony"
        subpages_content = []
        base_url = "https://example.com"

        result = combine_content_from_pages(main_content, subpages_content, base_url)

        self.assertIn("=== TREŚĆ GŁÓWNEJ STRONY (https://example.com) ===", result)
        self.assertIn("Treść głównej strony", result)
        self.assertNotIn("=== TREŚĆ PODSTRONY", result)


class TestFileOperations(unittest.TestCase):
    """Testy dla operacji na plikach."""

    def setUp(self):
        """Przygotowanie przed każdym testem."""
        # Usuń katalog wyniki jeśli istnieje
        import shutil

        if os.path.exists("wyniki"):
            shutil.rmtree("wyniki")

    def tearDown(self):
        """Czyszczenie po testach."""
        # Usuń katalog wyniki po testach
        import shutil

        if os.path.exists("wyniki"):
            shutil.rmtree("wyniki")

    def test_save_markdown_file_success(self):
        """Test pomyślnego zapisywania pliku."""
        content = "# Test Broszura\n\nTo jest testowa broszura."
        result = save_markdown_file("test_broszura", content)

        self.assertTrue(result, "Plik powinien zostać zapisany pomyślnie")

        # Sprawdź czy katalog został utworzony
        today = datetime.now().strftime("%Y-%m-%d")
        expected_dir = f"wyniki/{today}"
        self.assertTrue(
            os.path.exists(expected_dir), "Katalog powinien zostać utworzony"
        )

        # Sprawdź czy plik został utworzony
        expected_file = f"{expected_dir}/test_broszura.md"
        self.assertTrue(os.path.exists(expected_file), "Plik powinien zostać utworzony")

        # Sprawdź zawartość pliku
        with open(expected_file, "r", encoding="utf-8") as f:
            file_content = f.read()
        self.assertEqual(file_content, content, "Zawartość pliku powinna być poprawna")

    def test_save_markdown_file_with_extension(self):
        """Test zapisywania pliku z rozszerzeniem .md."""
        content = "# Test Broszura\n\nTo jest testowa broszura."
        result = save_markdown_file("test_broszura.md", content)

        self.assertTrue(result, "Plik powinien zostać zapisany pomyślnie")

        # Sprawdź czy plik został utworzony z poprawną nazwą
        today = datetime.now().strftime("%Y-%m-%d")
        expected_file = f"wyniki/{today}/test_broszura.md"
        self.assertTrue(os.path.exists(expected_file), "Plik powinien zostać utworzony")

    def test_save_markdown_file_empty_content(self):
        """Test zapisywania pliku z pustą zawartością."""
        result = save_markdown_file("empty_file", "")

        self.assertTrue(result, "Plik powinien zostać zapisany pomyślnie")

        # Sprawdź czy plik został utworzony
        today = datetime.now().strftime("%Y-%m-%d")
        expected_file = f"wyniki/{today}/empty_file.md"
        self.assertTrue(os.path.exists(expected_file), "Plik powinien zostać utworzony")

        # Sprawdź że plik jest pusty
        with open(expected_file, "r", encoding="utf-8") as f:
            file_content = f.read()
        self.assertEqual(file_content, "", "Plik powinien być pusty")

    @patch("pathlib.Path.mkdir")
    def test_save_markdown_file_directory_error(self, mock_mkdir):
        """Test obsługi błędu tworzenia katalogu."""
        mock_mkdir.side_effect = OSError("Permission denied")

        content = "# Test Broszura\n\nTo jest testowa broszura."
        result = save_markdown_file("test_broszura", content)

        self.assertFalse(result, "Funkcja powinna zwrócić False przy błędzie")

    @patch("builtins.open", side_effect=IOError("Disk full"))
    def test_save_markdown_file_write_error(self, mock_open):
        """Test obsługi błędu zapisywania pliku."""
        content = "# Test Broszura\n\nTo jest testowa broszura."
        result = save_markdown_file("test_broszura", content)

        self.assertFalse(result, "Funkcja powinna zwrócić False przy błędzie zapisu")


class TestIntegration(unittest.TestCase):
    """Testy integracyjne."""

    def test_import_modules(self):
        """Test czy wszystkie wymagane moduły można zaimportować."""
        try:
            import bs4  # noqa: F401
            import dotenv  # noqa: F401
            import openai  # noqa: F401
            import requests  # noqa: F401
        except ImportError as e:
            self.fail(f"Nie można zaimportować wymaganego modułu: {e}")

    def test_module_structure(self):
        """Test struktury modułu głównego."""
        from inwestor_pro import (  # noqa: F401
            clean_and_extract_text,
            combine_content_from_pages,
            fetch_html,
            fetch_subpage_content,
            find_subpage_links,
            generate_brochure,
            get_system_prompt,
            is_valid_url,
            load_api_key,
            main,
        )

        self.assertTrue(callable(main), "Funkcja main powinna być wywoływalna")
        self.assertTrue(
            callable(is_valid_url), "Funkcja is_valid_url powinna być wywoływalna"
        )
        self.assertTrue(
            callable(fetch_html), "Funkcja fetch_html powinna być wywoływalna"
        )
        self.assertTrue(
            callable(clean_and_extract_text),
            "Funkcja clean_and_extract_text powinna być wywoływalna",
        )
        self.assertTrue(
            callable(generate_brochure),
            "Funkcja generate_brochure powinna być wywoływalna",
        )
        self.assertTrue(
            callable(get_system_prompt),
            "Funkcja get_system_prompt powinna być wywoływalna",
        )
        self.assertTrue(
            callable(load_api_key), "Funkcja load_api_key powinna być wywoływalna"
        )


def run_tests():
    """Uruchom wszystkie testy."""
    # Konfiguracja testów
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Dodaj testy
    suite.addTests(loader.loadTestsFromTestCase(TestURLValidation))
    suite.addTests(loader.loadTestsFromTestCase(TestCLI))
    suite.addTests(loader.loadTestsFromTestCase(TestWebScraping))
    suite.addTests(loader.loadTestsFromTestCase(TestAIFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestSubpageFunctionality))
    suite.addTests(loader.loadTestsFromTestCase(TestFileOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))

    # Uruchom testy
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result


if __name__ == "__main__":
    print("Uruchamianie testow dla Inwestor Pro...")
    print("=" * 50)

    result = run_tests()

    print("=" * 50)
    if result.wasSuccessful():
        print("Wszystkie testy przeszly pomyslnie!")
        exit_code = 0
    else:
        print(f"{len(result.failures)} testow nie powiodlo sie")
        print(f"{len(result.errors)} testow zakonczylo sie bledem")
        exit_code = 1

    print("\nStatystyki:")
    print(f"   Uruchomione: {result.testsRun}")
    print(f"   Niepowodzenia: {len(result.failures)}")
    print(f"   Bledy: {len(result.errors)}")
    print(f"   Sukces: {result.testsRun - len(result.failures) - len(result.errors)}")

    sys.exit(exit_code)
