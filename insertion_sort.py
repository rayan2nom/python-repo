Values = list(map(int, input("Enter values, separating them by comma, to be sorted: ").split(','))) #Prompt user to input values in single line and convert to list of integers
Length = len(Values) 

for Index in range(1, Length): #Insertion sort algorithm
    Key = Index
    while Key > 0 and Values[Key - 1] > Values[Key]:
        Temp = Values[Key - 1]
        Values[Key - 1] = Values[Key]
        Values[Key] = Temp
        Key = Key - 1

print(Values) #Output list
