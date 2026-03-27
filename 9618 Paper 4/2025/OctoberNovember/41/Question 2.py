class Train:
    def __init__(self, ID, route):
        self._TrainIDNumber = ID #String
        self._Route = route #Integer

    def GetTrainIDNumber(self):
        return self._TrainIDNumber
    def GetRoute(self):
        return self._Route

Train1 = Train("12ADV", 134)
Train2 = Train("33ART", 20)
Train3 = Train("9FKF", 3)
Train4 = Train("21VBC", 24)

class Station:
    def __init__(self, ID, noplat):
        self._StationID = ID #String
        self._NumberPlatforms = noplat #Integer
        self._Trains = [] #Array[0:9] of Train
        self._NumberTrains = 0 #Integer

    def AddTrain(self, TrainRecord):
        if self._NumberTrains == self._NumberPlatforms:
            return False
        else:
            self._Trains.append(TrainRecord)
            self._NumberTrains += 1
            return True

    def GetTrains(self):
        if self._NumberTrains == 0:
            return "There are no trains"
        else:
            String = f"The trains at the station {self._StationID} are:"
            for x in range(self._NumberTrains):
                ID = self._Trains[x].GetTrainIDNumber()
                Route = self._Trains[x].GetRoute()

                Line = f"\n {ID} on route number {Route}"
                String = String + Line

            return String

Station1 = Station("STH", 2)
Station2 = Station("NTH", 1)

Attempt1 = Station1.AddTrain(Train1)
if Attempt1 == False:
    print("Station is full")

Attempt2 = Station1.AddTrain(Train2)
if Attempt2 == False:
    print("Station is full")

Attempt3 = Station1.AddTrain(Train3)
if Attempt3 == False:
    print("Station is full")

Attempt4 = Station2.AddTrain(Train4)
if Attempt4 == False:
    print("Station is full")

print(Station1.GetTrains())
print(Station2.GetTrains())
