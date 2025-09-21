from book import Book

def add_book(library):
    """
    Prompt the user for title, author, and ISBN,
    create a Book object, and add it to the library.
    """
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    new_book = Book(title, author, isbn)
    library.append(new_book)
    print("✅ Book added!\n")

def list_books(library):
    """
    Print all books in the library using __str__.
    """
    if not library:
        print("📚 Library is empty.\n")
    else:
        print("\n📚 Library contains:")
        for book in library:
            print(book)   # uses __str__ in Book
        print()

def find_book(library, query):
    """
    Search for a book by title or author.
    Returns the Book if found, otherwise None.
    """
    for book in library:
        if query.lower() in book.title.lower() or query.lower() in book.author.lower():
            return book
    return None

def main():
    """
    Main program loop for the Library Manager.
    """
    my_library = []  # start with an empty library
    
    while True:
        print("=== Library Manager ===")
        print("1) Add a new book")
        print("2) List all books")
        print("3) Find a book")
        print("4) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_book(my_library)
        elif choice == "2":
            list_books(my_library)
        elif choice == "3":
            query = input("Enter title or author to search: ")
            result = find_book(my_library, query)
            if result:
                print(f"🔎 Found: {result}\n")
            else:
                print("❌ No book found.\n")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")

if __name__ == "__main__":
    main()