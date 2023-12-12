inputFile = open("Day1\input.txt", "r").read()
# inputFile = open("Day1\example.txt", "r").read()

nums = []

firstInt = "a"
lastInt = "a"

numInts = 0
for char in inputFile:
    if char.isdigit():
        numInts += 1
        if firstInt == "a":
            firstInt = char
        else:
            lastInt = char
    if char == "\n":
        if numInts == 1:
            number = firstInt + firstInt
        else:
            number = firstInt + lastInt
        nums.append(int(number))
        firstInt = "a"
        lastInt = "a"
        numInts = 0

if numInts == 1:
    number = firstInt + firstInt
else:
    number = firstInt + lastInt
nums.append(int(number))

print(sum(nums))
