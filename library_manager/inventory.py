import json
from pathlib import Path
from library_manager.book import Book

# Create a folder 'data' to store JSON file if it doesn't exist
DATA_FOLDER = Path("data")
DATA_FOLDER.mkdir(exist_ok=True)

# Path to the JSON file that stores books
CATALOG_FILE = DATA_FOLDER / "catalog.json"

class LibraryInventory:
    def __init__(self):
        # List to store all Book objects
        self.books = []
        # Load books from JSON file if it exists
        self.load_from_file()

    def add_book(self, book):
        # Add a new book to the library
        self.books.append(book)
        self.save_to_file()  # Save changes to JSON

    def search_by_isbn(self, isbn):
        # Search a book by its ISBN
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def search_by_title(self, title):
        # Search books containing the title (case-insensitive)
        return [b for b in self.books if title.lower() in b.title.lower()]

    def display_all(self):
        # Print all books in the library
        for b in self.books:
            print(b)

    def save_to_file(self):
        # Save all books to JSON file
        data = [b.to_dict() for b in self.books]
        with open(CATALOG_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        # Load books from JSON file
        try:
            if CATALOG_FILE.exists():
                with open(CATALOG_FILE, "r") as f:
                    data = json.load(f)
                    # Recreate Book objects from dictionaries
                    self.books = [Book(**d) for d in data]
        except Exception as e:
            # Handle any error during loading
            print("Error loading catalog:", e)
            self.books = []
