studentScore = input("Input a list of student score ").split()
for n in range (0, len(studentScore)):
    studentScore[n] = int(studentScore[n])
print(studentScore)

heightScore = 0
for score in studentScore:
    if score > heightScore:
        heightScore = score
print(f"The height score in the class is: {heightScore}")