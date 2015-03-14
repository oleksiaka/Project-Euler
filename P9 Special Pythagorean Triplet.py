a = 1
while a < 1000:
    b = 1
    while b < 1000:
        c = 1
        while c < 1000:
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(a*b*c)
            c += 1
        b += 1
    a += 1

    
    

