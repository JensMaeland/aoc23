with open("input", "r") as file:
    input_data = file.read()

test_data = input_data.split("\n")
test_data = test_data[:10]

sum = 0
for line in input_data.split("\n"):
    num1 = 0
    num2 = 0
    print(line)
    for character in line:
        if character.isdigit():
            num1 = character
            break
    for character in reversed(line):
        if character.isdigit():
            num2 = character
            break
    if (num1 == 0 and num2 == 0):
        continue
    appendedSum = str(num1) + str(num2)
    print(f"Appended sum: {appendedSum}")
    sum += int(appendedSum)

print(f"Sum: {sum}")
