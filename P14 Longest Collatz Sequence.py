longest = 0

a = []
x0 = -1
xlast = 0
for x in range(10,1000000):
    
    count = 1
    a.append(x)
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        count += 1
    x0 += 1
    if count > longest:
        longest = count
        xlast = x0
        #print(a[x0],longest)


print(a[xlast])

