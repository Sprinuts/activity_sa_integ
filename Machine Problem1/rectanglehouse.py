# Get the area from the user
area = float(input("Enter the area: "))

# Compute the length and width based on the given ratio 2:1
length = (area * 2) ** 0.5
width = length / 2

# Print the results of the dog house
print(f"The size of the dog house:\nLength: {length:.2f}\nWidth: {width:.2f}")
