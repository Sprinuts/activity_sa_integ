rows = int(input("Enter the number of rows: ")) #get the number of rows from the user
number = 1 # first number in the triangle
for i in range(1, rows + 1):
    for j in range(1, i + 1): 
        print(number, end=" ") #print the number and add a space
        number += 1 #increment the number
    print() #then new line after each row
