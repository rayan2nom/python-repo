Values = list(map(int, input("Enter values, separating them with commas, to sort in ascending order: ").split(','))) #Prompts user input and converts string to a list of integers
Length = len(Values)
Swap = True

while Swap == True and Length > 1: #Bubble sort condition
    Swap = False
    for Index in range(0, Length - 1):
        if Values[Index] > Values[Index+1]:
            Temp = Values[Index+1]
            Values[Index+1] = Values[Index]
            Values[Index] = Temp
            Swap = True

    Length -= 1

print(Values) #Outputting array sorted in ascending order
