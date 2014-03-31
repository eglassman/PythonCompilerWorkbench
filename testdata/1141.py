def  getGuessedWord(secretWord, lettersGuessed):
         resf = rest = 0
         target = ''
         for i in range(len(secretWord)):
              if secretWord[i] in  lettersGuessed:
                  target = target + secretWord[i]
              else:
                  target = target + '_ '
         return target
