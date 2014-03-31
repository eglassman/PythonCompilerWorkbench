def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    state_of_word = ""

    for char in secretWord:
        if char in lettersGuessed:
            state_of_word = state_of_word + char
        else:
            state_of_word = state_of_word + "_"

    return state_of_word