print("Student Result Management System")

student_name = input("Enter student name: ")
score = int(input("Enter student score: "))

if score >= 50:
    result = "PASS"
else:
    result = "FAIL"

print("Student Name:", student_name)
print("Score:", score)
print("Result:", result)