def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")

    divider = "-" * 13
    guesses = 8
    lettersGuessed = ""
    while guesses > 0 and not(isWordGuessed(secretWord, lettersGuessed)):
        print(divider)
        
        print(f"You have {guesses} guesses left.")
        printf("Available letters:", getAvailableLetters(lettersGuessed))
        guessed = input("Please guess a letter: ")

        if guessed in lettersGuessed:
          print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif guessed in secretWord:
          lettersGuessed += guessed
          print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
          lettersGuessed += guessed
          guesses -= 1
          print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))

    print(divider)
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secretWord}.")
