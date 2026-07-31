from models.book import Book
from utils.file_handler import load_json, save_json
from utils.validation import (
    get_integer,
    get_float,
    get_non_empty_string,
    confirm,
)


class BookStore:

    def __init__(self):

        self.filename = "books.json"
        self.books = []

        self.load_books()


    def load_books(self):
        """
        Load all books from the JSON file.
        """

        data = load_json(self.filename)

        self.books = []

        for book_dict in data:
            self.books.append(Book(book_dict))


    def save_books(self):
        """
        Save all books to the JSON file.
        """
    
        data = []
    
        for book in self.books:
            data.append(book.to_dictionary())
    
        save_json(self.filename, data)


    def find_book(self, book_id):
        """
        Find a book using its ID.
        """
    
        for book in self.books:
        
            if book.book_id == book_id:
                return book
    
        return None


    def add_book(self):
        """
        Register a new book.
        """

        print("\n--- Add Book ---")

        book_id = get_integer("Book ID: ")

        if self.find_book(book_id):
            print("Book ID already exists.")
            return

        title = get_non_empty_string("Title: ")
        author = get_non_empty_string("Author: ")
        category = get_non_empty_string("Category: ")

        price = get_float("Price: ₹")
        quantity = get_integer("Quantity: ")

        book = Book(
            book_id,
            title,
            author,
            category,
            price,
            quantity,
        )

        self.books.append(book)

        self.save_books()

        print("\n Book added successfully.")


    def view_books(self):
        """
        Display all books.
        """
    
        print("\n--- Book List ---")
    
        if not self.books:
            print("No books available.")
            return
    
        for book in self.books:
            book.display()
    
    
    def search_book(self):
        """
        Search a book using its ID.
        """
    
        print("\n--- Search Book ---")
    
        book_id = get_integer("Enter Book ID: ")
    
        book = self.find_book(book_id)
    
        if book:
            book.display()
        else:
            print("Book not found.")
    
    
    def update_book(self):
        """
        Update book information.
        """
    
        print("\n--- Update Book ---")
    
        book_id = get_integer("Enter Book ID: ")
    
        book = self.find_book(book_id)
    
        if not book:
            print("Book not found.")
            return
    
        print("\nLeave blank to keep the current value.\n")
    
        title = input(f"Title ({book.title}): ").strip()
        author = input(f"Author ({book.author}): ").strip()
        category = input(f"Category ({book.category}): ").strip()
    
        if title:
            book.title = title
    
        if author:
            book.author = author
    
        if category:
            book.category = category
    
        price = input(f"Price ({book.price}): ").strip()
    
        if price:
            try:
                book.price = float(price)
            except ValueError:
                print("Invalid price. Previous value kept.")
    
        quantity = input(f"Quantity ({book.quantity}): ").strip()
    
        if quantity:
            try:
                book.quantity = int(quantity)
            except ValueError:
                print("Invalid quantity. Previous value kept.")
    
        self.save_books()
    
        print("\n Book updated successfully.")
    
    
    def delete_book(self):
        """
        Delete a book from the inventory.
        """
    
        print("\n--- Delete Book ---")
    
        book_id = get_integer("Enter Book ID: ")
    
        book = self.find_book(book_id)
    
        if not book:
            print("Book not found.")
            return
    
        book.display()
    
        if confirm("Delete this book?"):
            self.books.remove(book)
            self.save_books()
            print("Book deleted successfully.")
        else:
            print("Operation cancelled.")
    
    
    def purchase_book(self):
        """
        Purchase a book.
        """
    
        print("\n--- Purchase Book ---")
    
        book_id = get_integer("Enter Book ID: ")
    
        book = self.find_book(book_id)
    
        if not book:
            print("Book not found.")
            return
    
        print(f"\nAvailable Quantity : {book.quantity}")
    
        quantity = get_integer("Quantity to Purchase: ")
    
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    
        if quantity > book.quantity:
            print("Not enough books in stock.")
            return
    
        total = quantity * book.price
    
        book.quantity -= quantity
    
        self.save_books()
    
        print("\nPurchase Successful")
        print(f"Book : {book.title}")
        print(f"Quantity : {quantity}")
        print(f"Total Bill : ₹{total:.2f}")
    
    
    def inventory_report(self):
        """
        Display inventory statistics.
        """
    
        print("\n--- Inventory Report ---")
    
        total_books = len(self.books)
    
        total_quantity = 0
        total_value = 0
    
        low_stock = []
    
        for book in self.books:
        
            total_quantity += book.quantity
            total_value += book.price * book.quantity
    
            if book.quantity <= 5:
                low_stock.append(book)
    
        print(f"Total Titles          : {total_books}")
        print(f"Total Quantity        : {total_quantity}")
        print(f"Inventory Value       : ₹{total_value:.2f}")
    
        print("\nLow Stock Books")
    
        if not low_stock:
            print("None")
        else:
            for book in low_stock:
                print(f"- {book.title} ({book.quantity} left)")
    
    
    def menu(self):
        """
        Display the main menu.
        """
    
        while True:
        
            print("\n" + "=" * 50)
            print("      BOOK STORE MANAGEMENT SYSTEM")
            print("=" * 50)
    
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Book")
            print("4. Update Book")
            print("5. Delete Book")
            print("6. Purchase Book")
            print("7. Inventory Report")
            print("8. Exit")
    
            choice = get_integer("\nEnter your choice: ")
    
            if choice == 1:
                self.add_book()
    
            elif choice == 2:
                self.view_books()
    
            elif choice == 3:
                self.search_book()
    
            elif choice == 4:
                self.update_book()
    
            elif choice == 5:
                self.delete_book()
    
            elif choice == 6:
                self.purchase_book()
    
            elif choice == 7:
                self.inventory_report()
    
            elif choice == 8:
                print("\nThank you for using Book Store Management System.")
                break
            
            else:
                print("Invalid choice. Please try again.")