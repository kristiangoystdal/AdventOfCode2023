
inputFile = open("Day3\input.txt", "r").readlines()

SYMBOLS = '1234567890.'

nums = []
tot=0


for n in range(len(inputFile)):
    if(n!=0):
        prevline=inputFile[n-1]
    else:
        prevline=""
    line = inputFile[n]
    if(n!=len(inputFile)-1):
        nextline=inputFile[n+1]
    else:
        nextline= ""
    
    lineList = [*line]
    prevList = [*prevline]
    nextList = [*nextline]
    if('\n' in prevList):
        prevList.remove('\n')
    if('\n' in lineList):
        lineList.remove('\n')
    if('\n' in nextList):
        nextList.remove('\n')
    
    i = 0
    while i < len(lineList):
        char = lineList[i]
        if(char.isdigit()):
            # print(char)
            try:
                if(i!=0):
                    if(prevList[i-1] not in SYMBOLS):
                        # print(prevList[i-1])
                        # print(char)
                        print("Prev-1")
                        tempI = i
                        numberString = lineList[i]
                        i+=1

                        while True:
                            if(lineList[i].isdigit()):
                                numberString += lineList[i]
                                i+=1
                            else:
                                break
                            
                        print(numberString)
                        
                    elif(prevList[i+1] not in SYMBOLS):
                        # print(prevList[i+1])
                        # print(char)
                        print("PRev+1")
                        tempI = i
                        numberString = lineList[i]
                        i+=1

                        while True:
                            if(lineList[i].isdigit()):
                                numberString += lineList[i]
                                i+=1
                            else:
                                break
                            
                        print(numberString)
                        
                    elif(prevList[i] not in SYMBOLS):
                        # print(prevList[i+1])
                        # print(char)
                        print("PRev")
                        tempI = i
                        numberString = lineList[i]
                        i+=1

                        while True:
                            if(lineList[i].isdigit()):
                                numberString += lineList[i]
                                i+=1
                            else:
                                break
                            
                        print(numberString)
                        
                if(i!=len(lineList)-1):                               
                    if(nextList[i-1] not in SYMBOLS):
                        # print(nextList[i-1])
                        # print(char)
                        print("Next-1")
                        tempI = i
                        numberString = lineList[i]
                        i+=1

                        while True:
                            if(lineList[i].isdigit()):
                                numberString += lineList[i]
                                i+=1
                            else:
                                break
                            
                        print(numberString)
                        
                    
                        
                    elif(nextList[i+1] not in SYMBOLS):
                        # print(nextList[i+1])
                        print("Next+1")
                        tempI = i
                        numberString = lineList[i]
                        i+=1

                        while True:
                            if(lineList[i].isdigit()):
                                numberString += lineList[i]
                                i+=1
                            else:
                                break
                            
                        print(numberString)
                    
                   
                    elif(nextList[i] not in SYMBOLS):
                        # print(nextList[i+1])
                        print("Next")
                        tempI = i
                        numberString = lineList[i]
                        i+=1

                        while True:
                            if(lineList[i].isdigit()):
                                numberString += lineList[i]
                                i+=1
                            else:
                                break
                            
                        print(numberString)
                        

            except:
                print("")
        
        
        i+=1

print("")
print("Total: " + str(tot))
            
            
    