# Project 3 — Student Record Manager

## Client Background

A coaching institute currently manages student information using a simple console application.

The application works well during the day. Staff members can register students, update information, search records, and generate reports.

However, every time the application is closed, all student information is lost. Staff members are forced to enter the same records again the next day.

As the institute continues to grow, this process has become slow, repetitive, and frustrating.

The institute wants a more practical solution that remembers student information between sessions while remaining simple enough for office staff to use.

You have been hired to develop this application.

---

# Project Objective

Develop a console-based Student Record Manager that allows the institute to organize and manage student information efficiently.

The application should allow staff members to perform common operations on student records while ensuring that information remains available whenever the application is used again.

The application should continue running until the user chooses to exit.

---

# Functional Requirements

Your application should allow users to perform the following operations.

### 1. Register Student

Allow staff members to register a new student.

Each student record should contain information such as:

- Roll Number
- Name
- Age
- Course
- Marks

---

### 2. View All Students

Display every registered student.

The information should be presented in a clear and readable format.

---

### 3. Search Student

Allow staff members to search for a student.

You may decide the search criteria.

Examples include:

- Roll Number
- Name
- Course

---

### 4. Update Student Information

Allow staff members to modify an existing student's information.

The application should clearly indicate whether the update was successful.

---

### 5. Delete Student

Allow staff members to remove a student record.

The application should confirm the deletion before removing the record.

---

### 6. Student Performance Report

Generate a report displaying useful academic information such as:

- Total Students
- Average Marks
- Highest Marks
- Lowest Marks
- Grade Distribution

You may include additional statistics if you believe they would help the client.

---

### 7. Exit Application

Allow users to safely close the application.

---

# Client Requirements

The client has provided the following expectations.

### Permanent Student Records

Student information should remain available even after the application has been closed.

Staff members should not need to register the same students every day.

---

### Automatic Record Management

The client expects the application to remember all changes.

Whenever student information is added, updated, or removed, the records should remain consistent.

---

### Reliable Operation

Unexpected situations should not cause the application to stop working.

If something goes wrong, the application should clearly explain the problem and continue operating whenever possible.

---

### Organized Information

Student information should always be displayed in a consistent and readable format.

Office staff should be able to quickly locate the information they need.

---

### Future Growth

The institute expects the number of students to increase over time.

Design your application so it can continue managing larger numbers of student records without requiring major changes.

---

# Technical Expectations

Before writing your application, think carefully about questions such as:

- How should student records be organized?
- How will each student be uniquely identified?
- How should records be stored so they remain available later?
- How should the application recover if saved information cannot be accessed?
- How can repeated operations be simplified?

Spend time designing your solution before writing code.

---

# Development Guidelines

While developing your application:

- Build and test one feature at a time.
- Keep your code organized.
- Write meaningful variable and function names.
- Display clear instructions for every operation.
- Organize student information neatly.
- Make the application easy for non-technical users to operate.

Remember:

Applications become valuable when users can trust them to remember their information.

---

# Deliverables

Your final submission should include:

- A complete menu-driven console application.
- Student registration and management features.
- Search, update, and delete functionality.
- Academic reports.
- Reliable record management.
- Clear user interaction.
- Well-organized and readable code.
