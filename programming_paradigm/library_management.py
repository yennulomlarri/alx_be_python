# library_management.py

class Book:
    """Represents a book with a title, author, and checkout status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book objects."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'.")
                return
        print(f"Sorry, '{title}' is either not in the library or already checked out.")

    def return_book(self, title):
        """Returns a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned '{title}'.")
                return
        print(f"Sorry, '{title}' is not a book that was checked out from here.")

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")