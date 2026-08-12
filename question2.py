#Problem 2: Student Marks and Grade Analyzer
#Take the student’s name and five subject marks from the user.
name = input("Enter Student name: ")
s1 = int(input("Enter Marks: "))
s2 = int(input("Enter Marks: "))
s3 = int(input("Enter Marks: "))
s4 = int(input("Enter Marks: "))
s5 = int(input("Enter Marks: "))

marks = [s1, s2, s3, s4, s5]
total_marks = sum(marks)
avgerage_marks = total_marks / 5
high_marks = max(marks)
low_marks = min(marks)

passed = sum(1 for m in marks if m >= 40)
failed = len(marks) - passed

if avgerage_marks >= 90:
    grade = "A"
elif avgerage_marks >= 75:
    grade = "B"
elif avgerage_marks >= 60:
    grade = "C"
elif avgerage_marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Total Marks: ", total_marks)
print("Average Marks: ", avgerage_marks)
print("High Marks: ", high_marks)
print("Low Marks: ", low_marks)
print("Grade: ", grade)
print(f"Number of subjects Passed: {passed}")
print(f"Number of subjects Failed: {failed}")
