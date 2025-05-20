# File: Problem-3.py

def generate_limited_series(x):
    result = []
    for i in range(1, 2 * x):
        if i % 2 != 0:
            result.append(i)
        if len(result) == x or i > x * 2:
            break
    return result

# Example usage:
x = int(input("Enter a number: "))
print(generate_limited_series(x))
