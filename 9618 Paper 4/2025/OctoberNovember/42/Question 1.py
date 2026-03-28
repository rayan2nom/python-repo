class Bird:
    def __init__(self, dist, spec):
        self._DistancePerHour = dist #Real
        self._Species = spec #String
        self._XPosition = 500.0 #Rael
        self._YPosition = 500.0 #Real

    def GetSpecies(self):
        return self._Species

    def GetPosition(self):
        Position = f"X = {self._XPosition} & Y = {self._YPosition}"
        return Position

    def Move(self, MovePosition, FlyMinutes):
        DistanceTravelled = (self._DistancePerHour/60) * FlyMinutes

        if MovePosition == 'N':
            self._YPosition = self._YPosition + DistanceTravelled
        elif MovePosition == 'S':
            self._YPosition = self._YPosition - DistanceTravelled
        elif MovePosition == 'E':
            self._XPosition = self._XPosition + DistanceTravelled
        elif MovePosition == 'W':
            self._XPosition = self._XPosition - DistanceTravelled

Bird1 = Bird(71.0, "Cockatiel")
Bird2 = Bird(56.0, "Macaw")

print(f"Species: {Bird1.GetSpecies()} | Current Position: {Bird1.GetPosition()}")
print(f"Species: {Bird2.GetSpecies()} | Current Position: {Bird2.GetPosition()}")

Choice = input("Choose either the Cockatiel or Macaw: ")
while Choice.lower() != "cockatiel" and Choice.lower() != "macaw":
    Choice = input("Invalid! You must choose either the Cockatiel or Macaw: ")

Direction = input("Choose any direction of N, S, E or W: ")
while Direction.lower() != 'n' and Direction.lower() != 's' and Direction.lower() != 'e' and Direction.lower() != 'w':
    Direction = input("Invalid! You must choose either N, S, E or W: ")

Minutes = int(input("Enter the time the bird has been flying (to the nearest minute): "))

if Choice.lower() == "cockatiel":
    Bird1.Move(Direction, Minutes)
    print(f"{Bird1.GetSpecies()} | New Position: {Bird1.GetPosition()}")
else:
    Bird2.Move(Direction, Minutes)
    print(f"{Bird2.GetSpecies()} | New Position: {Bird2.GetPosition()}")

