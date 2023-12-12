
inputFile = open("Day2\input.txt", "r")
colors= ["red", "blue", "green"]

orbDict = {
    "red": 12,
    "blue": 14,
    "green": 13
}

validGames= []
for line in inputFile:
    lineList = line.split(":")
    gameID = int(lineList[0].split(" ")[1])
    
    turns = lineList[1].split(";")
    
    valid = True
    for i in range(len(turns)):
        orbs = turns[i].split(",")
        for j in range(len(orbs)):
            orbsColor = orbs[j].split(" ")
            for color in colors:
                if (color in orbsColor[2]):
                    if (orbDict[color]<int(orbsColor[1])):
                        valid = False
                        
    if(valid):
        validGames.append(gameID)
            
print(sum(validGames))
            
    


