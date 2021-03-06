import nltk

def readLecixonDictionary():
    with open("lexicon_dictionary.txt") as f:
        l = f.readlines()
        for i in l:
            l2 = i.split(' ', 1)
            l3 = l2[1].split()
            hashTable[l2[0]] = []
            hashTable[l2[0]].append(int(l3[0]))
            hashTable[l2[0]].append(int(l3[2]))
            hashTable[l2[0]].append(int(l3[4]))

def readTokenFile(fileName, token):
    tokenFile = open(fileName, "r")
    
    tokenFileContent = tokenFile.read().decode('utf-8')
    
    sentenceTokens = nltk.sent_tokenize(tokenFileContent)
    
    for i in sentenceTokens:
        
        sentenceVector = []
        if token == 0:
            sentenceVector = [3, 0, 0, 0]
        elif token == 1:
            sentenceVector = [0, 3, 0, 1]
        else:
            sentenceVector = [0, 0, 3, 2]
        
        wordTokens = nltk.word_tokenize(i)
        for j in wordTokens:
            if hashTable.has_key(j):
                for k in hashTable[j]:
                    sentenceVector[k] += hashTable[j][k]
        
        if token == 0:
            angryVectors.append(sentenceVector)
        elif token == 1:
            disgustVectors.append(sentenceVector)
        else:
            joyVectors.append(sentenceVector)

def writeVectorsToFile():
    f = open('featureVectorization.csv', 'w')
    maximumSize = max(len(angryVectors), len(disgustVectors), len(joyVectors))
    
    for i in range(maximumSize):
        if i < len(angryVectors):
            vectorLength = len(angryVectors[i])-1
            for j in range(vectorLength):
                f.write(str(angryVectors[i][j]))
                f.write(',')
            f.write(str(angryVectors[i][-1])+'\n')
        
        if i < len(disgustVectors):
            vectorLength = len(disgustVectors[i])-1
            for j in range(vectorLength):
                f.write(str(disgustVectors[i][j]))
                f.write(',')
            f.write(str(disgustVectors[i][-1])+'\n')
        
        if i < len(joyVectors):
            vectorLength = len(joyVectors[i])-1
            for j in range(vectorLength):
                f.write(str(joyVectors[i][j]))
                f.write(',')
            f.write(str(joyVectors[i][-1])+'\n')

hashTable = {}

readLecixonDictionary()

angryVectors = []
disgustVectors = []
joyVectors = []

readTokenFile("AngryToken.txt", 0)
readTokenFile("DisgustToken.txt", 1)
readTokenFile("joyToken.txt", 2)

writeVectorsToFile()

