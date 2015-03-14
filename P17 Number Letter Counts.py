
one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4

OneToNine = one+two+three+four+five+six+seven+eight+nine

ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8

TenToNineteen = ten+eleven+twelve+thirteen+fourteen+fifteen+sixteen+seventeen+eighteen+nineteen

OneToNineteen = OneToNine+TenToNineteen

twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6

TwentyToNinety = twenty+thirty+forty+fifty+sixty+seventy+eighty+ninety

HundredAnd= 10
thousand = 8

TwentyToNinetyNine = 10*TwentyToNinety + OneToNine*8

OneToNinetyNine = OneToNineteen + TwentyToNinetyNine

hundreds = (HundredAnd - 3)*9 + HundredAnd*9*99 + OneToNine*100 + OneToNinetyNine*10

Total = hundreds

Total = Total + one+thousand

print(Total)






 






    
    
    
