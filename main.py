students=[]
def add_student():
    name=input("Enter the student name:")
    section=input("Enter the section and class:")
    roll_number=input("Enter the roll no:")

    for student in students:
        if student["name"]==name:
            print("Already name exist")
            return

        if student["roll_number"]==roll_number:
            print("Roll number exist")
            return

    # Now allocate marks (0 to 100)
    marks=float(input("Enter the marks 0->100: "))
    if marks < 0 or marks > 100:
        print("Marks should be 0 to 100!")
        return

    student={
        "name":name,
        "roll_number":roll_number,
        "section":section,
        "marks":marks
    }

    students.append(student)
    print("Student Added successfully")
    
def view_students():
    if not students:
        print("Not added student")
        return
    print("\n=======STUDENT MANAGEMENT SYSTEM=====")
    for student in students:
        print("Name:",student["name"])
        print("Roll_no:",student["roll_number"])
        print("Section:",student["section"])
        print("Marks:",student["marks"])


def search_student():
    roll_number=input("Enter the roll number:")

    for student in students:
        if student["roll_number"]==roll_number:
            print("Name:",student["name"])
            print("Rollno:",student["roll_number"])
            print("Section:",student["section"])
            print("Marks:",student["marks"])
            return

    print("Student data not found")


def update_marks():
    roll_no=input("Enter the roll number:")

    for student in students:
        if student["roll_number"]==roll_no:
            marks=float(input("Enter the marks:"))

            if marks < 0 or marks > 100:
                print("Mark should be 0 to 100")
                return

            student["marks"]=marks
            print("Marks added successfully")
            return

    print("Student not found!")


def delete_student():
    roll_no=input("Enter the roll number:")

    for student in students:
        if student["roll_number"]==roll_no:
            students.remove(student)
            print("Student deleted successfully")
            return

    print("Student not found!")


def average_marks():
    if not students:
        print("No students registered.")
        return

    total=sum(student["marks"] for student in students)
    average=total/len(students)
    print("Average marks:",average)


def highest_scorer():
    if not students:
        print("No students registered.")
        return

    highest=max(students, key=lambda student: student["marks"])

    print("Highest-scoring student:",highest["name"])
    print("Roll Number:",highest["roll_number"])
    print("Marks:",highest["marks"])


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Calculate Student Average")
    print("7. Display Highest Scorer")
    print("8. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        update_marks()
    elif choice=="5":
        delete_student()
    elif choice=="6":
        average_marks()
    elif choice=="7":
        highest_scorer()
    elif choice=="8":
        print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
