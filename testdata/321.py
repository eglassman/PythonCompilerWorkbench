def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # if the letter has been guessed add it to a blank string
    # if it hasn't add an underscore
    # Remember to return the String!!!
    guessed = ''
    length = 0
    for letter in secretWord:
        if letter in (lettersGuessed):
            guessed += letter
        else:
            guessed +='_'
    return guessed