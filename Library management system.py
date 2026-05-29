class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"

        print(f"\nBook ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-" * 40)


class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        # Check duplicate Book ID
        for book in self.books:
            if book.book_id == book_id:
                print("\nBook ID already exists!")
                return

        new_book = Book(book_id, title, author)
        self.books.append(new_book)

        print("\nBook added successfully!")

    # Display All Books
    def display_books(self):
        if not self.books:
            print("\nNo books available in the library.")
            return

        print("\n===== ALL BOOKS =====")
        for book in self.books:
            book.display()

    # Search by Title
    def search_by_title(self):
        title = input("Enter title to search: ").lower()

        found = False

        for book in self.books:
            if title in book.title.lower():
                book.display()
                found = True

        if not found:
            print("\nNo matching books found.")

    # Search by Author
    def search_by_author(self):
        author = input("Enter author name to search: ").lower()

        found = False

        for book in self.books:
            if author in book.author.lower():
                book.display()
                found = True

        if not found:
            print("\nNo matching books found.")

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book.book_id == book_id:

                if book.available:
                    book.available = False
                    print("\nBook issued successfully!")
                else:
                    print("\nBook is already issued!")

                return

        print("\nBook not found!")

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book.book_id == book_id:

                if not book.available:
                    book.available = True
                    print("\nBook returned successfully!")
                else:
                    print("\nThis book was not issued!")

                return

        print("\nBook not found!")

    # Additional Feature 1: Remove Book
    def remove_book(self):
        book_id = input("Enter Book ID to remove: ")

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("\nBook removed successfully!")
                return

        print("\nBook not found!")

    # Additional Feature 2: View Available Books
    def view_available_books(self):
        available_books = [book for book in self.books if book.available]

        if not available_books:
            print("\nNo books are currently available.")
            return

        print("\n===== AVAILABLE BOOKS =====")

        for book in available_books:
            book.display()


# Main Program
def main():
    library = Library()

    while True:
        print("\n")
        print("=" * 45)
        print("     LIBRARY MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Remove Book")
        print("8. View Available Books")
        print("9. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            library.search_by_title()

        elif choice == "4":
            library.search_by_author()

        elif choice == "5":
            library.issue_book()

        elif choice == "6":
            library.return_book()

        elif choice == "7":
            library.remove_book()

        elif choice == "8":
            library.view_available_books()

        elif choice == "9":
            print("\nThank you for using the Library Management System!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()