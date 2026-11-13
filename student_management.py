# Student management system
# list of student
# Data - Roll no, name, english , maths science
# total marks and percentage.

import pdb
import json
from pathlib import Path

file_must = Path("stud_regi.json")


def load_must():
    """Load Muster Register from the json file."""
    try:
        with file_must.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []   

def save_must(students):
    """Save Student Record to JSON file."""
    with file_must.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)

def add_stud(students):
    try:
        """Add New Student into Muster Register"""
        st_nm = input("Enter Student Name: ")
        st_roll = int(input("Enter Student Roll Number: "))
        st_maths = int(input("Enter Mathematics Marks: "))
        st_science = int(input("Enter Science Marks: "))
        st_english = int(input("Enter English Marks: "))

        # Validation for marks should be between 0 and 100

        if not st_maths in range(1, 101) or not st_science in range(1, 101) or not st_english in range(1, 101):
            print("\nInvalid Input : Marks should be between 1 and 100.")
            return
  
        students.append({
            "stud_name" : st_nm,
            "stud_roll" : st_roll,
            "stud_mm" : st_maths,
            "stud_sm" : st_science,
            "stud_em" : st_english,
        })

        save_must(students)
        print("\nNew student added successfully!")
    except ValueError:
        print("Please enter a valid number.")
        return []
    
def view_must(students):
    print(json.dumps(students, indent=4, ensure_ascii=False))

def attn_stud(students):
    # load_must()
    for student in students:
        print(f"Good Morning {student["stud_name"]}")
        a=input("")
    return[]

def repo_card(students):
    # load_must()
    for student in students:
        # Calculate total marks and percentage
    
        total_marks = (student["stud_mm"] + student["stud_sm"] + student["stud_em"])
        percentage = (total_marks / 300) * 100
        if (student["stud_mm"] < 35 or student["stud_sm"] < 35 or student["stud_em"] < 35):
            result = "Fail"
        elif percentage >= 75:
            result = "Grade A"
        elif percentage >= 60:
            result = "Grade B"
        elif percentage >= 45:
            result = "Grade C"
        else:
            result = "PASS"

        # Printing the student details, total marks, percentage and result

        print("\n================== REPORT CARD ===================")
        print(f"Student Name: {student["stud_name"]}")
        print(f"Roll Number: {student["stud_roll"]}")
        print(f"Mathematics Marks: {student["stud_mm"]}")
        print(f"Science Marks: {student["stud_sm"]}")
        print(f"English Marks: {student["stud_em"]}")
        print(f"Total Marks: {total_marks}")
        print(f"Percentage: {percentage:.2f}%        Result : {result}")
        print("===================================================")
        a=input("")


def main():
    students = load_must()

    while True:
        print("\n-----Student Management System-----")
        print("1. Add Student...")
        print("2. View Muster Register...")
        print("3. Attendance Check...")
        print("4. Report Card...")
        print("5. Exit...")

        choice = input("Choice an option : ").strip()

        try:
            if choice == "1":
                add_stud(students)
            elif choice == "2":
                view_must(students)
            elif choice == "3":
                attn_stud(students)
            elif choice == "4":
                repo_card(students)
            elif choice == "5":
                print("\nOkay! Lets continue with our session..!")
                break
            else:
                print("Invalid choice. Select between 1-5")

        except OSError as error:
            print(f"\nFile operation failed : {error}")

if __name__== "__main__":
    main()    