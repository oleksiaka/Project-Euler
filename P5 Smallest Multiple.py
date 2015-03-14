# Brute Force Method, takes along time.

#start = 20

#while True:
#    count = 0
#    for x in range(1,21):
#        if start % x == 0:
#            count += 1

#    if count == 20:
#        print(start)
#        break
#    start += 1

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

def listprimes(number):
    primelist = []
    for x in range(1,number + 1):
        if isprime(x) == True:
            primelist.append(x)
    return primelist

listofprimes = listprimes(20)
factors = []

for x in listofprimes:
    i = 1
    while x**i <= 20:
        factors.append(x)
        i += 1
        
product = 1
for x in factors:
    product *= x

print(listofprimes)
print(factors)
print(product)
    

