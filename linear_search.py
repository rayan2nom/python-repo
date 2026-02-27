import random #Import random library

Array = []

for Index in range(15): #Inputting 15 random and unique integers in Array
    Number = random.randint(0, 101)
    while Number in Array:
        Number = random.randint(0, 101)
    Array.append(Number)
Array.sort() #Sorts array in ascending order by default

SearchValue = int(input("Enter the value to search in array: ")) #Linear search algorithm
Found = False

for Index in range(len(Array)):
    if Array[Index] == SearchValue:
        Found = True
        FoundIndex = Index
        break

if Found:
    print(f"Value found at index {FoundIndex}")
else:
    print("Value not found in array")
