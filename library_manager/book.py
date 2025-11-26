# Book class represents a single book in the library
class Book:
    def __init__(self, title, author, isbn, status="available"):
        # Initialize book with title, author, ISBN, and status
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue(self):
        # Mark book as issued if it is available
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        # Mark book as available if it was issued
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        # Return True if book is available
        return self.status == "available"

    def to_dict(self):
        # Convert Book object into dictionary for JSON storage
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def __str__(self):
        # String representation of the book
        return f"{self.title} - {self.author} (ISBN: {self.isbn}) [{self.status}]"
