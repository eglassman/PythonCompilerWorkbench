def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    letter = 0
    guess_letters=0
    print_out=''
    bukva=0



    for bukva in range(len(secretWord)):
        for letter_guess_no in range(len(lettersGuessed)):
            if secretWord[bukva]==lettersGuessed[letter_guess_no]:
                print_out+=lettersGuessed[letter_guess_no]
                break
            else:
                if letter_guess_no==(len(lettersGuessed))-1:
                    print_out+='_'
                    break
                else:
                    letter_guess_no+=1
 
     
    bukva=+1
    return print_out