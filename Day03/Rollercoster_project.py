print("Welcome to the Rollercoaster!")
height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 50
        print("child tickets are 50tk")
    elif age <= 18:
        bill = 80
        print("youth tickets are 80tk")
    else:
        bill = 100
        print("Adult tickets are 100tk")

    wantsPhotos = input("do you wants a photo taken? Y or N.")
    if wantsPhotos == "Y":
        bill += 20
    print(f"your final bill is {bill}")
else:
    print("sorry you can't ride")