def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    rest =''
    
    for i in range(len(secretWord)):
        rest = rest + '_'
    for c in lettersGuessed:
        if c in secretWord:
            for index in range(len(secretWord)):
                if secretWord[index] == c:
                    rest = rest[:index]+c+rest[index+1:]
    return rest
