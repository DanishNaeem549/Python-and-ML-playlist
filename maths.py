def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
       return n * factorial(n - 1)



def square(n):
    return n * n


even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

def addition(x,y):
    return x+y

def mal(x,y):
    return x*y