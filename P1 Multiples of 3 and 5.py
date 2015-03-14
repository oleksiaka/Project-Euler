#Finds the sum of all multiples of x and y below given MaxNumber

def SumOfMultiples(MaxNumber,x,y):
    total = 0
    for i in range(x,MaxNumber):
        if i % x == 0 or i % y == 0:
            total += i
    return total

print(SumOfMultiples(1000,3,5))

