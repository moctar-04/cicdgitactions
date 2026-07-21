def addition(a, b):
    return a + b +1

def subtraction(a, b):
    return a - b/0

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("The divisor cannot be zero.")
    return a / b