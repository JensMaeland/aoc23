import os

cwd = os.getcwd()
print(f"CWD: {cwd}")

with open(f"{cwd}/2/input", "r") as file:
    input_data = file.read().split("\n")

test_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

totalRedCount = 12
totalGreenCount = 13
totalBlueCount = 14


def read_line(line):
    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    gameInfo, line = line.split(": ")
    gameId = int(gameInfo.split(" ")[1])
    redMaxCount = 0
    greenMaxCount = 0
    blueMaxCount = 0

    rounds = line.split("; ")
    for round in rounds:
        # "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        colors = round.split(", ")
        for color in colors:
            # "3 blue"
            currCount = getCount(color)
            currColor = getColor(color)
            if currColor == "red":
                redMaxCount = max(redMaxCount, currCount)
            elif currColor == "green":
                greenMaxCount = max(greenMaxCount, currCount)
            elif currColor == "blue":
                blueMaxCount = max(blueMaxCount, currCount)

    return gameId, redMaxCount, greenMaxCount, blueMaxCount


def getCount(input):
    return int(input.split(" ")[0])


def getColor(input):
    return input.split(" ")[1]


def run(data):
    idSum = 0
    for line in data:
        gameId, redCount, greenCount, blueCount = read_line(line)
        if redCount > totalRedCount or greenCount > totalGreenCount or blueCount > totalBlueCount:
            continue
        idSum += gameId
    print(idSum)


run(input_data)
