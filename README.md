# Student Management System

A menu-driven Python command-line application for managing a small set of student records and calculating basic academic statistics. This is a Python fundamentals project; it does not currently use a database or expose a REST API.

## Implemented features

- Add a student with name, section, roll number, and marks
- List all student records
- Search for a student by roll number
- Update a student's marks
- Delete a student by roll number
- Calculate the average marks
- Display the highest-scoring student
- Validate marks to the range 0–100

## Technology

Python 3 · Python standard library · Command-line interface

## Run locally

Clone the repository:

```bash
git clone https://github.com/kirubanandhan016/python-student-management-system.git
cd python-student-management-system
```

Run the actual entry-point file:

```bash
python main.py
```

On Windows, the Python launcher can also be used:

```powershell
py main.py
```

## Data storage

Student records are stored in the in-memory `students` list in `main.py`. Data is not persisted when the program exits.

## Example record structure

```python
{
    "name": "Arun",
    "roll_number": "101",
    "section": "B.E. ECE",
    "marks": 85.0
}
```

## Concepts demonstrated

- Python lists and dictionaries
- Functions, loops, and conditional statements
- CRUD-style operations on in-memory records
- Basic validation and aggregation
- Finding minimum/maximum values in a collection

## Known limitations

- Non-numeric mark input can raise a `ValueError`; robust input recovery is a useful next improvement.
- Records are not persisted to disk or a database.
- Automated tests are not currently included.

## Future improvements

- Add consistent handling for invalid numeric input.
- Persist records using SQLite.
- Add Pytest coverage for CRUD operations and validation.
- Build a FastAPI version with Pydantic schemas and database persistence.

## Author

**Kirubanandhan V**

- GitHub: [@kirubanandhan016](https://github.com/kirubanandhan016)
- Portfolio: [kirubanandhan016.github.io](https://kirubanandhan016.github.io/)
