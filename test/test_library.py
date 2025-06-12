# tests/test_library.py

import unittest
from unittest.mock import Mock

from src.library import Library
from src.library_repository import LibraryRepository

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock(spec=LibraryRepository)
        self.library = Library(self.mock_repo)

    def test_return_book_calls_add_book_on_repository(self):
        self.library.return_book("Wiedźmin", "Andrzej Sapkowski", 1993)

        self.mock_repo.add_book.assert_called_once_with("Wiedźmin", "Andrzej Sapkowski", 1993)

    def test_borrow_book_calls_remove_book_on_repository(self):
        # Konfigurujemy atrapę, aby metoda remove_book zwróciła True
        self.mock_repo.remove_book.return_value = True

        result = self.library.borrow_book("Lód")

        self.assertTrue(result)
        self.mock_repo.remove_book.assert_called_once_with("Lód")

    def test_list_books_returns_data_from_repository(self):
        expected_books = [
            {'title': 'Solaris', 'author': 'Stanisław Lem', 'year': 1961},
            {'title': 'Niezwyciężony', 'author': 'Stanisław Lem', 'year': 1964}
        ]
        self.mock_repo.get_all_books.return_value = expected_books

        result = self.library.list_books()

        self.mock_repo.get_all_books.assert_called_once()
        self.assertEqual(result, expected_books)

# Umożliwia uruchomienie testów bezpośrednio z tego pliku
if __name__ == '__main__':
    unittest.main()