from math import sqrt

# Creates an array that lists all factors of a given number, not including itself.
def factors(number):
    ListOfFactors = [1]
    for x in range(2,int(sqrt(number)) + 1):
        if x == sqrt(number):
            ListOfFactors.append(x)
        elif number % x == 0:
            ListOfFactors.append(x)
            ListOfFactors.append(int(number / x))
    return ListOfFactors

#Checks if a given number is abundant, that is the sum of its proper divisors is
#greater than the number itself. Ex. 12 is abundant: 1 + 2 + 3 + 4 + 6 = 16 > 12

def IsAbundant(number):
    SumOfFactors = 0
    for x in factors(number):
        SumOfFactors += x
    if SumOfFactors > number:
        return True
    else:
        return False

List = []
for x in range(10,28123):
    if IsAbundant(x):
        List.append(x)

#def SumOf(number):
#    for x in List:
#        if x > number:
#            return False
#        if (number-1) in List:
#            return True
#    return False
#Total = 0
#for x in range(10,28123):
#    if not SumOf(x):
#        Total  += x
#
#print(Total)
    
            
            
        








#def AmSum(number):
#    List = []
#    for y in range(1,number):
#        if IsAbundant(y):
#            List.append(y)
#    for i in List:
#        for j in List:
#            if i + j == number:
#                print(number,i,j)
#                return False
#    return True

# Even Numbers

Total = 0
#for x in range(2,51,2):
#    if x < 24:
#        Total += x
#    else:
#        if AmSum(x):
#            Total += x

# Odd Numbers

#for x in range(1,29000,2):
#    if x < 946:
#        Total += x
#    else:
#        if AmSum(x):
#            Total += x
            


        
    
        
        
        
        





