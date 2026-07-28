# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_menu():
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """Prompt for name, ID, and scores, then save the student record."""
    name = input("Student name: ")

    id_input = input("Student ID: ")
    try:
        student_id = int(id_input)
    except ValueError:
        print("Error: Student ID must be a whole number.")
        return

    count_input = input("How many scores? ")
    try:
        count = int(count_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if count <= 0:
        print("Error: Number of scores must be positive.")
        return

    scores = []
    for i in range(1, count + 1):
        score_input = input(f"Enter score {i}: ")
        try:
            score = float(score_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            return
        scores.append(score)

    students.append({"name": name, "id": student_id, "scores": scores})
    print(f'Student "{name}" added successfully.')


def calculate_student_average(student):
    """Return the average score for a single student, rounded to 2 places."""
    total = 0
    for score in student["scores"]:
        total += score
    return round(total / len(student["scores"]), 2)


def format_score(score):
    """Display whole-number scores without a trailing .0."""
    if score == int(score):
        return str(int(score))
    return str(score)


def display_all_students(students):
    """Print a formatted table of every student's name, ID, scores, average."""
    if not students:
        print("No students have been added yet.")
        return

    # Widths adapt to content so long score lists don't overlap other columns.
    name_width = max(15, max((len(s["name"]) for s in students), default=0) + 2)
    scores_width = max(
        15,
        max(
            (len(", ".join(format_score(sc) for sc in s["scores"])) for s in students),
            default=0,
        )
        + 2,
    )
    line_width = name_width + 12 + scores_width + 10

    print("-" * line_width)
    print(f"{'Name':<{name_width}}{'ID':<12}{'Scores':<{scores_width}}{'Average':<10}")
    print("-" * line_width)
    for student in students:
        scores_str = ", ".join(format_score(sc) for sc in student["scores"])
        average = calculate_student_average(student)
        print(
            f"{student['name']:<{name_width}}{student['id']:<12}"
            f"{scores_str:<{scores_width}}{average:<10}"
        )
    print("-" * line_width)


def find_student_by_id(students, student_id):
    """Return the student dict matching student_id, or None if not found."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def show_student_average(students):
    """Ask for a student ID and display their average score."""
    id_input = input("Enter student ID: ")
    try:
        student_id = int(id_input)
    except ValueError:
        print("Error: Please enter a valid whole number ID.")
        return

    student = find_student_by_id(students, student_id)
    if student is None:
        print("Error: No student found with that ID.")
        return

    average = calculate_student_average(student)
    print(f"{student['name']}'s average score: {average}")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            show_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a number between 1 and 4.")

        print()


if __name__ == "__main__":
    main()