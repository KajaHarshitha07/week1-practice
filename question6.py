#Problem 6: Function-Based Number List Analyzer
#Take a line of space-separated integers from the user and convert it into a list.
def analyze_numbers(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)

    even_count = sum(1 for num in numbers if num %2 ==0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    return total_sum, average, highest, lowest, even_count, odd_count


def numbers_above_average(numbers, average):
    return [num for num in numbers if num > average]

user_input = input("Enter a line of space separated integers: ")
numbers = list(map(int, user_input.split()))

total_sum, average, highest, lowest, even_count, odd_count = analyze_numbers(numbers)
above_average = numbers_above_average(numbers, average)
print(f"Total Sum: {total_sum}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Even Count: {even_count}")
print(f"Odd Count: {odd_count}")
  
