# pylint: disable-all

import os
import random


def getOccurencesOfSymbols(input):
    symbols = []
    for line in input:
        for char in line:
            if char not in symbols:
                symbols.append(char)
    symbols.sort()
    return symbols


cwd = os.getcwd()

with open(f"{cwd}/3/input", "r") as file:
    input_data = file.read().split("\n")

test_data = [
    "467..114..",
    "...*......",
    "..35...633",
    ".......#..",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]
symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']
maxLength = 140
testMaxLength = 10


class Number:
    def __init__(self, value, startIndex, endIndex, lineNumber):
        self.value = int(value)
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.lineNumber = lineNumber

    def __repr__(self):
        return f"Value: {self.value}\n startIndex: {self.startIndex}\n endIndex: {self.endIndex}\n\n"


class Triplet:
    def __init__(self, prevLine, currLine, nextLine):
        self.prevLine = prevLine
        self.currLine = currLine
        self.nextLine = nextLine

    def __repr__(self):
        return f"PrevLine: {self.prevLine}\n currLine: {self.currLine}\n nextLine: {self.nextLine}\n\n"


class Gear:
    def __init__(self, lineIndex, linePos):
        self.lineIndex = lineIndex
        self.linePos = linePos
    adjacentNumbers = []

    def __repr__(self):
        return f"lineIndex: {self.lineIndex}\nlinePos: {self.linePos}"


def getNumbersInLine(line, lineNumber):
    skipCount = 0
    numbersInLine = []

    # Stop searching while we are in a number
    for i in range(0, len(line)):
        char = line[i]
        if (skipCount > 0):
            skipCount -= 1
            continue

        if char.isdigit():
            startIndex = i
            intsInNumber = []
            intsInNumber.append(char)
            skipCount = 1
            # ints after first digit
            for j in range(i+1, len(line)):
                # We are still in the number
                if line[j].isdigit():
                    intsInNumber.append(line[j])
                    skipCount += 1
                    if (j == len(line)-1):
                        currNumber = Number(
                            value=int("".join(intsInNumber)),
                            startIndex=startIndex, endIndex=j,
                            lineNumber=lineNumber
                        )
                        numbersInLine.append(currNumber)

                else:
                    currNumber = Number(
                        int("".join(intsInNumber)), startIndex, j-1)
                    numbersInLine.append(currNumber)
                    break
    return numbersInLine

def getTriplet(number, prevLine, currLine, nextLine):
    lineLength = len(currLine)

    indexFrom = number.startIndex
    indexTo = number.endIndex

    adjustedIndexFrom = indexFrom - 1
    adjustedIndexTo = indexTo + 1

    if (indexFrom == 0):
        adjustedIndexFrom = indexFrom

    if (indexTo == lineLength - 1):
        adjustedIndexTo = indexTo

    prev = prevLine[adjustedIndexFrom:adjustedIndexTo+1]
    curr = currLine[adjustedIndexFrom] + currLine[adjustedIndexTo]
    next = nextLine[adjustedIndexFrom:adjustedIndexTo+1]
    return Triplet(prev, curr, next)

def isAdjacentToGear(number, triplet):
    
    return gear

def lineLength(line):
    return len(line)

def run(input):

    maxLength = lineLength(input[0])
    inputLength = len(input)

    allNumbers = []

    # Legger til padding for å unngå out of bounds
    input.insert(0, "." * maxLength)
    input.append("." * maxLength)
    for i in range(1, len(input)-1):
        line = input[i]
        prevLine = input[i-1]
        currLine = line
        nextLine = input[i+1]
        numbersInLine = getNumbersInLine(line, i)
        for number in numbersInLine:
            allNumbers.append(number)

    for number in allNumbers:
        

# "467..114..",
# "...*......",
# "..35...633",
# ".......#..",
# "617*......",
# ".....+.58.",
# "..592.....",
# "......755.",
# "...$.*....",
# ".664.598.."
