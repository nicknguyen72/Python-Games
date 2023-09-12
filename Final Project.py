game_choice = ''
end_game = False


while game_choice != 'Quit' and game_choice != 'quit':
    
    print ('\nThe games avaliable to choose from are Rock-Paper-Scissors, Hangman, and Tic-Tac-Toe')
    print ('To choose a game select the number that appears next to it')
    print ('If you want to learn how to play these games type 4')
    print ('\n*Type quit to exit the whole program')
    print ('\n1. Rock-Paper-Scissors\n2. Hangman\n3. Tic-Tac-Toe\n4. Instructions')
    game_choice = input('Choose which game you would like to play: ')
       
    try:
        game_choice = int(game_choice)
    except:
        if game_choice == 'quit' or game_choice == 'Quit':
            break
        else:
            print ('\n______________________________________________________________________________')
            print ('\n*Invalid input please try again')
            continue

########################### 1. Rock-Paper-Scissosrs ###########################

    if game_choice == 1:
        import random
        print ('______________________________________________________________________________')
        print ('\nYour options are rock, paper, or a scissors')
        player_choice = input('Choose your method of attack: ')
        player_score = 0
        computer_score = 0
        game_over = False
        
        if player_choice == 'Quit' or player_choice == 'quit':
            end_game = True
            
        while player_choice != 'stop' and player_choice != 'Stop' and player_choice != 'quit' and player_choice != 'Quit':
            if player_choice != 'Rock' and player_choice != 'rock' and player_choice != 'Paper' and player_choice != 'paper' and player_choice != 'Scissors' and player_choice != 'scissors': # If input is not valid keep asking until they put something that works  
                print ('______________________________________________________________________________')    
                print ('\n*Invalid input please try again')
                print ('\nYour options are rock, paper, or a scissors')
                player_choice = input('Choose your method of attack: ')
                continue
                
            computer_number = random.randint(0, 2) # Generates random number which turns into what the computer plays
            if computer_number == 0:
                computer_choice = 'Rock'
            elif computer_number == 1:
                computer_choice = 'Paper'
            elif computer_number == 2:
                computer_choice = 'Scissors'
                
            if player_choice == 'Rock' or player_choice == 'rock': # Finds out if the player lost or won depending on their choice versus the computer's choice
                if computer_choice == 'Rock':
                    print("""
    _______                                              _______    
---'   ____)                                            (____   '---
      (_____)          The computer chose Rock         (_____)      
      (_____)                                          (_____)      
      (____)                                            (____)      
---.__(___)                                              (___)__.---
        """)
                    print ('It\'s a tie'.center(71))
                if computer_choice == 'Paper':
                    print("""
    _______                                                 _______      
---'   ____)                                           ____(____    '---       
      (_____)          The computer chose Paper       (______ 
      (_____)                                         (______         
      (____)                                           (_______   
---.__(___)                                              (__________.---   
        """)
                    print ('You lose'.center(71))
                    computer_score += 1
                if computer_choice == 'Scissors':
                    print("""
    _______                                                   _______      
---'   ____)                                             ____(____    '---
      (_____)         The computer chose Scissors       (______          
      (_____)                                          (__________       
      (____)                                                 (____)      
---.__(___)                                                    (___)__.---
        """)
        
                    print ('You win'.center(71))
                    player_score += 1
            elif player_choice == 'Paper' or player_choice == 'paper':
                if computer_choice == 'Rock':
                    print("""
    ________                                         _______    
---'    ____)____                                   (____   '---
           ______)     The computer chose Rock     (_____)      
          _______)                                 (_____)      
         _______)                                   (____)      
---.__________)                                      (___)__.---
        """)
                    print ('You win'.center(71))
                    player_score += 1
                if computer_choice == 'Paper':
                    print("""
    ________                                               _______      
---'    ____)____                                     ____(____   '---       
           ______)     The computer chose Paper     (______ 
          _______)                                  (______         
         _______)                                    (_______   
---.__________)                                        (__________.---   
        """)
        
                    print ('It\'s a tie'.center(71))
                if computer_choice == 'Scissors':
                    print("""
    ________                                                _______      
---'    ____)____                                      ____(____   '---
           ______)    The computer chose Scissors     (______          
          _______)                                   (__________       
         _______)                                         (____)      
---.__________)                                             (___)__.---
        """)
                    print ('You lose'.center(71))
                    computer_score += 1
            elif player_choice == 'Scissors' or player_choice == 'scissors':
                if computer_choice == 'Rock':
                    print("""
    _______                                           _______    
---'   ____)____                                     (____   '---
          ______)       The computer chose Rock     (_____)      
       __________)                                  (_____)      
      (____)                                         (____)      
---.__(___)                                           (___)__.---
        """)
                    print ('You lose'.center(71))
                    computer_score += 1
                if computer_choice == 'Paper':
                    print("""
    _______                                                _______      
---'   ____)____                                      ____(____    '---
          ______)      The computer chose Paper     (______           
       __________)                                  (_______ 
      (____)                                         (_______ 
---.__(___)                                             (__________.---
        """)
                    print ('You win'.center(71))
                    player_score += 1
                if computer_choice == 'Scissors':
                    print("""
    _______                                                _______      
---'   ____)____                                      ____(____    '---
          ______)     The computer chose Scissors    (______          
       __________)                                  (__________       
      (____)                                              (____)      
---.__(___)                                                 (___)__.---
        """)
                    print ('It\'s a tie'.center(71))
        
            print ('Player points: {}                                          Computer points: {}'.format(player_score, computer_score)) # Outputting the score of the game
            print ('______________________________________________________________________________')
            print ('\n*Enter stop or Stop to end the game and go back to the menu\n*Enter quit to end the program')
            print ('\nYour options are rock, paper, or a scissors')
            player_choice = input('Choose your next method of attack: ')
            
            if player_choice == 'Quit' or player_choice == 'quit': # This is so that the player doesn't have to go through the first menu again when wanting to quit the whole program
                end_game = True
        
################################# 2. Hangman #################################
    
    elif game_choice == 2:
        clear = "\n" * 100 # To clear the board so that they can't see the word
        
        hangman_board = [
           [' _', '_', '_', '_', '_', '_', '_', '_'],
           [' |', '/', ' ', ' ', '  ', ' |'],
           [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['_', '|', '_', '_', '_', '_']
        ]
        
        print ('______________________________________________________________________________')
        word = input('Enter a word to be guessed: ').lower()
        letter_guess = ''
        lives = 6
        lose = False
        correct_amount = 0
        correct_letters = 0
        game_over = False
        
        if word == 'Quit' or word == 'quit': # Checking to see if the user wants to quit
            end_game = True
        elif word != 'stop' and word != 'Stop':
            print (clear)
        
        blank_space = []
        for i in range(len(word)): # Adding blank space depending on how long the word is
            blank_space += '-'
            correct_amount += 1
            
        letters_used = []
        while lives > 0 and letter_guess != 'stop' and letter_guess != 'Stop' and letter_guess != 'Quit' and letter_guess != 'quit' and word != 'Quit' and word != 'quit' and word != 'Stop' and word != 'stop':
            print (hangman_board[0][0] + hangman_board[0][1] + hangman_board[0][2] + hangman_board[0][3] + hangman_board[0][4] + hangman_board[0][5] + hangman_board[0][6] + hangman_board[0][7])
            print (hangman_board[1][0] + hangman_board[1][1] + hangman_board[1][2] + hangman_board[1][3] + hangman_board[1][4] + hangman_board[1][5])
            print (hangman_board[2][0] + hangman_board[2][1] + hangman_board[2][2] + hangman_board[2][3] + hangman_board[2][4] + hangman_board[2][5] + hangman_board[2][6] + hangman_board[2][7])
            print (hangman_board[3][0] + hangman_board[3][1] + hangman_board[3][2] + hangman_board[3][3] + hangman_board[3][4] + hangman_board[3][5] + hangman_board[3][6] + hangman_board[3][7] + hangman_board[3][8])
            print (hangman_board[4][0] + hangman_board[4][1] + hangman_board[4][2] + hangman_board[4][3] + hangman_board[4][4] + hangman_board[4][5] + hangman_board[4][6] + hangman_board[4][7] + hangman_board[4][8])
            print (hangman_board[5][0] + hangman_board[5][1] + hangman_board[5][2] + hangman_board[5][3] + hangman_board[5][4] + hangman_board[5][5])
            print ()
            if letters_used == []:
                print ('*Letters used: ')
            else:
                print ('*Letters used: ', end='')
                for letter in letters_used:
                    if letters_used.index(letter) == len(letters_used) - 1:
                        print (letter)
                    else:
                        print (letter, end=' ')
            print ()
            for spot in blank_space:
                if blank_space.index(spot) == len(blank_space):
                    print (spot)
                else:
                    print (spot, end=' ')
            print ('\n\n*Enter stop or Stop to end the game and go back to the menu\n*Enter quit to end the whole program\n*Enter \'retype\' to retype the word')
            letter_guess = input('Enter a letter to guess the word: ').lower()
        
            if letter_guess == 'Stop' or letter_guess == 'stop': # Seeing if the user put stopped, if did then stop game and go back to main menu
                break
            elif letter_guess == 'Quit' or letter_guess == 'quit': # If user put quit then quit everything
                end_game = True
                break
            elif letter_guess == 'retype': # Reset the whole game when this is selected
                word = input('Retype a word to be guessed (lowercase only): ').lower()
                print ('\n______________________________________________________________________________')
                blank_space = []
                correct_amount = 0
                correct_letters = 0
                for i in range(len(word)): # Adding blank space depending on how long the word is
                    blank_space += '-'
                    correct_amount += 1
                hangman_board = [
                   [' _', '_', '_', '_', '_', '_', '_', '_'],
                   [' |', '/', ' ', ' ', '  ', ' |'],
                   [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['_', '|', '_', '_', '_', '_']
                ]    
                letters_used = []
                lives = 6
                print (clear)
            elif len(letter_guess) == 1: # Making sure that what the user inputted into letter_guess is valid (not a number)
                valid_letter = True
                for letter in letters_used:
                    if letter_guess == letter: # Checking to see if that letter is already guessed
                        print ('\n______________________________________________________________________________')
                        print ('\n*{} has already been used or guessed'.format(letter_guess))
                        valid_letter = False
                        break
                    else:
                        valid_letter = True
                letter_position = []
                if valid_letter: # If the letter is not used yet then see if the letter is in the word
                    correct_guess = False
                    for i in range(len(word)):
                        if letter_guess == word[i]: # If the letter is in the word then grab position for later use
                            correct_guess = True
                            letter_position.append(i)
                    if correct_guess: # If they guessed correctly then change the blank space to that letter, otherwise they lose a life
                        for position in letter_position:
                            blank_space[position] = letter_guess
                            correct_letters += 1
                        letters_used.append(letter_guess)
                    else:
                        letters_used.append(letter_guess)
                        lives -= 1
                    print ('\n______________________________________________________________________________')
            else: # If the input is not valid then send here
                print ('\n______________________________________________________________________________')
                print ('\n*Invalid input please try again')
            
            if correct_amount == correct_letters:
                print (hangman_board[0][0] + hangman_board[0][1] + hangman_board[0][2] + hangman_board[0][3] + hangman_board[0][4] + hangman_board[0][5] + hangman_board[0][6] + hangman_board[0][7])
                print (hangman_board[1][0] + hangman_board[1][1] + hangman_board[1][2] + hangman_board[1][3] + hangman_board[1][4] + hangman_board[1][5])
                print (hangman_board[2][0] + hangman_board[2][1] + hangman_board[2][2] + hangman_board[2][3] + hangman_board[2][4] + hangman_board[2][5] + hangman_board[2][6] + hangman_board[2][7])
                print (hangman_board[3][0] + hangman_board[3][1] + hangman_board[3][2] + hangman_board[3][3] + hangman_board[3][4] + hangman_board[3][5] + hangman_board[3][6] + hangman_board[3][7] + hangman_board[3][8])
                print (hangman_board[4][0] + hangman_board[4][1] + hangman_board[4][2] + hangman_board[4][3] + hangman_board[4][4] + hangman_board[4][5] + hangman_board[4][6] + hangman_board[4][7] + hangman_board[4][8])
                print (hangman_board[5][0] + hangman_board[5][1] + hangman_board[5][2] + hangman_board[5][3] + hangman_board[5][4] + hangman_board[5][5])
                print ()
                if letters_used == []:
                    print ('Letters used: ')
                else:
                    print ('*Letters used: ', end='')
                    for letter in letters_used:
                        if letters_used.index(letter) == len(letters_used) - 1:
                            print (letter)
                        else:
                            print (letter, end=' ')
                print ()
                for spot in blank_space:
                    if blank_space.index(spot) == len(blank_space):
                        print (spot)
                    else:
                        print (spot, end=' ')
                print ('\n\nYOU WIN')
                print ('\nGAME OVER')
                print ('\n______________________________________________________________________________')
                game_over = True
            
            if lives == 5:
                hangman_board[2][7] = 'O'
            elif lives == 4:
                hangman_board[3][7] = '|'
            elif lives == 3:
                hangman_board[3][6] = '/'
            elif lives == 2:
                hangman_board[3][8] = '\\'
            elif lives == 1:
                hangman_board[4][6] = '/'
            elif lives == 0:
                hangman_board[4][8] = '\\'
                lose = True
            
            if lose:
                print (hangman_board[0][0] + hangman_board[0][1] + hangman_board[0][2] + hangman_board[0][3] + hangman_board[0][4] + hangman_board[0][5] + hangman_board[0][6] + hangman_board[0][7])
                print (hangman_board[1][0] + hangman_board[1][1] + hangman_board[1][2] + hangman_board[1][3] + hangman_board[1][4] + hangman_board[1][5])
                print (hangman_board[2][0] + hangman_board[2][1] + hangman_board[2][2] + hangman_board[2][3] + hangman_board[2][4] + hangman_board[2][5] + hangman_board[2][6] + hangman_board[2][7])
                print (hangman_board[3][0] + hangman_board[3][1] + hangman_board[3][2] + hangman_board[3][3] + hangman_board[3][4] + hangman_board[3][5] + hangman_board[3][6] + hangman_board[3][7] + hangman_board[3][8])
                print (hangman_board[4][0] + hangman_board[4][1] + hangman_board[4][2] + hangman_board[4][3] + hangman_board[4][4] + hangman_board[4][5] + hangman_board[4][6] + hangman_board[4][7] + hangman_board[4][8])
                print (hangman_board[5][0] + hangman_board[5][1] + hangman_board[5][2] + hangman_board[5][3] + hangman_board[5][4] + hangman_board[5][5])
                print ('\nThe word was \'{}\''.format(word))
                print ('\nYOU LOSE')
                game_over = True
                print ('\nGAME OVER')
                print ('\n______________________________________________________________________________')
            
            
            if game_over: # Retry menu of game
                valid_input = False
                while not(valid_input):
                    print ('\n*If you wish to continue the game enter \'Y\', if not then enter \'N\'\n*To exit the program completely enter quit')
                    retry = input('Do you wish to play again?: ')
                    if retry == 'Y' or retry == 'y':
                        word = input('Enter a new word to be guessed: ').lower()
                        print ('\n______________________________________________________________________________')
                        blank_space = []
                        correct_amount = 0
                        correct_letters = 0
                        for i in range(len(word)): # Adding blank space depending on how long the word is
                            blank_space += '-'
                            correct_amount += 1
                        hangman_board = [
                           [' _', '_', '_', '_', '_', '_', '_', '_'],
                           [' |', '/', ' ', ' ', '  ', ' |'],
                           [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' |', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           ['_', '|', '_', '_', '_', '_']
                        ]    
                        letters_used = []
                        lives = 6
                        valid_input = True
                        game_over = False
                        lose = False
                        print (clear)
                    elif retry == 'N' or retry == 'n':
                        letter_guess = 'stop'
                        break
                    elif retry == 'Quit' or retry == 'quit':
                        letter_guess = 'quit'
                        end_game = True
                        break
                    else:
                        print ('\n______________________________________________________________________________')
                        print ('\n*Invalid input please try again')

################################# 3. Tic-Tac-Toe #################################   

    elif game_choice == 3:
        game_over = False
        user_input = ''
        filled_spots = 0
        winner = ''
        player_turn = 'player x'
        gameboard = [
                [' ', '1', ' ', '2', ' ', '3'],
                ['A', ' ', '|', ' ', '|', ' '],
                [' ', '-', '+', '-', '+', '-'],
                ['B', ' ', '|', ' ', '|', ' '],
                [' ', '-', '+', '-', '+', '-'],
                ['C', ' ', '|', ' ', '|', ' ']
                ]
        print ('\n______________________________________________________________________________')
        while not(game_over) and user_input != 'stop' and user_input != 'Stop' and user_input != 'quit' and user_input != 'Quit':
            print ()
            print (gameboard[0][0], gameboard[0][1], gameboard[0][2], gameboard[0][3], gameboard[0][4], gameboard[0][5])
            print (gameboard[1][0], gameboard[1][1], gameboard[1][2], gameboard[1][3], gameboard[1][4], gameboard[1][5])
            print (gameboard[2][0], gameboard[2][1], gameboard[2][2], gameboard[2][3], gameboard[2][4], gameboard[2][5])
            print (gameboard[3][0], gameboard[3][1], gameboard[3][2], gameboard[3][3], gameboard[3][4], gameboard[3][5])
            print (gameboard[4][0], gameboard[4][1], gameboard[4][2], gameboard[4][3], gameboard[4][4], gameboard[4][5])
            print (gameboard[5][0], gameboard[5][1], gameboard[5][2], gameboard[5][3], gameboard[5][4], gameboard[5][5])
            print ('\n*Enter stop or Stop to end the game and go back to the menu\n*Enter quit to end the whole program')
            print ('\nEnter the row first then column (letter)(number)')
            valid_input = True
            if player_turn == 'player x':
                user_input = input('Enter where you want to place an X: ')
            elif player_turn == 'player o':
                user_input = input('Enter where you want to place an O: ')
            if user_input == 'stop' or user_input == 'Stop':
                break
            elif user_input == 'quit' or user_input == 'Quit':
                end_game = True
                break
            elif len(user_input) == 2:
                print ('\n______________________________________________________________________________')
                if user_input[0] == 'a' or user_input[0] == 'A':
                    row = 1
                elif user_input[0] == 'b' or user_input[0] == 'B':
                    row = 3
                elif user_input[0] == 'c' or user_input[0] == 'C':
                    row = 5
                else:
                    print ('\n*Invalid input for the row')
                    valid_input = False
                if user_input[1] == '1':
                    col = 1
                elif user_input[1] == '2':
                    col = 3
                elif user_input[1] == '3':
                    col = 5
                else:
                    print ('\n*Invalid input for the column')
                    valid_input = False
                if valid_input:
                    if gameboard[row][col] == ' ':
                        if player_turn == 'player x':
                            gameboard[row][col] = 'X'
                            player_turn = 'player o'
                        elif player_turn == 'player o':
                            gameboard[row][col] = 'O'
                            player_turn = 'player x'
                        filled_spots += 1
                    else:
                        print ('\n*Spot {} is already taken'.format(user_input))
            else:
                print ('\n______________________________________________________________________________')
                print ('\n*Invalid input length')
            
            if gameboard[1][1] == gameboard[1][3] == gameboard[1][5] == 'X' or gameboard[3][1] == gameboard[3][3] == gameboard[3][5] == 'X' or gameboard[5][1] == gameboard[5][3] == gameboard[5][5] == 'X': # Checking to see if they match horizontally
                winner = 'X'
                game_over = True
            elif gameboard[1][1] == gameboard[3][1] == gameboard[5][1] == 'X' or gameboard[1][3] == gameboard[3][3] == gameboard[5][3] == 'X' or gameboard[1][5] == gameboard[3][5] == gameboard[5][5] == 'X': # Checking to see if they match vertically
                winner = 'X'
                game_over = True
            elif gameboard[1][1] == gameboard[3][3] == gameboard[5][5] == 'X' or gameboard[5][1] == gameboard[3][3] == gameboard[1][5] == 'X': # Checking to see if they match diagonally
                winner = 'X'
                game_over 
            elif gameboard[1][1] == gameboard[1][3] == gameboard[1][5] == 'O' or gameboard[3][1] == gameboard[3][3] == gameboard[3][5] == 'O' or gameboard[5][1] == gameboard[5][3] == gameboard[5][5] == 'O':
                winner = 'O'
                game_over = True
            elif gameboard[1][1] == gameboard[3][1] == gameboard[5][1] == 'O' or gameboard[1][3] == gameboard[3][3] == gameboard[5][3] == 'O' or gameboard[1][5] == gameboard[3][5] == gameboard[5][5] == 'O':
                winner = 'O'
            elif gameboard[1][1] == gameboard[3][3] == gameboard[5][5] == 'O' or gameboard[5][1] == gameboard[3][3] == gameboard[1][5] == 'O':
                winner = 'O'
            elif filled_spots == 9:
                winner = 'tie'
                
            if winner != '': # Retry menu of game
                game_over = True
                valid_input = False
                print ()
                print (gameboard[0][0], gameboard[0][1], gameboard[0][2], gameboard[0][3], gameboard[0][4], gameboard[0][5])
                print (gameboard[1][0], gameboard[1][1], gameboard[1][2], gameboard[1][3], gameboard[1][4], gameboard[1][5])
                print (gameboard[2][0], gameboard[2][1], gameboard[2][2], gameboard[2][3], gameboard[2][4], gameboard[2][5])
                print (gameboard[3][0], gameboard[3][1], gameboard[3][2], gameboard[3][3], gameboard[3][4], gameboard[3][5])
                print (gameboard[4][0], gameboard[4][1], gameboard[4][2], gameboard[4][3], gameboard[4][4], gameboard[4][5])
                print (gameboard[5][0], gameboard[5][1], gameboard[5][2], gameboard[5][3], gameboard[5][4], gameboard[5][5])
                if winner == 'tie':
                    print ('\nGAME TIE')
                else:
                    print ('\nPlayer {} WINS!'.format(winner))
                while not(valid_input):
                    print ('\n*If you wish to continue the game enter \'Y\', if not then enter \'N\'\n*To exit the program completely enter quit')
                    retry = input('Do you wish to play again?: ')
                    if retry == 'Y' or retry == 'y':
                        game_over = False
                        user_input = ''
                        filled_spots = 0
                        player_turn = 'player x'
                        winner = ''
                        gameboard = [
                            [' ', '1', ' ', '2', ' ', '3'],
                            ['A', ' ', '|', ' ', '|', ' '],
                            [' ', '-', '+', '-', '+', '-'],
                            ['B', ' ', '|', ' ', '|', ' '],
                            [' ', '-', '+', '-', '+', '-'],
                            ['C', ' ', '|', ' ', '|', ' ']
                            ]
                        print ('\n______________________________________________________________________________')
                        break
                    elif retry == 'N' or retry == 'n':
                        break
                    elif retry == 'Quit' or retry == 'quit':
                        word = 'quit'
                        end_game = True
                        break
                    else:
                        print ('\n______________________________________________________________________________')
                        print ('\n*Invalid input please try again')
                        
################################# 4. Instructions #################################                
    
    elif game_choice == 4:
        instruction_choice = 0
        while instruction_choice != 'back' or instruction_choice != 'Back':
            print ('\n______________________________________________________________________________')  
            print ('\nSelect what game you would like to learn about')
            print ('\n*Type back to return to the home screen')
            print ('\n1. Rock-Paper-Scissors\n2. Hangman\n3. Tic-Tac-Toe')
            instruction_choice = input('Which game would you like to learn about: ')
            try:
                instruction_choice = int(instruction_choice)
                print ('\n______________________________________________________________________________')
                if instruction_choice == 1:
                    print ('\nHow to play Rock-Paper-Scissors:\n\nThe user goes against a \'computer\' that randomly generates a option to go against the user.\nTo play type in either rock, paper, or scissors into the console.')
                elif instruction_choice == 2:
                    print ('\nHow to play Hangman:\n\nHangman is a two player game where the first player inputs a random word for the second player to guess.')
                    print ('Make sure to only input the word in all lowercase because the second player has to guess the EXACT letter.')
                    print ('The second user has 6 tries to guess what the word is before the \'hangman\' is created.')
                    print ('To play keep inputing specifically lowercase letters into the console until the word is gussed or the game is over.')
                elif instruction_choice == 3:
                    print ('\nHow to play Tic-Tac-Toe:\n\nTic-Tac-Toe is a two player game where one player is represented by X and the other by O.\nEach player takes turn putting their symbol on the board until either one player gets 3 in a row or the board is filled, which will result in a tie.')
                    print ('To play each player types an input with the row first and the column second.')
                    print ('\n*Your input should look like this (letter / row)(number / column), i.e. a1 or b3')
                else:
                    print ('\n*Invalid input please try again')
            except:
                if instruction_choice == 'back' or instruction_choice == 'Back':
                    break
                print ('\n______________________________________________________________________________')
                print ('\n*Invalid input please try again')

################################# Invalid Input #################################  

    else:
        print ('\n______________________________________________________________________________')  
        print ('\n*Invalid input please try again')  
          
    if end_game or game_choice == 'quit' or game_choice == 'Quit':
        break
    
    print ('\n______________________________________________________________________________')
    
print ('\n______________________________________________________________________________')
print ('\nThanks for playing!')

    
    