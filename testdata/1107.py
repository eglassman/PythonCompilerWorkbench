def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    step = 0
    display = ''
    while step < len(secretWord):
        if secretWord[step] not in lettersGuessed:
            display +=('_ ')
            
        else:
            display += secretWord[step]
        step+= 1
    
    return display
