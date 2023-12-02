# pylint: disable-all

with open("input", "r") as file:
    input_data = file.read()

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

reversedNumbers = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
    "orez": 0
}


def getFirstNumber(input):
    lowestIndex = 99999
    firstNumber = 99999

    # Find the first named number
    for namedNumber in numbers.keys():
        if namedNumber in input:
            index = input.index(namedNumber)
            if index < lowestIndex:
                lowestIndex = index
                firstNumber = numbers[namedNumber]

    # Find the first digit, use if index is lower than lowest named digit
    digitIndex = 0
    for character in input:
        if character.isdigit():
            if digitIndex < lowestIndex:
                firstNumber = character
            break
        digitIndex += 1

    # If no numbers are found
    if firstNumber == 99999:
        return 0

    return firstNumber


def getReversedFirstNumber(input):
    # The same as above, just reversed the named numbers
    lowestIndex = 99999
    firstNumber = 99999

    for namedNumber in reversedNumbers.keys():
        if namedNumber in input:
            index = input.index(namedNumber)
            if index < lowestIndex:
                lowestIndex = index
                firstNumber = reversedNumbers[namedNumber]

    digitIndex = 0
    for character in input:
        if character.isdigit():
            if digitIndex < lowestIndex:
                firstNumber = character
            break
        digitIndex += 1

    if firstNumber == 99999:
        return 0

    return firstNumber


def run():
    sum = 0
    for line in input_data.split("\n"):
        print(line)
        num1 = getFirstNumber(line)
        print(f"First number: {num1}")
        num2 = getReversedFirstNumber(line[::-1])
        print(f"Last number: {num2}")
        if (num1 == 0 and num2 == 0):
            continue
        appendedSum = str(num1) + str(num2)
        sum += int(appendedSum)
        print()

    print(f"Sum: {sum}")


run()
