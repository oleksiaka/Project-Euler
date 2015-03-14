# Finds the largest prime factor of given number

from math import sqrt

def isprime(number): # Tests if given number is prime

    if number < 2:
        return False
    elif number == 2:
        return True
    
    check = int(sqrt(number))

    for x in range(2,check + 1):
        if number % x == 0:
            return False
    return True


def LargestPrimeFactor(number):
    SqrtOfNumber = int(sqrt(number))
    LargestPrime = 0
    while SqrtOfNumber > 0:
        if number % SqrtOfNumber == 0:
            if isprime(SqrtOfNumber) == True and SqrtOfNumber > LargestPrime:
                LargestPrime = SqrtOfNumber
        SqrtOfNumber -= 1
    return LargestPrime

print(LargestPrimeFactor(600851475143))
