def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x=len(secretWord)
    y=len(lettersGuessed)
    s=secretWord
    count=0
    for i in range(x):
        for j in range(y):
            if secretWord[i]==lettersGuessed[j]:
               count+=1 
               s=s.replace(s[i],s[i])
               break
        if count!=(i+1):
            s=s.replace(s[i],'_')
        count=(i+1)    
    return s        
   
        