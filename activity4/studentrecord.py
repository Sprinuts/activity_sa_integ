import os

student_records = []

defaultFileName = "studentrecord.txt"
openedFileName = None

while True:
    os.system("cls")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        fileName = input("Enter file name: ")
        fileName = fileName + ".txt"
        file = open(fileName, "a+")
        print(f"The file {fileName} opened successfully.")
        openedFileName = fileName
        os.system("pause")
        os.system("cls")

    elif choice == '2':
        if openedFileName:
            file = open(openedFileName, "a")
        else:
            file = open(defaultFileName, "a")
        for record in student_records:
            formattedRecord = str(tuple(record.split(','))) + "\n"
            file.write(formattedRecord)
        file.close()
        if openedFileName:
            print(f"The file {openedFileName} saved successfully.")
        else:
            print(f"The file {defaultFileName} saved successfully.")
        os.system("pause")
        os.system("cls")

    elif choice == '3':
        fileName = input("Enter file name: ")
        fileName = fileName + ".txt"
        file = open(fileName, "a")
        for record in student_records:
            formattedRecord = str(tuple(record.split(','))) + "\n"
            file.write(formattedRecord)
        file.close()
        print(f"The file {fileName} saved successfully.")
        os.system("pause")
        os.system("cls")

    elif choice == '4':
        if openedFileName:
            file = open(openedFileName, "r")
        else:
            file = open(defaultFileName, "r")
        records = file.readlines()
        file.close()
        for record in records:
            print(record.strip())
        os.system("pause")
        os.system("cls")
        # Code to show all student records

    elif choice == '5':
        # Code to show a specific student record
        studentId = input("Enter the student ID: ")
        found = False

        if openedFileName:
            file = open(openedFileName, "r")
        else:
            file = open(defaultFileName, "r")

        records = file.readlines()
        file.close()

        for record in records:
            current_student_id = record.split(',')[0].strip("('")  # Extracting and cleaning the student ID
            if current_student_id == studentId:
                found = True
                print(record.strip())
                break

        if not found:
            print("Student record not found.")
        os.system("pause")
        os.system("cls")

    elif choice == '6':
        # Code to add a new student record
        studentId = input("Enter student ID: ")
        studentName = input("Enter student name: ")
        classStanding = input("Enter class standing: ")
        majorExam = input("Enter major exam grade: ")
        record = f"{studentId},{studentName},{classStanding},{majorExam}"
        student_records.append(record)
        print("Student record added successfully.")
        os.system("pause")
        os.system("cls")
        
    elif choice == '7':
        # Code to edit a student record
        studentId = input("Enter the student ID of the record you want to edit: ")
        found = False

        if openedFileName:
            file = open(openedFileName, "r+")
        else:
            file = open(defaultFileName, "r+")

        records = file.readlines()

        for i, record in enumerate(records):
            current_student_id = record.split(',')[0].strip("('")  # Extracting and cleaning the student ID
            if current_student_id == studentId:
                found = True
                print("Enter the updated information:")
                studentName = input("Enter student name: ")
                classStanding = input("Enter class standing: ")
                majorExam = input("Enter major exam grade: ")
                updated_record = str((studentId, studentName, classStanding, majorExam)) + "\n"
                records[i] = updated_record
                print("Student record updated successfully.")
                os.system("pause")
                break

        if not found:
            print("Student record not found.")
            os.system("pause")

        file.seek(0)
        file.writelines(records)
        file.truncate()
        file.close()

    elif choice == '8':
        if openedFileName:
            file = open(openedFileName, "r")
        else:
            file = open(defaultFileName, "r")
        records = file.readlines()
        file.close()

        if len(records) == 0:
            print("No student records found.")
        else:
            confirm = input("Are you sure you want to delete all student records? (y/n): ")
            if confirm.lower() == 'y':
                if openedFileName:
                    file = open(openedFileName, "w")
                else:
                    file = open(defaultFileName, "w")
                file.close()
                print("All student records have been deleted.")
            else:
                print("Deletion cancelled.")

        os.system("pause")
        os.system("cls")

    elif choice == '9':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")