from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def main():
    # Create a library inventory object
    library = LibraryInventory()

    while True:
        # Display menu
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search by Title")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            # Add a new book
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            library.add_book(Book(title, author, isbn))
            print("Book added!")

        elif choice == "2":
            # Issue a book by ISBN
            isbn = input("ISBN to issue: ")
            book = library.search_by_isbn(isbn)
            if book and book.issue():
                library.save_to_file()
                print("Book issued!")
            else:
                print("Cannot issue book.")

        elif choice == "3":
            # Return a book by ISBN
            isbn = input("ISBN to return: ")
            book = library.search_by_isbn(isbn)
            if book and book.return_book():
                library.save_to_file()
                print("Book returned!")
            else:
                print("Cannot return book.")

        elif choice == "4":
            # Display all books
            library.display_all()

        elif choice == "5":
            # Search books by title
            title = input("Title to search: ")
            results = library.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == "6":
            # Exit program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run main program
if __name__ == "__main__":
    main()
