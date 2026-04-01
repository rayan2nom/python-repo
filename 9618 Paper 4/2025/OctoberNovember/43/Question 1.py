class BoardObject:
    def __init__(self, code, value):
        self._Code = code #String
        self._Value = value #Integer

    def GetCode(self):
        return self._Code

    def GetValue(self):
        return self._Value

Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
Object3 = BoardObject("C", 5)
Object4 = BoardObject("D", 2)
Object5 = BoardObject("E", 7)

class Board:
    def __init__(self):
        self._TheBoard = [[BoardObject("-", 0) for col in range(10)] for row in range(10)]

    def GetObject(self, Row, Column):
        return self._TheBoard[Row][Column]

    def SetObject(self, BoardObject, Row, Column):
        self._TheBoard[Row][Column] = BoardObject

    def DisplayBoard(self):
        for row in range(10):
            Line = ''
            for col in range(10):
                Line = Line + self._TheBoard[row][col].GetCode() + " "
            print(Line)

NewBoard = Board()
NewBoard.SetObject(Object1, 0, 0)
NewBoard.SetObject(Object2, 9, 9)
NewBoard.SetObject(Object3, 4, 5)
NewBoard.SetObject(Object4, 2, 2)
NewBoard.SetObject(Object5, 8, 7)

NewBoard.DisplayBoard()

RPos = int(input("Enter a row between 0 and 9 inclusive: "))
while RPos < 0 or RPos > 9:
    RPos = int(input("Invalid number! Enter a row between 0 and 9 inclusive: "))

RCol = int(input("Enter a column between 0 and 9 inclusive: "))
while RCol < 0 or RCol > 9:
    RCol = int(input("Invalid number! Enter a column between 0 and 9 inclusive: "))

if NewBoard.GetObject(RPos, RCol).GetCode() == "-":
    print("Miss")
else:
    print(f"Code: {NewBoard.GetObject(RPos, RCol).GetCode()} | Value: {NewBoard.GetObject(RPos, RCol).GetValue()}")
