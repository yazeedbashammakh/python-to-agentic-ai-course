# Project 4 — Library Management Console

## Client Background

A local community library has been using a small console application to manage its daily operations.

Initially, the application worked well because the library had only a few books and members. However, over time the collection has expanded significantly, and the number of daily visitors has increased.

The library now manages hundreds of books and many registered members. As new features have been added, the application has become increasingly difficult to maintain and extend.

The library wants a more organized system that is easier to manage today and can continue growing as new requirements are introduced in the future.

You have been hired to develop this application.

---

# Project Objective

Develop a console-based Library Management System that helps library staff manage books, members, and borrowing activities efficiently.

The application should organize information clearly, simplify daily operations, and provide a foundation that can easily support future improvements.

The application should continue running until the user chooses to exit.

---

# Functional Requirements

Your application should allow users to perform the following operations.

### 1. Register Books

Allow staff members to add new books to the library.

Each book should contain information such as:

- Book ID
- Title
- Author
- Category
- Publication Year
- Available Copies

---

### 2. Register Members

Allow staff members to register new library members.

Each member should contain information such as:

- Member ID
- Name
- Age
- Contact Number

---

### 3. View Records

Allow staff members to display:

- All Books
- All Members

Display information in a clean and organized format.

---

### 4. Search Records

Allow staff members to search for:

- Books
- Members

You may decide the search criteria.

Examples include:

- ID
- Name
- Title
- Author
- Category

---

### 5. Update Records

Allow staff members to update existing information for books or members.

The application should clearly indicate whether the update was successful.

---

### 6. Remove Records

Allow staff members to remove books or members from the system.

Confirm the operation before permanently removing any record.

---

### 7. Borrow Books

Allow members to borrow available books.

The application should update the availability of the selected book.

---

### 8. Return Books

Allow members to return previously borrowed books.

The application should update the availability accordingly.

---

### 9. Library Reports

Generate useful reports such as:

- Total Books
- Total Members
- Borrowed Books
- Available Books
- Most Borrowed Categories

You may include additional reports if you believe they would benefit the client.

---

### 10. Exit Application

Allow users to safely close the application.

---

# Client Requirements

The client has provided the following expectations.

### Organized Information

Books and members should be managed in a structured and consistent manner.

The application should remain easy to understand even as the library continues to grow.

---

### Reliable Operations

Daily activities such as borrowing and returning books should always produce accurate results.

The application should help prevent mistakes that could lead to incorrect library records.

---

### Easy Expansion

The client expects additional features to be added in the future.

The application should be designed in a way that allows new functionality to be introduced without requiring major changes to the existing system.

---

### Clear User Experience

Library staff should always know which operations are available.

Every completed operation should return users to the main menu.

---

### Maintainable Software

The client wants the application to remain organized as it grows.

Future developers should be able to understand and modify the application without difficulty.

---

# Technical Expectations

Before writing your application, think carefully about questions such as:

- What information belongs together?
- Which operations naturally belong with that information?
- How can similar pieces of information be managed consistently?
- How can the application avoid duplicated code?
- How can future features be added with minimal effort?

Spend time designing your solution before writing code.

---

# Development Guidelines

While developing your application:

- Divide the problem into smaller components.
- Build one feature at a time.
- Test every feature thoroughly.
- Use meaningful names throughout your program.
- Keep the user interface clean and consistent.
- Design your application so it remains organized as new features are added.

Remember:

As software grows, good organization becomes just as important as correct functionality.

---

# Deliverables

Your final submission should include:

- A complete menu-driven console application.
- Book management features.
- Member management features.
- Borrow and return functionality.
- Search and reporting features.
- Clean and organized code.
- A user-friendly interface.
