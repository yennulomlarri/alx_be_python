# oop/library_system.py

class Book:
    """Base class for all books."""
    def __init__(self, title, author):
        """Initializes a Book instance with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the Book."""
        # This provides a default representation for the base Book class.
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """A class representing an electronic book, inheriting from Book."""
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance.
        Calls the base class constructor and initializes the file_size attribute.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """A class representing a physical book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        """

        Initializes a PrintBook instance.
        Calls the base class constructor and initializes the page_count attribute.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class representing a library, which is composed of a collection of books.
    This demonstrates composition.
    """
    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book in the library."""
        print("Books in the library:")
        for book in self.books:
            # Polymorphism in action: Python calls the correct __str__ method
            # for each object (Book, EBook, or PrintBook).
            print(book)