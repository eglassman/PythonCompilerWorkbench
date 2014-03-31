def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    guessedWord = list(secretWord)
    remainingLetters = set(secretWord) - (set(secretWord) & set(lettersGuessed))
    
    for letter in remainingLetters:
        for n in range(len(list(secretWord))):
            if letter == list(secretWord)[n]:
                guessedWord.pop(n)
                guessedWord.insert(n, "_")

    return ''.join(guessedWord)