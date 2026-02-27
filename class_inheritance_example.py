class Animal:
    def __init__(self, Name, Sound, Size, Intelligence):
        self.Name = Name #String
        self.Sound = Sound #String
        self.Size = Size #Integer
        self.Intelligence = Intelligence #Integer

    def Description(self):
        String = f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}."
        return String

class Parrot(Animal):
    def __init__(self, pName, pSound, pSize, pIntelligence, pWingSpan, pNumberWords):
        super().__init__(pName, pSound, pSize, pIntelligence)
        self.WingSpan = pWingSpan #Integer
        self.NumberWords = pNumberWords #Integer

    def ChangeNumberWords(self, Change):
        self.NumberWords = self.NumberWords + Change

    def Description(self):
        String = super().Description() + f" It has a wingspan of {self.WingSpan} cm and can say {self.NumberWords} words."
        return String

class Wolf(Animal):
    def __init__(self, wName, wSound, wSize, wIntelligence, wTerritorySize):
        super().__init__(wName, wSound, wSize, wIntelligence)
        self.TerritorySize = wTerritorySize #Integer

    def SetTerritorySize(self, ChangeSize):
        self.TerritorySize = self.TerritorySize + ChangeSize

    def Description(self):
        String = super().Description() + f" Its territory is {self.TerritorySize} square miles."
        return String

NewParrot = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
NewWolf = Wolf("Nighteyes", "Howl", 8, 7, 100)
NewHorse = Animal("Copper", "Neigh", 10, 6)

NewWolf.SetTerritorySize(-20)
NewParrot.ChangeNumberWords(2)
print(NewParrot.Description())
print(NewWolf.Description())
print(NewHorse.Description())
