power = 1000

total = 2**power

length = len(str(total))

sumof = 0

for x in range(0,length):
    sumof += int(str(total)[x])

print(sumof)
