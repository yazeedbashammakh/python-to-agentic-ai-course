from services.bookstore import BookStore


def main():
    """
    Start the Book Store Management System.
    """

    bookstore = BookStore()
    bookstore.menu()


if __name__ == "__main__":
    main()