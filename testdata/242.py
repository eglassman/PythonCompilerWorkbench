def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    final=''
    lp=len(secretWord)
    for i in range(0,lp):
        if lettersGuessed.count(secretWord[i])==0:
            final+=' _ '
        else:
            final+= secretWord[i]
    return final