def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ()
    st = ''
    for c in secretWord:
         if lettersGuessed.count(c) == 0:
             result = result + ('_',)
         else:
             result = result + (c,)
    return st.join(result)