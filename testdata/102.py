def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = ''
    for char in secretWord:
        found = False
        for lett in range(len(lettersGuessed)):
            if char == lettersGuessed[lett]:
                found = True
                break
        if found == True:
            output = output + char
        else:
            output = output + '_'
    return output
