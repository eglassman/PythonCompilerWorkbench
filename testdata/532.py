def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    partwd = ''
    for n in secretWord:
        if n in lettersGuessed:
            partwd+=n
        else:
            partwd+='_'

    return partwd
