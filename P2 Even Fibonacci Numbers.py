#Finds the sum of even Fibonacci Numbers below given MaxNumber

def SumOfFib(MaxNumber):
    a = 1
    b = 2
    total = 0
    while b < MaxNumber:       
        if b % 2 == 0:      #Sums only even fibonacci numbers
            total += b      #
        b = b + a
        a = b - a
    return total

print(SumOfFib(4000000))

    
