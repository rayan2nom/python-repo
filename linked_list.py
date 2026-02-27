class Node: #Making the building block: Node
    def __init__(self, Data):
        self._TheData = Data
        self._NextNode = None #Node

    def GetData(self):
        return self._TheData
    def GetNextNode(self):
        return self._NextNode

    def SetNextNode(self, Object):
        self._NextNode = Object

class LinkedList: #The entire linked list
    def __init__(self):
        self._HeadNode = None #Node

    def InsertNode(self, Integer):
        TheNode = Node(Integer)
        TheNode.SetNextNode(self._HeadNode)
        self._HeadNode = TheNode

    def Traverse(self):
        String = ''
        CurrentNode = self._HeadNode
        while CurrentNode != None:
            String = String + str(CurrentNode.GetData()) + " "
            CurrentNode = CurrentNode.GetNextNode()
        return String

    def RemoveNode(self, Integer):
        CurrentNode = self._HeadNode
        if CurrentNode == None:
            return False
        elif CurrentNode.GetData() == Integer:
            return True

        Found = False
        while Found == False and CurrentNode != None:
            if CurrentNode.GetNextNode().GetData() == Integer:
                Found = True
                CurrentNode.SetNextNode(CurrentNode.GetNextNode().GetNextNode())
            else:
                CurrentNode = CurrentNode.GetNextNode()

        return Found

List = LinkedList()
List.InsertNode(10)
List.InsertNode(20)
List.InsertNode(30)
List.InsertNode(40)
List.InsertNode(50)
ReturnValue = List.Traverse()
print(ReturnValue)
List.RemoveNode(30)
ReturnValue = List.Traverse()
print(ReturnValue)
