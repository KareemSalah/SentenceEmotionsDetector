import nltk

class FeatureVectorizer:
    hashTable = {}
    angryVectors = []
    disgustVectors = []
    joyVectors = []
    
    def __init__(self):
        pass

    def readLecixonDictionary(self):
        with open("lexicon_dictionary.txt") as f:
            l = f.readlines()
            for i in l:
                l2 = i.split(' ', 1)
                l3 = l2[1].split()
                self.hashTable[l2[0]] = []
                self.hashTable[l2[0]].append(int(l3[0]))
                self.hashTable[l2[0]].append(int(l3[2]))
                self.hashTable[l2[0]].append(int(l3[4]))

    def readTokenFile(self, fileName, token):
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
                if self.hashTable.has_key(j):
                    for k in self.hashTable[j]:
                        sentenceVector[k] += self.hashTable[j][k]

            if token == 0:
                self.angryVectors.append(sentenceVector)
            elif token == 1:
                self.disgustVectors.append(sentenceVector)
            else:
                self.joyVectors.append(sentenceVector)

    def writeVectorsToFile(self):
        f = open('featureVectorization.csv', 'w')
        maximumSize = max(len(self.angryVectors), len(self.disgustVectors), len(self.joyVectors))

        for i in range(maximumSize):
            if i < len(self.angryVectors):
                vectorLengthMinusOne = len(self.angryVectors[i])-1
                for j in range(vectorLengthMinusOne):
                    f.write(str(self.angryVectors[i][j]))
                    f.write(',')
                f.write(str(self.angryVectors[i][-1])+'\n')
            if i < len(self.disgustVectors):
                vectorLengthMinusOne = len(self.disgustVectors[i])-1
                for j in range(vectorLengthMinusOne):
                    f.write(str(self.disgustVectors[i][j]))
                    f.write(',')
                f.write(str(self.disgustVectors[i][-1])+'\n')
            if i < len(self.joyVectors):
                vectorLengthMinusOne = len(self.joyVectors[i])-1
                for j in range(vectorLengthMinusOne):
                    f.write(str(self.joyVectors[i][j]))
                    f.write(',')
                f.write(str(self.joyVectors[i][-1])+'\n')
    
    def vectorize(self, sentences):
        listOfVectors = []
        
        for i in sentences:
            sentenceVector = []

            wordTokens = nltk.word_tokenize(i)
            for j in wordTokens:
                if self.hashTable.has_key(j):
                    for k in self.hashTable[j]:
                        sentenceVector[k] += self.hashTable[j][k]
            listOfVectors.append(sentenceVector)
            
        return listOfVectors

    def start(self, mode='train', text=None):
        self.readLecixonDictionary()

        if mode == 'train':

            self.readTokenFile("AngryToken.txt", 0)
            self.readTokenFile("DisgustToken.txt", 1)
            self.readTokenFile("joyToken.txt", 2)

            self.writeVectorsToFile()
        else:
            sentences = nltk.sent_tokenize(text)
            return self.vectorize(sentences)
