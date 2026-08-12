#Function-Based Programming Questions
#Problem 4: Function-Based Shopping Bill Calculator
def calculate_bill(price, quantity):
    total_amount = price * quantity
    if total_amount >=2000:
        discount = total_amount * 0.10
    else:
        discount = 0
    final_amount = total_amount - discount
    return final_amount, total_amount, discount
product_name = input("enter product name:")    
price = int(input("enter product price:"))    
quantity = int(input("enter quantity:"))
final_amount, total_amount, discount = calculate_bill(price, quantity)
print(f"Product Name: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total Amount: {total_amount}")
print(f"Discount: {discount}")    
print(f"Final Amount: {final_amount}")