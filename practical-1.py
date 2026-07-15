"""Experiment:Configure VS Code with AI Coding Assistant
Objective: Implement and understand Configure VS Code with AI Coding Assistant."""
def add_numbers(num1, num2):
    sum_result = num1 + num2
    return sum_result

def check_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  
            
    return True  

num_a = int(input("Enter first number: "))
num_b = int(input("Enter second number: "))

total_sum = add_numbers(num_a, num_b)
print(f"The sum of two numbers is: {total_sum}")

if check_prime(total_sum):
    print(f"Yes, {total_sum} is a Prime Number.")
else:
    print(f"No, {total_sum} is NOT a Prime Number.")
