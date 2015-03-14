from math import sqrt
#Finds sum of natural numbers up to given number.

def TriNum(number):
    total = 0
    for x in range(1,number + 1):
        total += x
    return total

#Creates an array that lists all factors of a given number. 

def factors(number):
    ListOfFactors = []
    if number > 1:
        ListOfFactors.append(number)
    for x in range(1,int(sqrt(number)) + 1):
        if number % x == 0:
            ListOfFactors.append(x)
            if x > 1:
                ListOfFactors.append(int(number / x))
    return ListOfFactors


start = 1
while True:
    NumberOfFactors = len(factors(TriNum(start)))
    if NumberOfFactors > 500:
        print(TriNum(start))
        break
    start += 1






