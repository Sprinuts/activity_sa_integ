#open the students.txt file
file = open("students.txt", "a")
print()
#get the number of records to be added
numberRecords = int(input("Enter the number of records: "))
#get the student information and write it to the file
for i in range(numberRecords):
    print()
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    quiz1 = input("Enter quiz 1 score: ")
    quiz2 = input("Enter quiz 2 score: ")
    quiz3 = input("Enter quiz 3 score: ")
    quiz4 = input("Enter quiz 4 score: ")
    file.write(f"{id}, {name}, {quiz1}, {quiz2}, {quiz3}, {quiz4}\n") 
file.close() #close the file
print()
print("The record has been saved to students.txt.") #message to user