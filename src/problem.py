from __future__ import annotations

import copy

from book import Book
from library import Library


class Problem:
    """Problem to solve"""

    def __init__(self, name: str, filename: Path):

        self.name = name
        self.filename = filename

        with open(self.filename, "r", encoding="utf-8") as file:

            self.raw = file.read()

        self.parse(self.raw)

    def parse(self, raw: str):
        """Parses the raw representation of the problem

        Parameters
        ----------
        raw : str
            text representation of the problem
        """

        rows = raw.split("\n")

        def get_row_data(row: str):
            temp = []
            for info in row.split(" "):
                if info == "":
                    g = 2
                temp.append(int(info))
            return temp

        # Parse header
        header = get_row_data(rows[0])
        self.num_books = header[0]  # B = Number of different books
        self.num_libraries = header[1]  # L = Number of libraries
        self.num_days = header[2]  # D =Number of days available
        self.book_scores = get_row_data(rows[1])  # Scores for each Book

        # Parse sections
        self.libraries = []
        for j in range(2, len(rows) - 2, 2):
            if rows[j] == "":
                # For some reason the different data files are inconsistent and may contain 1 OR 2 empty lines at the end of the file (?)
                # Just skip empty lines..
                continue
            library_info = get_row_data(rows[j])  # Info about library
            books_in_library = get_row_data(
                rows[j + 1]
            )  # List of book ids in this library

            books = [Book(book, self.book_scores[book]) for book in books_in_library]
            Library_num_books = library_info[0]  # unused
            signup_process = library_info[1]
            books_per_day = library_info[2]
            library_id = int(j / 2) - 1
            self.libraries.append(
                Library(library_id, books, signup_process, books_per_day)
            )
