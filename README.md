# 🎓 Student Management System

<p align="center">
  <b>A Menu-Driven Student Record Management Application Built with Python</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Interface-CLI-181717?style=for-the-badge&logo=windows-terminal&logoColor=white" alt="Command Line Interface">
  <img src="https://img.shields.io/badge/Dependencies-None-2EA44F?style=for-the-badge" alt="No Dependencies">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Project Status">
</p>

---

## 📌 About the Project

The **Student Management System** is a lightweight command-line application developed using Python to manage student records and analyze academic performance.

The application provides an interactive menu that allows users to add, view, search, update, and delete student records. It also calculates average marks and identifies the highest-scoring student.

This project demonstrates practical Python programming fundamentals through a simple, structured, and easy-to-use application.

## ✨ Features

| No. | Feature | Description |
|:---:|---|---|
| 1 | ➕ Add Student | Register a student with name, roll number, section/class, and marks |
| 2 | 📋 View Students | Display all registered student records |
| 3 | 🔍 Search Student | Find a student using their roll number |
| 4 | ✏️ Update Marks | Modify an existing student's marks |
| 5 | 🗑️ Delete Student | Remove a student record using their roll number |
| 6 | 📊 Average Marks | Calculate the average marks of all registered students |
| 7 | 🏆 Highest Scorer | Identify the student with the highest marks |
| 8 | 🚪 Exit | Exit the application through the main menu |

### ✅ Validation

- Prevents duplicate student names and roll numbers.
- Accepts marks only within the range of 0 to 100.
- Checks for student records before performing relevant operations.

## 🛠️ Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
</p>

**Programming language:** Python 3

**Concepts used:**
- Variables and data types
- Lists and dictionaries
- Functions and modular programming
- Loops and conditional statements
- User input and output
- Searching and record manipulation
- Input validation
- Built-in functions: `sum()`, `max()`, and `len()`
- Lambda functions

## 📂 Project Structure

```text
python-student-management-system/
│
├── student_management.py
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.8 or newer
- Git installed on your computer
- No third-party Python packages required

### Step 1: Clone the Repository

```bash
git clone https://github.com/kirubanandhan016/python-student-management-system.git
```

### Step 2: Navigate to the Project Folder

```bash
cd python-student-management-system
```

### Step 3: Run the Application

```bash
python student_management.py
```

**Windows users** can also run:

```powershell
py student_management.py
```

> **Note:** If your Python source file is named `main.py`, use `python main.py` or `py main.py` instead.

## 🖥️ Application Menu

When you run the program, the following interactive menu appears:

```text
========================================
       STUDENT MANAGEMENT SYSTEM
========================================

1. Add Student
2. View All Students
3. Search Student
4. Update Marks
5. Delete Student
6. Calculate Student Average
7. Display Highest Scorer
8. Exit

========================================
Enter your choice:
```

Enter an option from `1` to `8` and follow the on-screen instructions.

## 📊 Example

```text
===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student
4. Update Marks
5. Delete Student
6. Calculate Student Average
7. Display Highest Scorer
8. Exit

Enter your choice: 1

Enter the student name: Arun
Enter the section and class: B.E. ECE
Enter the roll no: 101
Enter the marks 0->100: 85

Student Added successfully
```

## 💾 Data Storage

The application stores student records in a Python list containing dictionaries.

Each student record contains:

```python
{
    "name": "Arun",
    "roll_number": "101",
    "section": "B.E. ECE",
    "marks": 85.0
}
```

**Current limitation:** Records are stored only in memory. All student information is lost when the application exits. Permanent data storage is not yet implemented.

## 🎯 Learning Objectives

This project helps develop practical skills in:

- Writing reusable Python functions
- Organizing records with lists and dictionaries
- Implementing CRUD operations (Create, Read, Update, Delete)
- Validating and processing user input
- Performing calculations on collections of data
- Building interactive command-line applications
- Using Git and GitHub for version control and project documentation

## 🚀 Future Improvements

- [ ] Store student records permanently using JSON.
- [ ] Integrate SQLite for database management.
- [ ] Handle invalid numeric input using `try-except`.
- [ ] Add student grades and performance reports.
- [ ] Implement automated tests using `unittest` or `pytest`.
- [ ] Develop a REST API using FastAPI.
- [ ] Add a web interface for managing student records.

## 👨‍💻 Author

**Kirubanandhan V.**

*Python Developer | C/C++ | Problem Solving*

<p>
  📧 <b>Email:</b> <a href="mailto:kirubanandhan016@gmail.com">kirubanandhan016@gmail.com</a>
  <br>
  🐙 <b>GitHub:</b> <a href="https://github.com/kirubanandhan016">@kirubanandhan016</a>
</p>

---

<p align="center">
  <b>⭐ If you find this project useful, consider giving the repository a star!</b>
  <br>
  <sub>Built with Python and a passion for learning.</sub>
</p>
