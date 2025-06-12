# src/library.py

from .library_repository import LibraryRepository

class Library:
    """
    Główna klasa biblioteki, która zarządza operacjami na książkach
    poprzez wstrzyknięte repozytorium.
    """
    def __init__(self, repository: LibraryRepository):
        self.repository = repository

    def borrow_book(self, title: str) -> bool:
        """Wypożycza książkę, usuwając ją z repozytorium."""
        return self.repository.remove_book(title)

    def return_book(self, title: str, author: str, year: int):
        """Zwraca książkę, dodając ją do repozytorium."""
        self.repository.add_book(title, author, year)

    def list_books(self) -> list:
        """Zwraca listę wszystkich dostępnych książek."""
        return self.repository.get_all_books()