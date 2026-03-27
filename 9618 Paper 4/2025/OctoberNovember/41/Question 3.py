class Record:
    def __init__(self, key, data):
        self.Key = key #Integer
        self.Data = data #String

HashTable = []
def InitialiseHashTable():
    global HashTable
    HashTable = [[Record(-1, '') for x in range(10)] for x in range(100)]

def Hash(KeyField):
    HashValue = KeyField % 100
    return HashValue

def InsertData(RecordToAdd):
    global HashTable

    HashValue = Hash(RecordToAdd.Key)
    for column in range(10):
        if HashTable[HashValue][column].Key == -1:
            HashTable[HashValue][column] = RecordToAdd
            break

def ReadData():
    global HashTable
    try:
        with open("HashTableData.txt", "r") as file:
            for line in file:
                Line = line.strip().split(",")
                Add = Record(int(Line[0]), Line[1])
                InsertData(Add)
    except IOError:
        print("File not found")

def GetRecord(KeyField):
    global HashTable

    HashValue = Hash(KeyField)
    Found = False

    for column in range(10):
        if HashTable[HashValue][column].Key == KeyField:
            data = HashTable[HashValue][column].Data
            Found = True
            break

    if Found:
        print(f"Data of found record: {data}")
    else:
        print("Not found")

InitialiseHashTable()
ReadData()
for x in range(5):
    key = int(input("Enter the key field: "))
    GetRecord(key)
