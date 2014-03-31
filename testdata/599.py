def getGuessedWord(secretWord, lettersGuessed): 
    i = 0 
    somestring = ''
    for letter in secretWord: 
        if letter in lettersGuessed: 
            somestring += letter + ' '
        else: 
            somestring += '_ '
    return somestring