def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements == 0:
        return 0

    if ArrayCopy[NumberElements-1] == DataToFind:
        return RecursiveCount(ArrayCopy, NumberElements-1, DataToFind) + 1
    else:
        return RecursiveCount(ArrayCopy, NumberElements-1, DataToFind)

Array = [0,5,1,2,5,9,9,6,5,0]
print(RecursiveCount(Array, 10, 0))

LocString = "x=0;y=1;x=x+y;y++;"

def SplitData(String):
    Length = len(String)
    StringArray = []
    Line = ''
    for x in range(Length):
        if String[x] != ";":
            Line = Line + String[x]
        else:
            StringArray.append(Line)
            Line = ''

    return StringArray

print(SplitData(LocString))
