def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    z = []
    for x in range(0,len(secretWord)):
        z.append('_ ')
        for y in range(0,len(lettersGuessed)):
            if secretWord[x]==lettersGuessed[y]:
                if x%2==0:
                    z[x-(x%2)] = lettersGuessed[y]
                else:
                    z[x-(x%2)+1] = lettersGuessed[y]
    z = "".join(z)
    return z