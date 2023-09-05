print("welcome to the love calculator")
name1 = input("what is your name ")
name2 = input("what is their name ")
combinedString = name1 + name2
lowerCaseString = combinedString.lower()
t = lowerCaseString.count("t")
r = lowerCaseString.count("r")
u = lowerCaseString.count("u")
e = lowerCaseString.count("e")
true = t+r+u+e
l = lowerCaseString.count("l")
o = lowerCaseString.count("o")
v = lowerCaseString.count("v")
e = lowerCaseString.count("e")
love = l+o+v+e
loveScore = int(str(true) + str(love))


if (loveScore < 10) or (loveScore > 90):
    print(f"your love score is {loveScore},you go together like coke and mentos")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"your love score is {loveScore}, you are alright")
else:
    print(f"your love score is {loveScore}")
