def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    lengthSW = len(secretWord)
    lengthLG = len(lettersGuessed)
    coRrect = [0]
    reSult = ['_ ']
    outPut = ''

    for i in range(lengthSW-1):
        coRrect.append(0)
        reSult.append('_') 
    
    j=0
    while j < lengthSW:
        jj = 0
        while jj < lengthLG:
            if secretWord[j] == lettersGuessed[jj]:
                coRrect[j] = 1
            jj = jj + 1
        j = j + 1
    
    for k in range(lengthSW):
        if coRrect[k] > 0:
           reSult[k] = secretWord[k]

    for l in range(lengthSW):
        outPut = outPut + reSult[l]
        
    return outPut
