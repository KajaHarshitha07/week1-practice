#Problem 5: Employee Salary Calculator Using a Default Argument
#Create a function named:

def calculate_salary(basic_salary, bonus_percentage=5):
    bonus_amount = basic_salary * (bonus_percentage / 100)
    final_salary = basic_salary + bonus_amount
    return bonus_amount, final_salary

name = input("Enter Employee name: ")
basic_salary = int(input("Enter  salary: "))
special_bonus = input("does employee has special bonus? (yes/no): ")
if special_bonus == "yes":
    bonus_percentage = int(input("Enter bonus percentage: "))
    bonus_amount, final_salary = calculate_salary(basic_salary, bonus_percentage)
else:
    bonus_percentage = 5
    bonus_amount, final_salary = calculate_salary(basic_salary)
print(f"Employee Name: {name}")
print(f"Basic Salary: {basic_salary}")
print(f"Bonus Percenatge: {bonus_percentage}")
print(f"Bonus Amount: {bonus_amount}")
print(f"Final Salary: {final_salary}")
