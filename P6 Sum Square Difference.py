# Finds the difference between the square of the sum of all numbers up to MaxNumber
# and the sum of the squares of all numbers up to MaxNumber

def SumOfSquares(x):
    sumof = 0
    for i in range(1,x+1):
        j = i**2
        sumof += j
    return sumof

def SquareOfSum(x):
    sumof = 0
    for i in range(1,x+1):
        sumof += i
    sumof = sumof**2
    return sumof

MaxNumber = 100

print(SquareOfSum(MaxNumber) - SumOfSquares(MaxNumber))
