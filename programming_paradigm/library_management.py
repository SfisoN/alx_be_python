class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute for availability

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # was already available

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out

    def __str__(self):
        """User-friendly representation of a book."""
        return f"{self.title} by {self.author}"


class Library:
    """Represents a library that stores and manages books."""

    def __init__(self):
        self._books = []  # private list to store Book objects

    def add_book(self, book):
        """Add a new Book object to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # book not found or not available

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # book not found or wasn't checked out

    def list_available_books(self):
        """Print all books that are available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(book)
