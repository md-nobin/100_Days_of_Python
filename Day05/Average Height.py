studentHeights = input("Input a list of student height ").split()
for n in range (0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])
print(studentHeights)
totalHeight = 0
for height in studentHeights:
    totalHeight += height
print(totalHeight)

numberOfStudent = 0
for student in studentHeights:
    numberOfStudent += 1
print(numberOfStudent)