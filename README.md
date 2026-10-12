# Student Management System

A lightweight command-line application built with Python to manage student records, maintain marks, and analyze class performance through an interactive menu.

## Features

- **Add Student:** Register a student with a name, unique roll number, section/class, and marks.
- **View Students:** Display all registered student records.
- **Search Student:** Find a student using their roll number.
- **Update Marks:** Modify an existing student's marks.
- **Delete Student:** Remove a student record using their roll number.
- **Average Marks:** Calculate the average marks of all registered students.
- **Highest Scorer:** Identify the student with the highest marks.
- **Input Validation:** Restrict marks to the range of 0–100.
- **Interactive Menu:** Navigate through the available operations using simple menu options.

## Technologies Used

- Python 3
- Lists and Dictionaries
- Functions
- Loops and Conditional Statements
- Built-in Functions such as `sum()` and `max()`
- Lambda Functions

## Requirements

- Python 3.8 or newer
- No third-party libraries required

## Project Structure

```text
python-student-management-system/
├── student_management.py
└── README.md
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/python-student-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-student-management-system
   ```

3. Run the application:

   ```bash
   python student_management.py
   ```

   On Windows, you can also use:

   ```powershell
   py student_management.py
   ```

## Usage

After starting the application, select an option from the main menu:

| Option | Operation |
|---|---|
| 1 | Add Student |
| 2 | View All Students |
| 3 | Search Student |
| 4 | Update Marks |
| 5 | Delete Student |
| 6 | Calculate Average Marks |
| 7 | Display Highest Scorer |
| 8 | Exit |

Enter the requested information and follow the on-screen prompts.

## Data Storage

Student records are stored in an in-memory Python list of dictionaries. All records remain available while the application is running. The records are cleared when the application exits because persistent storage has not been implemented.

## Learning Objectives

This project demonstrates practical use of:

- Python data structures
- Function-based program design
- Searching and updating records
- Input handling and validation
- Data aggregation and comparison
- Menu-driven command-line applications

## Future Improvements

- Add permanent data storage using JSON or SQLite.
- Implement exception handling for invalid numeric input.
- Add student grade calculation and report generation.
- Improve search and validation features.
- Add automated tests using `unittest` or `pytest`.

## Author

**Kirubanandhan V.**

GitHub: [@kirubanandhan016](https://github.com/kirubanandhan016)

---

If you find this project useful, feel free to explore the code and suggest improvements.
