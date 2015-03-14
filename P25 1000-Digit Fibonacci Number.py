def SumOfFib():
    a = 1
    b = 2
    count = 3
    while True:       
        if len(str(b)) == 1000:      
            print(count)
            break
        b = b + a
        a = b - a
        count += 1
SumOfFib()

