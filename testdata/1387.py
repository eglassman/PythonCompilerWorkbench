def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    fin = ''
    if lettersGuessed == []:
        for x in range(len(secretWord)):
            fin += '_ '
    for count1 in range(len(secretWord)):
        let = secretWord[count1]
        for pos in range(len(lettersGuessed)):
            if let == lettersGuessed[pos]:
                fin=fin+let
                break
            elif pos == len(lettersGuessed)-1:
                fin +=('_ ')
    return fin