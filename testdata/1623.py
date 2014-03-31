def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word=secretWord
    wordlen=len(word)
    guess=''
    truecount=0
    falsecount=0
    countletter=0
    for letter in word:
        countletter +=1
        if letter in lettersGuessed:
            truecount +=1
            guess=guess+letter
        else:
            falsecount +=1
            guess=guess+'_ '
    return guess
