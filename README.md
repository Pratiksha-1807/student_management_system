# student_management_system
A simple Python command-line program that demonstrates object-oriented programming concepts — abstraction, inheritance, encapsulation, and properties — through a student record system.
--------------------------------------------
# code structure

| Class / Function | Purpose |
|---|---|
| `Student` (ABC) | Abstract base class defining shared attributes (`name`, `rollno`) and an abstract `display_info()` method |
| `SchoolStudent` | Concrete subclass for school-level students |
| `CollegeStudent` | Concrete subclass for college-level students |
| `create_school_student()` | Prompts user input and returns a `SchoolStudent` instance |
| `create_college_student()` | Prompts user input and returns a `CollegeStudent` instance |
| `main()` | Collects input for both student types and prints all records |
--------------------------------------------
# What it does

The program lets you enter records for two types of students, School Students and College Students, and then prints a formatted summary of all entered records.

[School Student]
name:
roll number:
grade:
section:

[College Student]
name:
roll number:
year:
branch:
Both are subclasses of an abstract Student base class, which enforces that every student type implements its own display_info() method.
