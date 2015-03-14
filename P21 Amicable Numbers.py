# Sums up all of the amicable pairs under a given number.

from math import sqrt

# Creates an array that lists all factors of a given number, not including itself. 
def factors(number):
    ListOfFactors = [1]
    for x in range(2,int(sqrt(number)) + 1):
        if number % x == 0:
            ListOfFactors.append(x)
            ListOfFactors.append(int(number / x))
    return ListOfFactors

# Sums up all of the factors of a given number.

def SumOfFactors(number):
    SumOfFactors = 0
    for x in range(0,len(factors(number))):
        SumOfFactors += factors(number)[x]
    return SumOfFactors

# Determines if a number is part of an amicable pair.

def IsAmicable(number):
    if SumOfFactors(SumOfFactors(number)) == number and SumOfFactors(number) != number:
        return True
    else:
        return False

# Sums up all amicable pairs.

def SumOfAmicable(number):
    total = 0
    for x in range(1,number):
        if IsAmicable(x):
            total += x
    return total

print(SumOfAmicable(10000))




            



    





