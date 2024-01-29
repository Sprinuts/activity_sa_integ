#open the file as write binary
file = open("students.bin", "ab")
print()
numberRecord = int(input("Enter the number of records: ")) #get the number of records to be added
#get the student information and write it to the file
for i in range(numberRecord):
    print()
    id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    quiz1 = int(input("Enter quiz 1 score: "))
    quiz2 = int(input("Enter quiz 2 score: "))
    quiz3 = int(input("Enter quiz 3 score: "))
    quiz4 = int(input("Enter quiz 4 score: "))
    record = (id, name, quiz1, quiz2, quiz3, quiz4)
    file.write(f"{record}\n".encode('utf-8')) #write the record to the file in binary
file.close()
print()
print("The record has been saved to students.bin.") #message to user

file = open('students.bin', 'rb') #open the file as read binary
print()
print("Student ID\tName\t\t\tQuiz Scores\t\t\tAverage Score") #for ease of looking at the record
print("------------------------------------------------------------------------------------")
for line in file:
    record = eval(line.decode('utf-8').strip())
    id, name, quiz1, quiz2, quiz3, quiz4 = record
    totalScore = quiz1 + quiz2 + quiz3 + quiz4 #compute for the total score
    averageScore = totalScore / 4 #compute for the average score
    print(f"{id}\t{name}\t\t({quiz1}, {quiz2}, {quiz3}, {quiz4})\t\t{averageScore}") #print the record
print("------------------------------------------------------------------------------------")
file.close()