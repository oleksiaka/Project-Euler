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

total = 0
x= 0
while x < 2000000:
    if isprime(x) == True:
        total += x
    x += 1
print(total)
