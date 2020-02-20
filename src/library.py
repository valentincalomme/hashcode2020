from __future__ import annotations

import copy


class Library:
    def __init__(
        self, library_id: int, books: List[Book], sign_up_time: int, books_per_day: int
    ):

        self.library_id = library_id
        self.books = sorted(books, key=lambda x: x.book_score, reverse=True)
        self.sign_up_time = sign_up_time
        self.books_per_day = books_per_day

        self.books_to_scan = []
        self.sign_up_day = None

    def next_books_to_scan(self, scanned_books: Set[Book]):

        books_worth_scanning = list(set(self.books).difference(scanned_books))

        books_worth_scanning = sorted(
            books_worth_scanning, key=lambda x: x.book_score, reverse=True
        )

        score = sum(books_worth_scanning, key=lambda x: x.book_score)

        return books_worth_scanning[: self.books_per_day], score

    def get_status(self, time: int, deadline: int) -> Tuple[List[Book], List[Book]]:

        scanned = []
        unscanned = copy.copy(self.books)

        num_days = max(min(time, deadline) - self.sign_up_day, 0)

        for book in range(num_days * self.books_per_day):

            if len(unscanned) > 0:

                scanned.append(unscanned.pop(0))

        return scanned, unscanned
