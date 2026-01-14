# Day 4: Calculator with Functions
# Basic operations: +, -, *, /
# Advanced operations: power (x^y), square root, percentage
# Keep calculating until user quits
# Handle division by zero
# Store calculation history (last 5 calculations)

# Example interaction:
# === CALCULATOR ===
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Power (x^y)
# 6. Square root
# 7. Percentage
# 8. View history
# 9. Clear history
# 0. Exit

import math

history = []
history_count = 5

def saveHistory(answer):
    history.append(answer)
    if len(history)>history_count:
        history.pop(0)

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

def power(a,b):
    return math.pow(a,b)

def square_root(a):
    if a<0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def percentage(a,b):
    return (a/100)*b

def show_history():
    if not history:
        print('No History')
    else:
        for i, item in enumerate(history, start=1):
            print(f'{i}. {item}')

def clear_history():
    history.clear()
    print('History Cleared')

while True:
    print("\n=== CALCULATOR ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square root")
    print("7. Percentage")
    print("8. View history")
    print("9. Clear History")
    print("0. Exit")

    choice = input('Enter choice: ').strip()
    
    if choice == '0':
        print('GoodBye')
        break

    if choice  == '8':
        show_history()
        continue
    
    if choice == '9':
        clear_history()
        continue

    try:
        if choice in ['1', '2', '3', '4', '5', '7']:
            first = float(input('Enter first number: '))
            second = float(input('Enter second number: '))

            if choice == '1':
                result = addition(first, second)
                answer = f'{first} + {second} = {result}'
            
            elif choice == '2':
                result = subtraction(first, second)
                answer = f'{first} - {second} = {result}'

            elif choice == '3':
                result = multiply(first, second)
                answer = f'{first} * {second} = {result}'

            elif choice == '4':
                result = divide(first, second)
                answer = f'{first} / {second} = {result}'

            elif choice == '5':
                result = power(first, second)
                answer = f'{first} ** {second} = {result}'

            elif choice == '7':
                result = percentage(first, second)
                answer = f'{first} % {second} = {result}'

            print(answer)
            saveHistory(answer)

        elif choice == '6':
            a = float(input('Enter a number: '))
            result = square_root(a)
            answer = f"√{a} = {result}"
            print(answer)
            saveHistory(answer)
    
    except (ValueError, ZeroDivisionError) as e:
        print(f'Error: {e}')
