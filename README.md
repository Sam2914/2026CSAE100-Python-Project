# Student Management System (2026CSAE100 Project)

A menu-driven command-line **Student Management System** developed in Python for the **Computational Thinking and Programming (2026CSAE100)** Collaborative Problem-Solving Project at Bennett University.

## Problem Statement & Objectives
Managing student records manually is error-prone and inefficient. This project provides a lightweight, file-backed Python application to store, retrieve, update, and manage student academic records persistently using a local text file (`students.txt`).

## Key Features
- **Add Student:** Validates unique Student IDs and ensures marks fall strictly between `0` and `100`.
- **View All Students:** Displays all saved records in a clean, formatted table.
- **Search Student:** Retrieves individual student details instantly by Student ID.
- **Update Student:** Allows selective updates to a student's name, course, or marks.
- **Delete Student:** Removes outdated records and updates persistent storage immediately.

## Python Concepts Used
- **Data Structures:** Nested Dictionaries (`records[student_id]`) and Lists
- **File Handling:** Reading and writing comma-separated records to `students.txt`
- **Functions & Modular Design:** Separate functions for each CRUD operation and input validation
- **Control Flow & Exception Handling:** `while` loops, conditionals, and `try-except` blocks (`FileNotFoundError`, `ValueError`)

## How to Run
1. Ensure Python 3 is installed on your system.
2. Clone or download this repository.
3. Run the program from your terminal:
   ```bash
   python main.py
