import math;

def add(x,a): 
    return x+a;
def subtract(x,y): 
    return x-y;
def multiply(x,y): 
    return x*y;
def divide(x,y):
    if (y == 0):
        raise ValueError("Can't divide by zero");
    else: 
        return x/y;
def power(x,y): 
    return x**y;
def square_root(x):
    if (y == 0):
        raise ValueError("Can't take square root of a negative number");
    else: 
        return math.sqrt(x);