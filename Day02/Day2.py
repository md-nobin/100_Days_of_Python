print("Welcome to the tip calculator")
bill = float(input("What is the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount
billPerPerson = totalBill / people
finalAmount = round(billPerPerson, 2)
finalBill = "{:.2f}".format(finalAmount)
print(f"Each person should pay: {finalBill}")
