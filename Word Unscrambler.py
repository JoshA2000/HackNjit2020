import enchant

wordList = []

def checkWord(cString):
    if englishDict.check(cString):
        return True
    else:
        return False
    
def unscrambler(cString, realWord):
    if not cString:
        if checkWord(realWord):
            return realWord
        else:
            return cString
    for letter in cString:
        if cString.index(letter) == 0:
            realWord += letter
            changedWord = cString[1:]
            newWord = unscrambler(changedWord, realWord)
        elif cString.index(letter) == len(cString) - 1:
            realWord += letter
            changedWord = cString[:len(cString) - 1]
            newWord = unscrambler(changedWord, realWord)
        else:
            realWord += letter
            changedWord = cString[:cString.find(letter)]  + cString[cString.find(letter) + 1:]
            newWord = unscrambler(changedWord,  realWord)
        if "*" not in realWord and realWord not in wordList:
            wordList.append(realWord)
            realWord = ""
        else:
            continue
    return wordList

englishDict = enchant.Dict("en_US")
scrambledWord = input("Enter some random letters ")
print(unscrambler(scrambledWord, ""))
