def avg(english, nepali, math):
    average = (english + nepali + math) / 3
    return average


student_name = input("Enter student's name: ")

while True:
    english = float(input("Enter marks of English (0-100): "))
    if 0 < english < 100:
        break
    print("Invalid marks! Please enter again.")
while True:
    nepali = float(input("Enter marks of Nepali (0-100): "))
    if 0 < nepali < 100:
        break
    print("Invalid marks! Please enter again.")
while True:
    math = float(input("Enter marks of Math (0-100): "))
    if 0 < math < 100:
        break
    print("Invalid marks! Please enter again.")
    
total = english + nepali + math

average = avg(english, nepali, math)

# using of conditional statements to determine grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B+"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C+"
elif average >= 40:
    grade = "C"
else:
    grade = "NG"
    
# Display the student name, total marks, average and grade
print("Student Result: ")
print(f"Student Name: {student_name}")
print(f"Total Marks: {total}'/300'")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")