import itertools

numbers = [0,1,2,3,4,5,6,7,8,9]
count  = 0

for x in itertools.permutations(numbers):
    count += 1
    if count == 1000000:
        print(x)
    



