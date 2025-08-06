#!/usr/bin/env python3
"""
This module defines a library system with Book, EBook, PrintBook, and Library classes.
"""

class Book:
    """Base class for a book with a title and an author."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """A derived class for an electronic book with a file size."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """A derived class for a printed book with a page count."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """A class to manage a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book object to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book in the library."""
        for book in self.books:
            print(book)