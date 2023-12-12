inputFile = open("Day1\input.txt", "r")
# inputFile = open("Day1\example2.txt", "r")

nums = []

numberStrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberInts = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


firstInt = "a"
lastInt = ""

numInts = 0
word = ""
for line in inputFile:
    lineNums = []
    for num in numberStrings:
        if num in line:
            lineNums.append(num)
    for char in line:
        word += char
        if char in numberInts:
            numInts += 1
            if firstInt == "a":
                firstInt = char
            else:
                lastInt = char
            word = ""
        else:
            for num in lineNums:
                if num in word:
                    numInts += 1
                    if firstInt == "a":
                        firstInt = numDict[num]
                    else:
                        lastInt = numDict[num]
                    clear = True
                    while clear:
                        for num1 in lineNums:
                            if num1 in word:
                                while num1 in word:
                                    word = word[1:]
                        break
    if numInts == 1:
        number = firstInt + firstInt
    else:
        number = firstInt + lastInt
    nums.append(int(number))
    firstInt = "a"
    word = ""
    numInts = 0

print(sum(nums))
