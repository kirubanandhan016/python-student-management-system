# Student Management System

A lightweight command-line application for managing student records. Add and maintain students, review marks, and quickly identify class performance from a simple interactive menu.

## Features

- Add a student with a name, unique roll number, and marks from 0 to 100.
- View all registered students.
- Search for a student by roll number.
- Update a student's marks.
- Delete a student record.
- Calculate the average marks across registered students.
- Display the highest-scoring student.
- Exit the application at any time from the main menu.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Run

Open a terminal in this directory and run:

```bash
python main.py
```

On some Windows installations, use:

```powershell
py main.py
```

Choose an option from the menu and follow the prompts. Marks must be numeric and between 0 and 100. Roll numbers must be unique.

## Data storage

Records are kept in memory while the program is running. They are cleared when the application exits; persistent storage is not included.
