Queue = []
for x in range(100):
    Queue.append('')
QueueHead = -1
QueueTail = -1
NumberItems = 0

def Enqueue(StringToAdd):
    global Queue, QueueHead, QueueTail, NumberItems

    if NumberItems == 100:
        return False
    else:
        if NumberItems == 0:
            QueueHead = 0
        QueueTail += 1
        Queue[QueueTail] = StringToAdd
        NumberItems += 1
        return True

def Dequeue():
    global Queue, QueueHead, QueueTail, NumberItems

    if NumberItems == 0:
        return "False"
    else:
        if NumberItems == 1:
            QueueTail = -1
            ReturnVal = Queue[QueueHead]
            QueueHead = -1
        else:
            ReturnVal = Queue[QueueHead]
            QueueHead += 1
        NumberItems -= 1

        return ReturnVal

def ReadData():
    try:
        with open("BinaryData.txt", "r") as file:
            for line in file:
                Digit = line.strip()
                if Enqueue(Digit) == False:
                    print("The queue is full!")
                    break
    except IOError:
        print("File not found!")

NewString = ''
def Compress():
    global NumberItems, NewString

    Appear = 1
    Current = Dequeue()
    Previous = Current

    while NumberItems > 0:
        Current = Dequeue()

        if Current == Previous:
            Appear += 1
        else:
            NewString += Previous + str(Appear)
            Previous = Current
            Appear = 1


    NewString = NewString + Previous + str(Appear)

ReadData()
Compress()
print(NewString)
