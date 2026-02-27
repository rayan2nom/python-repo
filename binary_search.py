import random #Imports Random library

Array = []
for x in range(15): #Appending array with 15 random numbers
    Number = random.randint(0, 51)
    while Number in Array: #Ensures each integer inputted is unique
        Number = random.randint(0, 51)
    Array.append(Number)
Array.sort() #Sorts array in ascending order by default

#Binary Search algorithm
Low = 0
High = len(Array)
Found = False

SearchValue = int(input("Enter the value you want to search: "))

while Found == False and Low <= High:
    Mid = int((Low + High) / 2)
    if Array[Mid] > SearchValue:
        High = Mid - 1
    elif Array[Mid] < SearchValue:
        Low = Mid + 1
    else:
        Found = True

if Found:
    print(f"Value has been found at index {Mid}")
else:
    print("Value is not in array")
