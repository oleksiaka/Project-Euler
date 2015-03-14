# Finds the nth prime

from math import sqrt

def isprime(number):

    if number < 2:
        return False
    elif number == 2:
        return True
    
    check = int(sqrt(number))

    for x in range(2,check + 1):
        if number % x == 0:
            return False
    return True

def nthPrime(n):
    count = 0
    start = 0
    while True:
        if isprime(start) == True:
            count += 1
        if count == n:
            return start
            break
        start += 1

print(nthPrime(10001))
