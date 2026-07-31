# Project 5 — Inventory Management System

## Client Background

A retail company currently manages its inventory using a collection of small console applications developed over time.

While these applications were useful in the beginning, they have become increasingly difficult to maintain as the business has grown.

The company now manages hundreds of products across multiple categories. New product types are introduced regularly, inventory changes throughout the day, and employees frequently need to search, update, and review product information.

The management wants a single application that is reliable, organized, and capable of supporting future business growth without requiring major redesigns.

You have been hired to develop this application.

---

# Project Objective

Develop a console-based Inventory Management System that allows employees to efficiently manage product information, inventory levels, and stock reports.

The application should simplify daily inventory operations while remaining flexible enough to support future product categories and additional business requirements.

The application should continue running until the user chooses to exit.

---

# Functional Requirements

Your application should allow users to perform the following operations.

### 1. Register Products

Allow employees to add new products to the inventory.

Each product should contain information such as:

- Product ID
- Product Name
- Category
- Brand
- Purchase Price
- Selling Price
- Quantity Available

You may include additional information if required.

---

### 2. View Products

Display all products currently available in the inventory.

Present the information in a clear and organized format.

---

### 3. Search Products

Allow employees to search for products.

You may decide the search criteria.

Examples include:

- Product ID
- Product Name
- Category
- Brand

---

### 4. Update Product Information

Allow employees to modify existing product information.

The application should clearly indicate whether the update was successful.

---

### 5. Remove Products

Allow employees to permanently remove products from the inventory.

Confirm the operation before deleting any product.

---

### 6. Manage Stock

Allow employees to:

- Increase stock
- Reduce stock

The application should ensure that inventory information remains accurate.

---

### 7. Inventory Reports

Generate useful reports such as:

- Total Products
- Total Inventory Value
- Products with Low Stock
- Out-of-Stock Products
- Products by Category

You may include additional reports if you believe they would benefit the client.

---

### 8. Exit Application

Allow users to safely close the application.

---

# Client Requirements

The client has provided the following expectations.

### Organized Product Management

The company sells different types of products.

Although these products may contain different information, the application should manage them in a consistent and organized manner.

The company expects new product categories to be added in the future without requiring major changes to the existing application.

---

### Reliable Inventory Records

Inventory information must always remain accurate.

Employees should be able to trust that product quantities and stock information correctly represent the actual inventory.

---

### Permanent Data Storage

Product information should remain available whenever the application is used again.

Employees should not need to recreate inventory records every time the application starts.

---

### Fault-Tolerant Operation

The application should continue operating even when users make mistakes.

Whenever an operation cannot be completed, the application should clearly explain the problem and allow users to continue working.

---

### Scalable Software

The company expects the inventory to continue growing.

Design the application so that future developers can easily understand, maintain, and expand the software.

---

# Technical Expectations

Before writing your application, think carefully about questions such as:

- How should different product types be represented?
- What information is shared by every product?
- What information is unique to certain products?
- How can responsibilities be divided into smaller components?
- How can the application avoid duplicated code?
- How should information be organized so it remains easy to maintain?
- How should inventory information be stored and recovered?
- How can the project remain organized as additional files and features are introduced?

Spend time designing your solution before writing code.

---

# Development Guidelines

While developing your application:

- Plan the overall structure before implementing features.
- Divide the application into manageable components.
- Build and test one feature at a time.
- Use meaningful names throughout the project.
- Keep the user interface clean and consistent.
- Organize your project so another developer can easily understand it.
- Design your application with future improvements in mind.

Remember:

Professional software is not measured only by what it can do today, but also by how easily it can grow tomorrow.

---

# Deliverables

Your final submission should include:

- A complete menu-driven console application.
- Product registration and management features.
- Inventory management functionality.
- Search and reporting features.
- Reliable handling of user interactions.
- Permanent record management.
- Clean, organized, and maintainable project structure.
- Well-documented code.
