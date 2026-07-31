# Book Store Management System

## Client Background

A local bookstore currently manages its inventory using notebooks and spreadsheets.

As the business has grown, managing books, updating stock, searching products, and calculating sales has become increasingly time-consuming and error-prone.

The owner wants a simple console-based application that helps employees manage the bookstore efficiently while keeping the system organized and easy to maintain.

You have been hired to develop the first version of this application.

---

# Project Objective

Develop a menu-driven console application that allows bookstore employees to manage books, inventory, and sales from a single application.

The application should remain easy to use, reliable, and organized as additional books and features are added in the future.

The application should continue running until the user chooses to exit.

---

# Functional Requirements

Your application should provide the following features.

## 1. Register Book

Employees should be able to register a new book.

Each book should contain information such as:

- Book ID
- Title
- Author
- Category
- Price
- Quantity Available

You may include additional information if required.

---

## 2. View All Books

Display all books currently available in the store.

The information should be presented in a clean and readable format.

---

## 3. Search Book

Allow employees to search for books.

You may decide the search criteria.

Examples include:

- Book ID
- Title
- Author
- Category

---

## 4. Update Book Information

Allow employees to modify existing book information.

The application should clearly indicate whether the update was successful.

---

## 5. Remove Book

Allow employees to permanently remove a book from the inventory.

The application should confirm the operation before deleting any record.

---

## 6. Purchase Book

Allow customers to purchase one or more books.

The application should:

- Verify that the requested quantity is available.
- Reduce the available stock after a successful purchase.
- Display the total purchase amount.
- Inform the user if sufficient stock is unavailable.

---

## 7. Inventory Reports

Generate useful reports such as:

- Total Number of Books
- Total Inventory Value
- Books Running Low on Stock
- Out-of-Stock Books
- Number of Books in Each Category

You may include additional reports if you believe they would help the client.

---

## 8. Exit Application

Allow users to safely close the application.

---

# Client Requirements

The client has provided the following expectations.

## Easy to Use

Employees should be able to use the application without technical knowledge.

Menus and messages should be simple and easy to understand.

---

## Accurate Inventory

Inventory information should always remain accurate.

Book quantities should automatically reflect every successful purchase.

Employees should not be able to sell books that are unavailable.

---

## Permanent Records

Book information should remain available even after the application is closed.

Employees should not have to register every book again each time the application starts.

---

## Reliable Operation

The application should continue operating even if users accidentally enter incorrect information.

Whenever an operation cannot be completed, the application should display a meaningful message and allow the user to continue using the system.

---

## Organized Software

The bookstore expects additional features to be added in future versions.

The application should therefore remain organized, easy to understand, and easy to extend.

Future developers should be able to add new features without rewriting the entire application.

