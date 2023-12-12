
inputFile = open("Day2\input.txt", "r")
colors= ["red", "blue", "green"]

orbDict = {
    "red": 12,
    "blue": 14,
    "green": 13
}

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

validGames= []
for line in inputFile:
    highestorbs=[0,0,0]
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
                    if(color=="red"):
                        if(highestorbs[0]<int(orbsColor[1])):
                            highestorbs[0]=int(orbsColor[1])
                    if(color=="blue"):
                        if(highestorbs[1]<int(orbsColor[1])):
                            highestorbs[1]=int(orbsColor[1])
                    if(color=="green"):
                        if(highestorbs[2]<int(orbsColor[1])):
                            highestorbs[2]=int(orbsColor[1])


    validGames.append(multiplyList(highestorbs))
    
print(sum(validGames))

            
            
    


