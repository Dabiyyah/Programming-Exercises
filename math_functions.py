def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with  just functions!")

age = add(12, 10)
height = subtract(70, 4)
weight = multiply(100, 1.5)

print(f"Age: {age}, Height: {height}, Weight: {weight}")

what = add(age, subtract(height, multiply(weight, 2)))

print("That becomes:", what, "No, I'm not doing it by hand.")
