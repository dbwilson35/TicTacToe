#board
board = {1: '_',2: '_',3: '_',
         4: '_',5: '_',6: '_',
         7: '_',8: '_',9: '_'}

#displayboard
def display_board():
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

game_running = True

#play game
def play_game():
    current_player = 1          #set player 1 as the current_player
    while game_running:
        display_board()         #disply the current board
        turn = input('Hello Player ' + str(current_player) + '. Please choose a spot that has not been chosen! (1-9)')      #request current player pick a square
        if int(turn) not in range(1,10):                                                                                     #if number is not between 1 and 9 then have player re-enter number
            print('That number is invalid. Please select a number 1 through 9')
            continue
        if board[int(turn)] != '_':                                                                     #if space has already been chosen have player choose new number
            print('That spot has already been chosen. Please select a different one.')
            continue
        if board[int(turn)] == '_':                                                                     #if space has not been chosen then
            if current_player == 1:
                board[int(turn)] = 'X'                                                                  #X for Player 1
            if current_player == 2:
                board[int(turn)] = 'O'                                                                  #O for Player 2
        if check_win(board) == True:
            print('Congratulations Player ' + str(current_player) + '! You are the winner!')            #Congratulate winning player
            display_board()                                                                             #Display board
            new_game()                                                                                  #Ask to play again?
            continue
        if check_tie(board) == True:
            print('Tie Game!')                                                                          #Oops Tie Game
            display_board()                                                                             #Display board
            new_game()                                                                                  #Ask to play again?
            continue
        current_player = next_player(current_player)                                                    #Change Player to next player (1 -> 2, 2 -> 1)
        continue


#switch players
def next_player(current_player):
    if current_player == 1:
        return 2
    if current_player == 2:
        return 1

#check win
def check_win(board):
    win =[                                          #List of win variations
          #row variations
          board[1] == board[2] == board[3] != '_',
          board[4] == board[5] == board[6] != '_',
          board[7] == board[8] == board[9] != '_',

          #column variations
          board[1] == board[4] == board[7] != '_',
          board[2] == board[5] == board[8] != '_',
          board[3] == board[6] == board[9] != '_',

          #diagonal variations
          board[1] == board[5] == board[9] != '_',
          board[3] == board[5] == board[7] != '_'
        ]
    return win.count(True) > 0                      #return True if any win variations are True.


#check tie
def check_tie(board):
    list_of_values = [value for value in board.values()]
    return list_of_values.count('_') == 0 and check_win(board) != True #return True if there are no blank spaces and no winner


#new game
def new_game():
    global game_running
    new_game = input('Would you like to play again? (Y/N)')
    if new_game == 'Y':                                       #If Y, reset the board and play again.
        reset_board(board)
    if new_game != 'Y':                                       #If anything other than Y, update game_running to False so the game stops
        game_running = False


#reset board for new_game
def reset_board(board):
    for a in board.keys():              #Reset the board so all values are '_'
        board[a] = '_'

play_game()
