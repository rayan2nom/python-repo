class Node:
    def __init__(self, nData):
        self._Data = nData #Integer
        self._LeftPointer = -1 #Integer
        self._RightPointer = -1 #Integer

    def GetLeft(self):
        return self._LeftPointer
    def GetRight(self):
        return self._RightPointer
    def GetData(self):
        return self._Data

    def SetLeft(self, Index):
        self._LeftPointer = Index
    def SetRight(self, Index):
        self._RightPointer = Index
    def SetData(self, Value):
        self._Data = Value

class TreeClass:
    def __init__(self):
        self.Tree = []
        for index in range(20):
            self.Tree.append(Node(-1))
        self.FirstNode = -1
        self.NumberNodes = 0

    def InsertNode(self, NewNode):
        if self.NumberNodes == 0:
            self.Tree[self.NumberNodes] = NewNode
            self.NumberNodes += 1
            self.FirstNode = 0
        else:
            self.Tree[self.NumberNodes] = NewNode
            CurrentIndex = self.FirstNode
            Inserted = False

            while not Inserted:
                if NewNode.GetData() < self.Tree[CurrentIndex].GetData():
                    if self.Tree[CurrentIndex].GetLeft() == -1:
                        self.Tree[CurrentIndex].SetLeft(self.NumberNodes)
                        self.NumberNodes += 1
                        Inserted = True
                    else:
                        CurrentIndex = self.Tree[CurrentIndex].GetLeft()

                elif NewNode.GetData() > self.Tree[CurrentIndex].GetData():
                    if self.Tree[CurrentIndex].GetRight() == -1:
                        self.Tree[CurrentIndex].SetRight(self.NumberNodes)
                        self.NumberNodes += 1
                        Inserted = True
                    else:
                        CurrentIndex = self.Tree[CurrentIndex].GetRight()

    def OutputTree(self):

        if self.FirstNode == -1:
            print("No nodes")
        else:
            for index in range(self.NumberNodes):
                CurrentNode = self.Tree[index]
                print(f"Left Pointer: {CurrentNode.GetLeft()} | Data: {CurrentNode.GetData()} | Right Pointer: {CurrentNode.GetRight()}")
