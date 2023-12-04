# pylint: disable-all
import os

cwd = os.getcwd()

with open(f"{cwd}/4/input", "r") as file:
    input_data = file.read().split("\n")

test_data = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


class Game:
    def __init__(self, cardId, winningNumbers, myNumbers):
        self.cardId = cardId
        self.winningNumbers = winningNumbers
        self.myNumbers = myNumbers

    def __repr__(self):
        return f"CardId: {self.cardId}\n WinningNumbers: {self.winningNumbers}\n MyNumbers:      {self.myNumbers}\n\n"


def getInformation(line):
    left, right = line.split(" | ")
    cardIdentifier, winningNumbersString = left.split(":")
    cardId = cardIdentifier.split()[1]
    winningNumbers = winningNumbersString.strip().split()
    myNumbers = right.split()
    winningNumbers.sort(key=lambda x: int(x))
    myNumbers.sort(key=lambda x: int(x))
    game = Game(cardId, winningNumbers, myNumbers)

    return game


def getPoints(game):
    points = []
    sum = 0

    for winningNumber in game.winningNumbers:
        if winningNumber in game.myNumbers:
            points.append(1)

    if len(points) == 0:
        return 0

    for point in points:
        sum += 1

    return sum


def run(input):
    gameCount = 0
    games = []
    initialGames = ["fill"]

    for line in input:
        game = getInformation(line)
        games.append(game)
        initialGames.append(game)

    while (len(games) != 0):
        sum = 0
        game = games.pop(0)
        gameId = int(game.cardId)
        sum += getPoints(game)
        for i in range(gameId, gameId + sum):
            games.append(initialGames[i+1])
        gameCount += 1

    return gameCount


# print(run(test_data))

print(run(input_data))

# print(getPoints(getInformation(test_data[5])))
