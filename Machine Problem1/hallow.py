size = int(input("Enter the size of the square: ")) #get the size of the square from the user
for i in range(size): 
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ") #print  if the position is in the border not inside
        else:
            print(" ", end=" ") #print if the position is inside the border
    print()
