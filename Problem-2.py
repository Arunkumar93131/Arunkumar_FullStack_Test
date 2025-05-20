# File: Problem-2.py

def generate_series(n):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

# Example usage:
x = int(input("Enter a number: "))
print(generate_series(x))
