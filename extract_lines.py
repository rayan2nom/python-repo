HighScores = [[" ", " ", " "] for index in range(7)]

def ReadData():
    global HighScores
    try:
        file = open("HighScoreTable.txt")

        PlayerID = file.readline().strip()

        Players = 0
        while PlayerID != "":
            GameLevel = file.readline().strip()
            Score = file.readline().strip()

            HighScores[Players][0] = PlayerID
            HighScores[Players][1] = GameLevel
            HighScores[Players][2] = Score

            Players += 1

            PlayerID = file.readline().strip()

        file.close()
    except IOError:
        print("File not found")

def OutputHighScores(Array):
    for x in range(7):
        Output = f"{Array[x][0]} reached level {Array[x][1]} with a score of {Array[x][2]}"
        print(Output)

def SortScores():
    Swap = True
    Length = 7

    while Swap == True and Length > 1:
        Swap = False
        for x in range(Length-1):
            if int(HighScores[x][1]) < int(HighScores[x+1][1]):
                TempLevel = HighScores[x+1][1]
                HighScores[x+1][1] = HighScores[x][1]
                HighScores[x][1] = TempLevel

                TempID = HighScores[x + 1][0]
                HighScores[x + 1][0] = HighScores[x][0]
                HighScores[x][0] = TempID

                TempScore = HighScores[x + 1][2]
                HighScores[x + 1][2] = HighScores[x][2]
                HighScores[x][2] = TempScore

                Swap = True

        Length -= 1

ReadData()
print("Before")
OutputHighScores(HighScores)
SortScores()
print("After")
OutputHighScores(HighScores)
