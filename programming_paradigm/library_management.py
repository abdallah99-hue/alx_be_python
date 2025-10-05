# library_management.py

class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to make it available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages books."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return True
                else:
                    print(f"Book '{title}' is already checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return True
                else:
                    print(f"Book '{title}' was not checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            for book_str in available_books:
                print(book_str)
        else:
            print("No books available.")
