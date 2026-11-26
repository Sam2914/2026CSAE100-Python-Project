FILE_NAME = "students.txt"



def load_records():
    records = {}
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                if len(parts) == 4:
                    student_id = parts[0]
                    records[student_id] = {
                        "name": parts[1],
                        "course": parts[2],
                        "marks": float(parts[3])
                    }
        file.close()
    except FileNotFoundError:
        # If the file does not exist yet, start with empty records
        pass
    return records



def save_records(records):
    file = open(FILE_NAME, "w")
    for student_id, details in records.items():
        line = f"{student_id},{details['name']},{details['course']},{details['marks']}\n"
        file.write(line)
    file.close()



def get_valid_marks():
    while True:
        marks_input = input("Enter Marks (0-100): ").strip()
        try:
            marks = float(marks_input)
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value for marks.")



def add_student(records):
    print("\n--- ADD NEW STUDENT ---")
    student_id = input("Enter Student ID (e.g., S101): ").strip().upper()

    if student_id == "":
        print("Error: Student ID cannot be empty.")
        return

    if student_id in records:
        print(f"Error: Student ID '{student_id}' already exists!")
        return

    name = input("Enter Student Name: ").strip().replace(",", " ")
    course = input("Enter Course (e.g., CSE, ECE): ").strip().upper().replace(",", " ")
    marks = get_valid_marks()

    records[student_id] = {
        "name": name,
        "course": course,
        "marks": marks
    }

    save_records(records)
    print(f"Success: Record for '{name}' (ID: {student_id}) added!")



def view_students(records):
    print("\n--- ALL STUDENT RECORDS ---")
    if len(records) == 0:
        print("No student records found.")
        return

    print(f"{'ID':<10} {'Name':<20} {'Course':<12} {'Marks':<8}")
    print("-" * 52)
    for student_id, details in records.items():
        print(f"{student_id:<10} {details['name']:<20} {details['course']:<12} {details['marks']:<8}")



def search_student(records):
    print("\n--- SEARCH STUDENT ---")
    student_id = input("Enter Student ID to search: ").strip().upper()

    if student_id in records:
        student = records[student_id]
        print("\nRecord found:")
        print(f"ID     : {student_id}")
        print(f"Name   : {student['name']}")
        print(f"Course : {student['course']}")
        print(f"Marks  : {student['marks']}")
    else:
        print(f"Record not found for ID '{student_id}'.")



def update_student(records):
    print("\n--- UPDATE STUDENT ---")
    student_id = input("Enter Student ID to update: ").strip().upper()

    if student_id not in records:
        print(f"Record not found for ID '{student_id}'.")
        return

    print(f"Current Details -> Name: {records[student_id]['name']}, Course: {records[student_id]['course']}, Marks: {records[student_id]['marks']}")

    new_name = input("Enter new Name (press Enter to keep current): ").strip().replace(",", " ")
    new_course = input("Enter new Course (press Enter to keep current): ").strip().upper().replace(",", " ")

    if new_name != "":
        records[student_id]["name"] = new_name
    if new_course != "":
        records[student_id]["course"] = new_course

    change_marks = input("Do you want to update marks? (y/n): ").strip().lower()
    if change_marks == "y":
        records[student_id]["marks"] = get_valid_marks()

    save_records(records)
    print(f"Success: Record for ID '{student_id}' updated!")



def delete_student(records):
    print("\n--- DELETE STUDENT ---")
    student_id = input("Enter Student ID to delete: ").strip().upper()

    if student_id in records:
        deleted_name = records[student_id]["name"]
        del records[student_id]
        save_records(records)
        print(f"Success: Record for '{deleted_name}' (ID: {student_id}) deleted!")
    else:
        print(f"Record not found for ID '{student_id}'.")



def main():
    records = load_records()

    while True:
        print("\n===============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("===============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            view_students(records)
        elif choice == "3":
            search_student(records)
        elif choice == "4":
            update_student(records)
        elif choice == "5":
            delete_student(records)
        elif choice == "6":
            save_records(records)
            print("Records saved. Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


main()