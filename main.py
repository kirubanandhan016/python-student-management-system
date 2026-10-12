def find_student(students, roll_number):
    for student in students:
        if student["roll_number"] == roll_number:
            return student
    return None


def read_marks(prompt="Marks (0-100): "):
    while True:
        try:
            marks = float(input(prompt))
        except ValueError:
            print("Enter a valid number.")
            continue

        if 0 <= marks <= 100:
            return marks
        print("Marks must be between 0 and 100.")


def add_student(students):
    name = input("Student name: ").strip()
    roll_number = input("Roll number: ").strip()

    if not name or not roll_number:
        print("Name and roll number are required.")
        return
    if find_student(students, roll_number):
        print("A student with that roll number already exists.")
        return

    students.append({
        "name": name,
        "roll_number": roll_number,
        "marks": read_marks(),
    })
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students registered.")
        return

    print("\nRegistered students")
    for student in students:
        print(
            "Name: {name} | Roll number: {roll_number} | Marks: {marks:g}".format(
                **student
            )
        )


def search_student(students):
    roll_number = input("Roll number to search: ").strip()
    student = find_student(students, roll_number)
    if student is None:
        print("Student not found.")
        return

    print(
        "Name: {name} | Roll number: {roll_number} | Marks: {marks:g}".format(
            **student
        )
    )


def update_marks(students):
    roll_number = input("Roll number to update: ").strip()
    student = find_student(students, roll_number)
    if student is None:
        print("Student not found.")
        return

    student["marks"] = read_marks()
    print("Marks updated successfully.")


def delete_student(students):
    roll_number = input("Roll number to delete: ").strip()
    student = find_student(students, roll_number)
    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    print("Student deleted successfully.")


def show_average(students):
    if not students:
        print("No students registered.")
        return

    average = sum(student["marks"] for student in students) / len(students)
    print("Average marks: {:g}".format(average))


def show_highest_scorer(students):
    if not students:
        print("No students registered.")
        return

    highest = max(students, key=lambda student: student["marks"])
    print(
        "Highest scorer: {name} | Roll number: {roll_number} | Marks: {marks:g}".format(
            **highest
        )
    )


def main():
    students = []
    actions = {
        "1": ("Add student", add_student),
        "2": ("View all students", view_students),
        "3": ("Search by roll number", search_student),
        "4": ("Update marks", update_marks),
        "5": ("Delete student", delete_student),
        "6": ("Calculate average marks", show_average),
        "7": ("Display highest scorer", show_highest_scorer),
    }

    while True:
        print("\nStudent Management System")
        for number, (label, _) in actions.items():
            print("{}. {}".format(number, label))
        print("8. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "8":
            print("Goodbye.")
            return
        action = actions.get(choice)
        if action is None:
            print("Invalid option. Choose a number from 1 to 8.")
            continue
        action[1](students)


if __name__ == "__main__":
    main()
