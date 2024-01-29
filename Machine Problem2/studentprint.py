#open the file as read only
file = open('students.txt', 'r')
lines = file.readlines() #assign the lines of the file to a variable

print()
print("Student ID\tName\t\t\tQuiz Scores\t\t\tAverage Score") #for ease of looking at the record
print("------------------------------------------------------------------------------------")
#printing the records
for line in lines:
    studentData = line.strip().split(',') #remove the newline character and split the data
    id = studentData[0] #assign the data to variables
    name = studentData[1]
    quizScore = studentData[2:]
    
    totalScore = 0 #initialize the total score to 0
    for score in quizScore:
        totalScore += int(score) #add the scores to the total score
    average_score = totalScore / 4 #compute for the average score

    print(f"{id}\t{name}\t\t{quizScore}\t{average_score}") #print the record
print("------------------------------------------------------------------------------------")
print()
file.close()