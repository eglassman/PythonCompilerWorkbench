def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    temp = ''
    for char in secretWord:
        if char in lettersGuessed:
            temp += char
        else:
            temp += '_'
    # add spaces between '_' characters
    lastchar = ''
    result = ''
    for char in temp:
        if char == '_':
            if lastchar != ' ':
                result += ' _ '
            else:
                result += '_ '
        else:
            result += char
        lastchar = char
    return result