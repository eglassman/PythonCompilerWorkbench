def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    sol = ""
    for elem in secretWord:
        if elem not in lettersGuessed:
            sol += '_'
        else:
            sol += elem
    return sol