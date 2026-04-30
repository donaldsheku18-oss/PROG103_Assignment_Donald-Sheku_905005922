# PROG103: Principles of Structured Programming
# Assignment: Student Result Management Terminal System (SRMTS)

# Function 1: Displays the terminal menu (Requirement: Section 5.2)
def show_menu():
    print("=" * 50)
    print("      LIMKOKWING SEMESTER 2 - GRADE RECORDER     ")
    print("=" * 50)
    print("1. INPUT STUDENT MARKS")
    print("2. ACCESS STUDENT REPORTS")
    print("3. Exit")
    return input("Select one of the above: ")

# Grading system ranges
grading_system = [
    (80, 100, "A", 4.00, "Pass with Distinction"),
    (75, 79, "A-", 3.67, "Pass with Distinction"),
    (70, 74, "B+", 3.33, "Pass with Merit"),
    (65, 69, "B", 3.00, "Pass with Merit"),
    (60, 64, "B-", 2.67, "Pass"),
    (55, 59, "C+", 2.33, "Pass"),
    (50, 54, "C", 2.00, "Pass"),
    (45, 49, "C-", 1.67, "Pass"),
    (40, 44, "D", 1.00, "Pass"),
    (0, 39, "F", 0.00, "Fail")
]

def marks_to_grade(marks):
    for low, high, grade, points, desc in grading_system:
        if low <= marks <= high:
            return grade, points, desc
    return "Invalid", 0.00, "Out of Range"

def check_status(avg_points):
    if avg_points >= 2.00:  # C or better
        return "PASS"
    else:
        return "FAIL"

# Variables to store multiple records (Requirement: Section 6)
names = [] 
all_student_records = []

modules = [
    "Computerized Mathematics",
    "Introduction to Multimedia",
    "Introduction to Data Communication",
    "Principles of Software Engineering",
    "Principles of Structured Programming",
    "Introduction to Database"
]

while True:   # Iteration (Requirement: Section 11)
    choice = show_menu()

    if choice == "1":
        while True:
            try:
                student_name = input("\nEnter Student Full Name: ")
                if not student_name.strip():
                    raise ValueError("Name cannot be empty.")
                if not student_name.replace(" ", "").isalpha():
                    raise ValueError("Name can only contain letters and spaces.")
                break
            except ValueError as e:
                print(f"  Error: {e} Please try again.")

        current_records = []

        print(f"Enter marks (0–100) for {student_name}:")
        for sub in modules:
            while True:
                try:
                    mark = float(input(f"  {sub}: "))
                    if 0 <= mark <= 100:
                        grade, points, desc = marks_to_grade(mark)
                        current_records.append((mark, grade, points, desc))
                        break
                    else:
                        print("  Invalid: Mark must be between 0 and 100.")
                except ValueError:
                    print("  Error: Please enter a numeric grade.")
                    
# Save student name and their list of 6 marks
        names.append(student_name)
        all_student_records.append(current_records)
        print(f"\nSuccessfully saved record for {student_name}!")

 # Output: Formatted display of all grades (Requirement: Section 5.3)1
 
    elif choice == "2":
        print("\n" + "X" * 50)
        print("           COMPLETE ACADEMIC REPORT           ")
        print("X" * 50)

        if not names:
            print("No student records available.")
        else:
            for i in range(len(names)):
                print(f"\nSTUDENT: {names[i].upper()}")
                print("-" * 30)

                records = all_student_records[i]
                total_points = 0

                for j in range(len(modules)):
                    mark, grade, points, desc = records[j]
                    print(f"{modules[j]:<30}: {mark:.1f} → {grade} ({desc})")
                    total_points += points

                avg_points = total_points / 6
                status = check_status(avg_points)
                print("-" * 30)
                print(f"SEMESTER GPA: {avg_points:.2f}")
                print(f"FINAL STATUS: {status}")
                print("=" * 50)

    elif choice == "3":
        print("System Closed. Good luck with Semester 2!")
        break
    else:
        print("Invalid choice. Enter 1, 2, or 3.")
