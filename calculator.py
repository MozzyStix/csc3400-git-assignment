import math;

def add(x,y): 
    try:
        return float(x) + float(y)
    except ValueError:
        raise ValueError("Both inputs must be numbers")
def subtract(x,y): 
    try:
        return float(x) - float(y)
    except ValueError:
        raise ValueError("Both inputs must be numbers")
def multiply(x,y): 
    try:
        return float(x) * float(y)
    except ValueError:
        raise ValueError("Both inputs must be numbers")
def divide(x,y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return x / y
def power(x,y): 
    try:
        return float(x) ** float(y)
    except ValueError:
        raise ValueError("Both inputs must be numbers")
def square_root(x):
    try:
        x = float(x)
    except ValueError:
        raise ValueError("Input must be a number")

    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    else:
        return math.sqrt(x)