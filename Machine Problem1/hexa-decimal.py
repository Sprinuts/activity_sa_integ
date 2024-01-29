hexdigits = "0123456789ABCDEF" #variable that contains ll the hexademical digits
decimal = int(input("Enter a decimal number: ")) #get the decimal number from the user
hexadecimal = "" #empty string

while decimal > 0: #loop until the decimal will become 0
    remainder = decimal % 16 #get the remainder by dividing by 16 which is the hexadecimal base
    hexadecimal = hexdigits[remainder] + hexadecimal #get the hexadecimal digit from hexdigits
    decimal = decimal // 16 

hexadecimalValue = hexadecimal #assign hexadecimal to a new variable
print(f"The hexadecimal value of is {hexadecimalValue}")