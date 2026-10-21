
import json


def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


students = load_students()


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def calculate_average(scores):
    return sum(scores) / len(scores)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_valid_score(subject):
    while True:
        try:
            score = float(input(f"Enter {subject} score (0-100): "))

            if 0 <= score <= 100:
                return score

            print("Invalid score! Enter a score from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def add_student():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    if not student_id or not name:
        print("Student ID and name cannot be empty.")
        return

    for student in students:
        if student["id"] == student_id:
            print("This student ID already exists.")
            return

    scores = [
        get_valid_score("Python"),
        get_valid_score("Math"),
        get_valid_score("Database")
    ]

    student = {
        "id": student_id,
        "name": name,
        "scores": scores,
        "average": calculate_average(scores)
    }

    students.append(student)
    save_students()

    print(f"Student {name} registered successfully!")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {calculate_grade(student['average'])}")


def display_students():
    if not students:
        print("No students registered yet.")
        return

    print("\n===== All Students =====")

    for student in students:
        average = student["average"]

        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Average: {average:.2f} | "
            f"Grade: {calculate_grade(average)}"
        )


def search_student():
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            average = student["average"]

            print("\n===== Student Found =====")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Scores:", student["scores"])
            print(f"Average: {average:.2f}")
            print(f"Grade: {calculate_grade(average)}")
            return

    print("Student not found.")


def show_top_student():
    if not students:
        print("No students registered yet.")
        return

    top = max(students, key=lambda student: student["average"])

    print("\n===== Top Student =====")
    print("Name:", top["name"])
    print("ID:", top["id"])
    print(f"Average: {top['average']:.2f}")
    print(f"Grade: {calculate_grade(top['average'])}")


while True:
    print("\n===== Student Grade Management =====")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student")
    print("4. Show top student")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        show_top_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Choose 1-5.")
