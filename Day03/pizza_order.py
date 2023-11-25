print("wellcome to the pizza hat ")
size = input("what size pizza do you want? S, M or L ")
addPepperoni = input("do you want pepperoni? Y or N ")
extraCheese = input("do you extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 150
elif size == "M":
    bill += 200
else:
    bill += 250

if addPepperoni =="Y":
    if size == "S":
        bill +=20
    else:
        bill += 30
if extraCheese == "Y":
    bill += 10
print(f"your final bill {bill},tk")
