
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    # Display book details
    def book_details(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Borrowed")

        print("-" * 30)

    # Borrowing a book
    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully!")
        else:
            print("Sorry, this book is already borrowed.")

    # Returning a book
    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully!")
        else:
            print("This book has not been borrowed.")


# Creating book objects
books = [
    Book(101, "Python Crash Course", "Eric Matthes"),
    Book(102, "Effective Java", "Joshua Bloch"),
    Book(103, "Clean Code", "Robert C. Martin")
]


# Display all books
def display_all_books():
    if not books:
        print("No books available in this library.")
        return

    print("\nAll Books:")
    for book in books:
        book.book_details()


# Search book by ID
def search_by_id(book_id):
    for book in books:
        if book.book_id == book_id:
            book.book_details()
            return book

    print("Book not found!")
    return None


# Search book by title
def search_by_title(title):
    for book in books:
        if book.title.lower() == title.lower():
            book.book_details()
            return book

    print("Book not found!")
    return None


# Main program
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Display all books")
        print("2. Search book by ID")
        print("3. Search book by title")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_books()

        elif choice == "2":
            try:
                book_id = int(input("Enter book ID: "))
                search_by_id(book_id)
            except ValueError:
                print("Please enter a valid numeric book ID.")

        elif choice == "3":
            title = input("Enter book title: ")
            search_by_title(title)

        elif choice == "4":
            try:
                book_id = int(input("Enter book ID to borrow: "))
                book = search_by_id(book_id)

                if book is not None:
                    book.borrow_book()

            except ValueError:
                print("Please enter a valid numeric book ID.")

        elif choice == "5":
            try:
                book_id = int(input("Enter book ID to return: "))
                book = search_by_id(book_id)

                if book is not None:
                    book.return_book()

            except ValueError:
                print("Please enter a valid numeric book ID.")

        elif choice == "6":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 6.")


# Run the program
if __name__ == "__main__":
    main()
