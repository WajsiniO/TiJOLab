# src/in_memory_repository.py

from .library_repository import LibraryRepository

class InMemoryRepository(LibraryRepository):
    """
    Implementacja repozytorium w pamięci, która używa słownika do przechowywania książek.
    """
    def __init__(self):
        self._books = {}

    def add_book(self, title: str, author: str, year: int):
        if title not in self._books:
            self._books[title] = {'author': author, 'year': year}

    def remove_book(self, title: str) -> bool:
        if title in self._books:
            del self._books[title]
            return True
        return False

    def get_all_books(self) -> list:
        return [{'title': title, **data} for title, data in self._books.items()]