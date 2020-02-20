from __future__ import annotations


class Book:
    def __init__(self, book_id: int, book_score: int):

        self.book_id = book_id
        self.book_score = book_score

    def __hash__(self):

        return hash((self.book_id, self.book_score))
