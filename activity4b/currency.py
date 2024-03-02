import csv

amount = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ")

exchangeRates = {}
with open('currency.csv', 'r') as file:
	reader = csv.reader(file)
	next(reader)
	for row in reader:
		exchangeRates[row[0]] = float(row[2])
		
if currency not in exchangeRates:
	print(f"The currency '{currency}' is not found in the exchange rates.")
else:
	converted = amount * exchangeRates[currency]
	
	print(f"Dollar: {amount} USD")
	print(f"{currency}: {converted}")