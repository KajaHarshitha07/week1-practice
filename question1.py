#Problem 1: Electricity Bill Calculator
#Write a Python program that reads the customer’s name and the number of electricity units consumed.

name = input("Enter the customer name: ")
units = float(input("Enter the number of electricity units consumed: "))
charge = 0
if units <= 100:
    charge=units * 2
elif units <= 200:
    charge = 100 * 2 + (units - 100) * 3
else:
    charge = 100 * 2 + 100 * 3 +  (units - 200) * 5
surcharge = 0
if charge >= 1000:
    surcharge =charge * 0.05
Final_bill = charge + surcharge

print("Customer Name: ", name)
print("Units Consumed: ", units)
print("Electricity Charge: ", charge)
print("Surcharge: ", surcharge)
print("Final Bill: ", Final_bill)
