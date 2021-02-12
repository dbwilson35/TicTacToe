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
            print('Congratulations PLayer ' + str(current_player) + '! You are the winner!')
            display_board()
            new_game()
            continue
        if check_tie(board) == True:
            print('Tie Game!')
            display_board()
            new_game()
            continue
        current_player = next_player(current_player)
        continue


#switch players
def next_player(current_player):
    if check_tie(board) == True or check_win(board) == True:
        return 1
    else:
        if current_player == 1:
            return 2
        if current_player == 2:
            return 1


def check_win(board): #giving it the import of board
    #check rows
    win =[board[1] == board[2] == board[3] != '_',
          board[4] == board[5] == board[6] != '_',
          board[7] == board[8] == board[9] != '_',
          board[1] == board[4] == board[7] != '_',
          board[2] == board[5] == board[8] != '_',
          board[3] == board[6] == board[9] != '_',
          board[1] == board[5] == board[9] != '_',
          board[3] == board[5] == board[7] != '_'
        ]
    return win.count(True) > 0

#check tie
def check_tie(board):
    list_of_values = []
    for value in board.values():
        list_of_values.append(value)
    if list_of_values.count('_') == 0 and check_win(board) != True:
        return True


def new_game():
    global game_running
    new_game = input('Would you like to play again? (Y/N)')
    if new_game == 'Y':
        reset_board(board)
    if new_game != 'Y':
        game_running = False

#reset board for new_game
def reset_board(board):
    for a, b in board.items():
        board[a] = '_'

play_game()
