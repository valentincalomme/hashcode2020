from __future__ import annotations

import copy


class Library:
    """Library object

    A library is represented by:
        - the set of books in the library
        - the time in days it takes to sign the library up for scanning
        - the number of books that can be scanned each day from the library once the library is signed up
    """

    def __init__(
        self, library_id: int, books: List[Book], sign_up_time: int, books_per_day: int
    ):

        self.library_id = library_id
        self.books = sorted(books, key=lambda x: x.book_score, reverse=True)
        self.sign_up_time = sign_up_time
        self.books_per_day = books_per_day

        self.books_to_scan = []

    def potential(
        self, time: int, deadline: int, scanned_books: Set[Book] = set()
    ) -> int:
        """Calculates the potential of the library

        The potential is defined as the upper bound of points the library can add to a solution.
        It depends on the time, the deadline, and the books that were previously scanned.
        """

        days_left = deadline - time - self.sign_up_time

        books_worth_scanning = list(set(self.books).difference(scanned_books))
        books_worth_scanning = sorted(
            books_worth_scanning, key=lambda x: x.book_score, reverse=True
        )
        books_worth_scanning = books_worth_scanning[: days_left * self.books_per_day]

        return sum([book.book_score for book in books_worth_scanning])
