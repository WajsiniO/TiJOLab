# src/library_repository.py

from abc import ABC, abstractmethod

class LibraryRepository(ABC):
    """
    Abstrakcyjny interfejs definiujący operacje na repozytorium książek.
    """
    @abstractmethod
    def add_book(self, title: str, author: str, year: int):
        """Dodaje książkę do repozytorium."""
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        """Usuwa książkę z repozytorium na podstawie tytułu."""
        pass

    @abstractmethod
    def get_all_books(self) -> list:
        """Zwraca listę wszystkich książek."""
        pass