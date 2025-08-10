import csv

FILE = "students.csv"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, roll, marks])
    print("Student added successfully!\n")

def view_students():
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            print("\nName\tRoll\tMarks")
            print("-"*25)
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("No records found.\n")

def search_student():
    roll = input("Enter roll number to search: ")
    found = False
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == roll:
                print("Student Found:", row)
                found = True
                break
    if not found:
        print("Student not found.\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    rows = []
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[1] != roll]
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Student deleted successfully!\n")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice.\n")