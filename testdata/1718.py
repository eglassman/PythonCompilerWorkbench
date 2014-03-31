def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result=""
    for st in secretWord:
        inSecret=st in lettersGuessed
        if inSecret==False:
            result+="_ "
        else:
             result+=st   
    return result