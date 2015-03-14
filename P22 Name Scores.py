#Imports text file and organizes it into an alphabetical list.

ListOfNames = open("P22Text.txt", "r")
ListOfNames = ListOfNames.read().replace("\"","").split(",")
ListOfNames.sort()

#Creates a dictionary AlphVal which assigns a numeric value to
#each letter. Ex. A = 1, B = 2, C = 3 ...etc...

Alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
AlphVal = {}

i = 0
while i < len(Alph):
    AlphVal[Alph[i]] = i + 1
    i += 1

#Calculates numeric value for each name in the list, multiplies that
#value by its position in the list, then adds up all those values.

Total = 0
for x in range(0,len(ListOfNames)):
    Value = 0
    for y in ListOfNames[x]:
        Value += AlphVal[y]
    Value *= (x+1)
    Total += Value
print(Total)
    





    
    



