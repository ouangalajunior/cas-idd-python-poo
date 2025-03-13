#module math_utilss.py

def factorielle(n):
    if n == 0 or n ==1:
        return 1
    return n*factorielle(n-1)


def fibonacci(n):
    if n<=0:
        return "n foit être un entier positif"
    elif n==1:
        return 0
    elif n==2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

