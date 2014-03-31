def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    newWord = ''
    for l in secretWord :
        if l in lettersGuessed:
            newWord += l + ' '
        else :
            newWord += '_ '
        
    return newWord
