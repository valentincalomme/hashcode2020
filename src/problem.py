from __future__ import annotations


class Problem:
    """Problem to solve"""

    def __init__(self, name: str, filename: Path):

        self.name = name
        self.filename = filename

        with open(self.filename, "r", encoding="utf-8") as file:

            self.raw = file.read()

        self.parse()

    def parse(self, raw: str):
        """Parses the raw representation of the problem

        Parameters
        ----------
        raw : str
            text representation of the problem
        """

        raise NotImplementedError


class Book:
    def __init__(self, book_id: int, book_score: int):

        self.book_id = book_id
        self.book_score = book_score

    def __hash__(self):

        return hash((self.book_id, self.book_score))


class Library:
    def __init__(
        self, library_id: int, books: List[Book], sign_up_time: int, books_per_day: int
    ):

        self.library_id = library_id
        self.books = sorted(books, key=lambda x: x.book_score, reverse=True)
        self.sign_up_time = sign_up_time
        self.books_per_day = books_per_day


class Time:
    def __init__(self, days: int):

        self.days = days
        self.current_day = 0
