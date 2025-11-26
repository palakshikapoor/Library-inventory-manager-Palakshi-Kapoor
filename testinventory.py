# tests/testinventory.py

import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library_manager.book import Book
from library_manager.inventory import LibraryInventory

def test_add_and_search():
    # Initialize inventory
    inv = LibraryInventory()
    inv.books = []  # clear existing books for testing

    # Add a test book
    book = Book("Test Book", "Test Author", "9999")
    inv.books.append(book)

    # Search by ISBN
    result = inv.search_by_isbn("9999")
    assert result is not None, "Book not found"
    assert result.title == "Test Book", "Title mismatch"
    assert result.author == "Test Author", "Author mismatch"

def test_issue_return():
    book = Book("Issue Test", "Author", "1111")
    assert book.is_available() is True, "Book should be available initially"
    
    book.issue()
    assert book.is_available() is False, "Book should be issued"
    
    book.return_book()
    assert book.is_available() is True, "Book should be available after return"

if __name__ == "__main__":
    # Run tests manually if needed
    test_add_and_search()
    test_issue_return()
    print("All tests passed!")
