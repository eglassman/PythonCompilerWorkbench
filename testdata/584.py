def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    index = 0
    word = '_'*len(secretWord) 
    word_list = list(word)
    for letter in secretWord:
        test = secretWord[index] in lettersGuessed
        if test == True:
            word_list[index] = secretWord[index]
            index += 1
        else:
            index +=1
    result = ' '.join(word_list) #There is a space between the strings so joins every item in list with space in between
    return result 
