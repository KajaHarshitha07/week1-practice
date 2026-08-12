# week1-practice
Normal Programming Questions
Problem 1: Electricity Bill Calculator
Write a Python program that reads the customer’s name and the number of electricity units consumed.

Use the following rates:

First 100 units      → ₹2 per unit
Next 100 units       → ₹3 per unit
Above 200 units      → ₹5 per unit
The rates must be applied slab-wise.

For example, if the customer consumes 250 units:

First 100 units      → 100 × ₹2
Next 100 units       → 100 × ₹3
Remaining 50 units   → 50 × ₹5
If the total electricity charge exceeds ₹1,000, add a surcharge of 5%.

Display:

Customer Name:
Units Consumed:
Electricity Charge:
Surcharge:
Final Bill:
Problem 2: Student Marks and Grade Analyzer
Take the student’s name and five subject marks from the user.

Store the marks inside a list.

Calculate:

Total Marks
Average Marks
Highest Mark
Lowest Mark
Number of Subjects Passed
Number of Subjects Failed
A student passes a subject when the mark is 40 or above.

Determine the final grade using the average:

Average 90 or above  → A
Average 75 to 89     → B
Average 60 to 74     → C
Average 40 to 59     → D
Average below 40     → F
Display all marks that are greater than the average.

Problem 3: Course Enrollment Analyzer
Start with the following dictionary:

courses = {
    "Python": 25,
    "Java": 18,
    "SQL": 30,
    "Web": 15
}
The dictionary contains course names and the number of enrolled students.

Display all course names with their enrollment count.

Then ask the user to enter a course name.

If the course exists, display its current enrollment. Otherwise, display:

Course not found.
Calculate and display:

Total Enrollments
Course with Highest Enrollment
Course with Lowest Enrollment
Courses Having More Than 20 Students
Create a set containing the names of courses having more than 20 students and display it.

Function-Based Programming Questions
Problem 4: Function-Based Shopping Bill Calculator
Write a function named:

calculate_bill(price, quantity)
The function must:

Receive the product price and quantity.
Calculate the total amount.
Apply a 10% discount if the total is ₹2,000 or more.
Return the total amount, discount and final amount.
Take the product name, price and quantity from the user.

Call the function and display:

Product Name:
Price:
Quantity:
Total Amount:
Discount:
Final Amount:
Do not print the result inside the function. Return the calculated values and print them after calling the function.

Problem 5: Employee Salary Calculator Using a Default Argument
Create a function named:

calculate_salary(basic_salary, bonus_percentage=5)
The function must:

Calculate the bonus using the given percentage.
Calculate the final salary.
Return the bonus amount and final salary.
Take the employee’s name and basic salary from the user.

Ask whether the employee has a special bonus percentage.

If the user enters yes, read the percentage and pass it to the function.
If the user enters no, call the function without passing the bonus percentage so that the default value is used.
Display:

Employee Name:
Basic Salary:
Bonus Percentage:
Bonus Amount:
Final Salary:
