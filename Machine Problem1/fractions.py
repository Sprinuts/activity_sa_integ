# Ask the user for the numerator and denominator
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

# Check if it's a proper or improper fraction
if numerator < denominator:
    print("The fraction is a proper fraction.")
else:
    # Convert to a mixed fraction
    #floor division
    wholeNumber = numerator // denominator
    remainder = numerator % denominator #get the remainder for numerator
    print("The fraction is a improper fraction.")
    print(f"The mixed function for the improper fraction: {wholeNumber} {remainder}/{denominator}")
