class Book:
    """
    Represents a single book in the bookstore.
    """

    def __init__(self, book_id, title, author, category, price, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.price = price
        self.quantity = quantity

    def display(self):
        """Display book information."""

        print("-" * 50)
        print(f"Book ID  : {self.book_id}")
        print(f"Title    : {self.title}")
        print(f"Author   : {self.author}")
        print(f"Category : {self.category}")
        print(f"Price    : ₹{self.price}")
        print(f"Quantity : {self.quantity}")

    def to_dictionary(self):
        """
        Convert Book object into a dictionary.
        """

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity,
        }
