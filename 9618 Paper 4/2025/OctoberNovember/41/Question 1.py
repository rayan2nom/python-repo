from random import randrange

Stack = []
for x in range(30):
    Stack.append(-1)
TopOfStack = -1

def Push(IntegerToPush):
    global TopOfStack, Stack

    if TopOfStack + 1 == 30:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = IntegerToPush
        return True

def Pop():
    global TopOfStack, Stack

    if TopOfStack == -1:
        return -999
    else:
        ReturnVal = Stack[TopOfStack]
        TopOfStack -= 1
        return ReturnVal

for x in range(40):
    Number = randrange(0, 1001)
    pushed = Push(Number)
    if not pushed:
        print("Stack full")
        break

def FindValues():
    global TopOfStack, Stack

    Largest = -9999
    Smallest = 10000

    for x in range(TopOfStack+1):
        Value = Pop()
        if Value > Largest:
            Largest = Value

        if Value < Smallest:
            Smallest = Value

    print(f"Largest number in stack: {Largest}")
    print(f"Smallest number in stack: {Smallest}")

FindValues()
