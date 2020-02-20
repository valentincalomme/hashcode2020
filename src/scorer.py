from __future__ import annotations

from book import Book
from problem import Library


class Scorer:
    """Implements the scoring system"""

    def score(self, problem: Problem, solution: Solution) -> int:
        """Scores a solution given a problem

        Parameters
        ----------
        problem : Problem
            Problem to solve
        solution : Solution
            Solution to the problem

        Returns
        -------
        int
            Score as a positive integer
        """

        # Build a list of books to scan withing D days
        num_days_elapsed = 0
        library_offset = 0
        scanlist = [
            [] for i in range(problem.num_days)
        ]  # List of books to be scanned on each day
        while num_days_elapsed < problem.num_days and library_offset < len(
            solution.libraries
        ):
            library: Library = solution.libraries[library_offset]
            library_offset += 1

            # Library signup
            num_days_elapsed += library.sign_up_time
            if num_days_elapsed > problem.num_days:
                break

            # Scan books for this library
            book_scan_days_elapsed = 0
            for book_scan_offset in range(0, len(library.books), library.books_per_day):
                scan_days_offset = num_days_elapsed + book_scan_days_elapsed
                book_scan_days_elapsed += 1
                if scan_days_offset >= problem.num_days:
                    break
                scanlist[scan_days_offset] += library.books[
                    book_scan_offset : book_scan_offset + library.books_per_day
                ]

        # Sum score in scan list (ignoring duplicates)
        score = 0
        scanned = []
        for day in scanlist:
            book: Book
            for book in day:
                if book.book_id not in scanned:
                    scanned.append(book.book_id)
                    score += book.book_score

        return score
