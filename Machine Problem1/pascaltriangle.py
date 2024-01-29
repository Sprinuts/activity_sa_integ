# Prompt the user to enter the number of rows
n = int(input("Enter the number of rows: "))

# Iterate through each row
for i in range(n):
    coefficient = 1
    
    # Print spaces before each row
    for j in range(n - i):
        print(" ", end="")
    
    # Calculate and print the coefficients for each row
    for j in range(i + 1):
        print(coefficient, end=" ")
        coefficient = coefficient * (i - j) // (j + 1)
    
    # This will move to the next line
    print()
