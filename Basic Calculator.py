def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return "Invalid operation"

a = 20
b = 10
print("Addition:", calculator(a, b, 'add'))
print("Subtraction:", calculator(a, b, 'subtract'))
print("Multiplication:", calculator(a, b, 'multiply'))
print("Division:", calculator(a, b, 'divide'))
