import random

RandomArray = []
for x in range(20):
    Number = random.randint(1,100)
    while Number in RandomArray:
        Number = random.randint(1,100)
    RandomArray.append(Number)

def PrintArray(IntegerArray):
    Line = ''
    for x in range(len(IntegerArray)):
        Line = Line + str(IntegerArray[x]) + ' '

    print(Line)

def BubbleSort(IntegerArray):
    Swap = True
    Last = len(IntegerArray) - 1

    while Swap and Last > 0:
        Swap = False
        for x in range(Last):
            if IntegerArray[x] > IntegerArray[x+1]:
                temp = IntegerArray[x+1]
                IntegerArray[x+1] = IntegerArray[x]
                IntegerArray[x] = temp
                Swap = True
        Last = Last - 1

    return IntegerArray

PrintArray(RandomArray)
BubbleSort(RandomArray)
print("Sorted")
PrintArray(RandomArray)

def RecursiveBinarySearch(IntegerArray, LB, UB, ValueToFind):
    if LB > UB:
        return -1

    Mid = int((LB+UB/2))
    if IntegerArray[Mid] == ValueToFind:
        return Mid

    if IntegerArray[Mid] > ValueToFind:
        UB = Mid - 1
        return RecursiveBinarySearch(IntegerArray, LB, UB, ValueToFind)

    if IntegerArray[Mid] < ValueToFind:
        LB = Mid + 1
        return RecursiveBinarySearch(IntegerArray, LB, UB, ValueToFind)

Integer = int(input("Enter an integer: "))
Search = RecursiveBinarySearch(RandomArray, 0, 19, Integer)
if Search == -1:
    print("Not found")
else:
    print(f"Found at position {Search}")
