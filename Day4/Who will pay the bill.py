import random
namesString = input("Giv me  everybody\'s names, seperated by a comma. ")
names = namesString.split(", ")
numberOfPeople = len(names)
randomPerson = random.randint(0, numberOfPeople)
badLuckPerson = names[randomPerson]
print(f"Bill will pay {badLuckPerson}")