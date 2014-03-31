def getGuessedWord(secretWord, lettersGuessed):
    str = ''  
    mem = False   
    for x in secretWord:
        mem = False
        for y in lettersGuessed:
            if x == y:
                str += x
                mem = True 
        if x != y and mem == False:
            str += '_'         
    return str
