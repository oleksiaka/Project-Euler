months = [31,28,31,30,31,30,31,31,30,31,30,31]

count = 0
DayOfWeek = 1
for x in range(1900,2001):

    if x % 4 == 0 and x != 1900:
        months[1] = 29
    else:
        months[1] = 28
    
    for y in range(0,12):
        days = 0

        while days < months[y]:
            if x > 1900:
                if days == 0 and DayOfWeek == 0:
                    count += 1
            if DayOfWeek < 6:
                DayOfWeek += 1
            else:
                DayOfWeek = 0

            days += 1

print(count)
