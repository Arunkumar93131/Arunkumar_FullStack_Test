# File: Problem-1.py

class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def calculate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            return self.a / self.b if self.b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"

# Example usage:
calc = Calculator(10, 5)
print(calc.calculate('add'))        # 15.0
print(calc.calculate('subtract'))   # 5.0
print(calc.calculate('multiply'))   # 50.0
print(calc.calculate('divide'))     # 2.0
