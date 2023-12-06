import os
from math import prod

cwd = os.getcwd()

with open(f"{cwd}/6/input", "r") as file:
    input_data = file.read().split("\n")

with open(f"{cwd}/6/testInput", "r") as file:
    test_data = file.read().split("\n")


class Race():
    def __init__(self, time):
        self.time = time
        self.winningDistance = None

    def add_record(self, winningDistance):
        self.winningDistance = winningDistance

    def __repr__(self):
        return f"Time: {self.time}\nwinningDistance: {self.winningDistance}\n"


def read_input(input):
    races = {}

    for line in input:
        indentifier, y = line.split(":")
        y = y.strip().split()

        if (indentifier.startswith("Time")):
            indexCounter = 0
            # Join the list of strings into one string named time
            time = int("".join(y))
            race = Race(time)
            races[indexCounter] = race
            indexCounter += 1

        elif (indentifier.startswith("Distance")):
            indexCounter = 0
            record = int("".join(y))
            races[indexCounter].add_record(record)
            indexCounter += 1
    return races


class Speed():
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed

    def getDistanceByTime(self, time):
        return int(self.speed * time)

    def __repr__(self):
        return f"Speed: {self.speed}\n"


def getWinningPossibilities(race):
    winningPossibilities = []
    winningDistance = race.winningDistance

    timeLimit = int(race.time)

    hasEnteredWinningPossibilities = False

    for i in range(0, int(race.time)):
        speed = Speed()
        accTime = i
        drivingTime = timeLimit - accTime

        speed.set_speed(accTime)

        distance = speed.getDistanceByTime(drivingTime)
        if (int(distance) > int(winningDistance)):
            hasEnteredWinningPossibilities = True
            winningPossibilities.append(i)
            continue

        # Here, we know that the distance has become less that the winning distance
        if (hasEnteredWinningPossibilities):
            break

    return winningPossibilities


def run(input_data):
    races = read_input(input_data)
    totalWinPossibilities = []
    print(races)

    for i in range(0, len(races)):
        race = races[i]
        winPosCount = len(getWinningPossibilities(race))
        totalWinPossibilities.append(winPosCount)

    return prod(totalWinPossibilities)


print(run(input_data=input_data))
