def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output=''
    c=0
    while c<len(secretWord):
        if secretWord[c] in lettersGuessed:
            output+=secretWord[c]
        else:
            output+='_'
        if c<len(secretWord):
            output+=' '
        c+=1
    return output