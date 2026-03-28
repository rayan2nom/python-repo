TreeArray = []
for row in range(50):
        TreeArray.append([-1, -1, -1])
RootPointer = -1
FreeNode = 0

def AddNode(Data):
    global TreeArray, RootPointer, FreeNode

    if FreeNode == 50:
        print("The tree is full")
    else:
        TreeArray[FreeNode][0] = -1
        TreeArray[FreeNode][1] = Data
        TreeArray[FreeNode][2] = -1

        if RootPointer == -1:
            RootPointer = FreeNode
        else:
            CurrentIndex = RootPointer
            Placed = True

            while not Placed:
                if Data >= TreeArray[CurrentIndex][1]:
                    if TreeArray[CurrentIndex][2] == -1:
                        TreeArray[CurrentIndex][2] = FreeNode
                    else:
                        CurrentIndex = TreeArray[CurrentIndex][2]
                else:
                    if TreeArray[CurrentIndex][0] == -1:
                        TreeArray[CurrentIndex][0] = FreeNode
                    else:
                        CurrentIndex = TreeArray[CurrentIndex][0]

        FreeNode += 1

try:
    with open("TreeData.txt", "r") as file:
        for line in file:
            Data = int(line.strip())
            AddNode(Data)
except IOError:
    print("File not found")

def WriteAllToFile():
    try:
        file = open("Tree.txt", "w")
        for x in range(50):
            String = str(TreeArray[x][0]) + "," + str(TreeArray[x][1]) + "," + str(TreeArray[x][2]) + "\n"
            file.write(String)
        file.close()
    except:
        print("Cannot write to file")

WriteAllToFile()
