def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    afterGuess = '_' * len(secretWord)
    char = ' '
    result = ''
    for i in range(len(secretWord)) :
        if secretWord[i] in lettersGuessed :
           afterGuess = afterGuess[:i] + secretWord[i] + afterGuess[i+1:]
    for n in range(len(afterGuess)) :
        result = result + afterGuess[n] + char
    return result