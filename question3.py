#Problem 3: Course Enrollment Analyzer
#Start with the following dictionary:
courses = {
    "Python": 25,
    "Java": 18,
    "SQL": 30,
    "Web": 15
}
for course,enrolled in courses.items():
    print(f"{course}: {enrolled} students enrolled")

search_course = input("enter a course: ")
if search_course in courses:
    print(f"Current enrollment for {search_course} : {course[search_course]}")
else:
    print(f"Course not found")

total_enrollments = sum(courses.values())
highest_courses = max(courses, key = courses.get)
lowest_courses = min(courses, key = courses.get)
morethan_20 = {course for course, enrollement in courses.items() if enrollement > 20}

print(f"Total Enrollments: {total_enrollments}")
print(f"Course with Highest Enrollment: {highest_courses}")
print(f"Course with Lowest Enrollment: {lowest_courses}")
print(f"Courses with more than 20 students enrolled: {morethan_20}")

