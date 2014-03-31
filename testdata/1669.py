def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
def getGuessedWord(secretWord, lettersGuessed):
	guessedWord = ''
	for s in secretWord:
		if s in lettersGuessed:
			guessedWord = guessedWord + s
		else:
			guessedWord = guessedWord + '_ '
	return guessedWord
