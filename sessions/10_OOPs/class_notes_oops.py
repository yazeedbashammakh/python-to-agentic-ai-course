# Scope of Variables in Python
# Exception Handling in Python

# OOps Objects Oriented Programming
# What is an object?
# Purpose: To structure the codebase.  
# Variables: 
# Functions: 

# Object: Combination of variables and functions.

# LMS: Student, Teacher, Non-teaching Staff, 

# Student: Age, Address, Name, Roll No, Marks, Grade
# Functionalities of Students: Register, is_passed, grade

# Teacher: Age, Address, Name, Employee ID, Subject, Salary


# class in python: Blueprint of an object. 
# Rohan is a student object. Mohan another student object.

# Objects: 
# 1. Information, attributes, properties.   --> Variables 
# 2. Functionalities: --> Functions, Methods. 


# class --> blueprint , design, template, structure of an object.


class Student:
    def __init__(self, name, age, address, marks=86):  
        self.name = name
        self.age = age
        self.address = address
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"address: {self.address}")
        print(f"marks: {self.marks}")

    def is_pass(self):
        return self.marks > 40

    def update_marks(self, additional_marks):
        self.marks = self.marks + additional_marks

    def grade(self):
        pass


rohan = Student("Rohan", 21, "XYZ", 76)
mohan = Student("Mohan", 22, "XYZ", 56)
chandu = Student("Chandu", 23, "XYZ", 67)

rohan.display()     # Call a method of the class display(rohan)
mohan.display()
chandu.display()

rohan.is_pass()
rohan.update_marks(10)
rohan.display()

# print(rohan.name)


# Encapsulation: Information + Functionalities together.



# User: Age, Address, Name
# Functionalities: 
    # display 
    # login
    # logout

# Student: (User Information) + Roll No, Marks, Grade
# Teacher: (User Information) + Employee ID, Subject, Salary

# DRY coding: Donot repeat yourself. 


class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"address: {self.address}")


class Student1(User): # --> Student class is an extension of User Class. Child Class.
    def __init__(self, name, age, address, roll_no, marks):
        super().__init__(name, age, address)
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        super().display()
        print(f"roll_no: {self.roll_no}")
        print(f"marks: {self.marks}")


class Teacher(User):
    def __init__(self, name, age, address, salary, subject):
        super().__init__(name, age, address)
        self.salary = salary
        self.subject = subject


rohan = Student1("Rohan", 21, "XYZ", 51, 76)
rohan.display()


# tacher1 = Teacher()


# Inheritance : variable, functions 




