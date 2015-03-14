# Finds the sum of the digits in the factorial of n

def fact(number):
    for x in range(1,number):
        number *= x
    return number

def SumOfDigits(n):
    total = 0
    for x in range(0,len(str(fact(n)))):
        total += int(str(fact(n))[x])
    return total

print(SumOfDigits(100))
    


