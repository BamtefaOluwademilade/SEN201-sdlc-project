student_name = input("Enter student name: ")
score = int(input("Enter student score: "))

if score >= 70 and score <= 100:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 0:
    grade = "F"
else:
    grade = "Invalid score"

print("Student Name:", student_name)
print("Score:", score)
print("Grade:", grade)