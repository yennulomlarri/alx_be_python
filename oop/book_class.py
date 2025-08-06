class Book:
    """
    A class to represent a book with title, author, and year.
    Implements special methods for object initialization, deletion, and representation.
    """
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with a title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns an informal, user-friendly string representation of the book.
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official, developer-friendly string representation
        that can be used to recreate the object.
        Format: "Book('title', 'author', year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"