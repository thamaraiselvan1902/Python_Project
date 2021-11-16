import random
def randomword():
    words = ['alarm', 'cupboard', 'broom', 'dustbin', 'roomfreshner', 'table', 'calender', 'pot',
             'photo', 'mirror', 'ironbox', 'scissors', 'lightbulb', 'fan', 'phone', 'tape', 'snacks']

    word = random.choice(words)
    return word

hang = ["""
H A N G M A N 

   +----+
   |    |  
   |   
   | 
   |    
   |    
  ========= """, """
H A N G M A N 

   +----+
   |    |  
   |    O
   | 
   |    
   |    
  =========""", """
H A N G M A N 

   +----+
   |    |  
   |    O
   |   / 
   |    
   |    
  =========""", """
H A N G M A N 

   +----+
   |    |  
   |   \O/
   |    
   |    
   |    
  =========""", """
H A N G M A N 

   +----+
   |    |  
   |   \O/
   |    |
   |    
   |    
  =========""", """
H A N G M A N 

   +----+
   |    |  
   |   \O/
   |    |
   |   /
   |    
  =========""", """
H A N G M A N 

   +----+
   |    |  
   |    O
   |   /|\ 
   |   //
   |    
  ========="""]


def Display(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Find the word :', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def Guess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    return input("\nDo you want to play again? ").upper().startswith('Y')


missedletters = ''
correctletters = ''
secretword = randomword()
gameover = False

while True:
    Display(hang, missedletters, correctletters, secretword)

    guess = Guess(missedletters + correctletters)

    if guess in secretword:
        correctletters = correctletters + guess

        foundAllLetters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secretword + '" You have won and saved an innocent!')
            gameover = True
    else:
        missedletters = missedletters + guess

        if len(missedletters) == len(hang) - 1:
            Display(hang, missedletters,
                         correctletters, secretword)
            print('You Killed an innocent!''\nYou have run out of guesses!\nAfter ' + str(len(missedletters)) + ' missed guesses and ' +
                  str(len(correctletters)) + ' correct guesses, the word was "' + secretword + '"')
            gameover = True

    if gameover:
        if playAgain():
            missedletters = ''
            correctletters = ''
            gameover = False
            secretword = randomword()
        else:
            break

