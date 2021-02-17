class ttc_board:

    def __init__(self):
        self.board  = {1: '_',2: '_',3: '_',
                       4: '_',5: '_',6: '_',
                       7: '_',8: '_',9: '_'}


    def display(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])


    def check_win(self):
        win = [                                         # List of win variations
            # row variations
            self.board[1] == self.board[2] == self.board[3] != '_',
            self.board[4] == self.board[5] == self.board[6] != '_',
            self.board[7] == self.board[8] == self.board[9] != '_',

            # column variations
            self.board[1] == self.board[4] == self.board[7] != '_',
            self.board[2] == self.board[5] == self.board[8] != '_',
            self.board[3] == self.board[6] == self.board[9] != '_',

            # diagonal variations
            self.board[1] == self.board[5] == self.board[9] != '_',
            self.board[3] == self.board[5] == self.board[7] != '_'
        ]
        return win.count(True) > 0


    def check_tie(self):
        list_of_values = [value for value in self.board.values()]
        return list_of_values.count('_') == 0 and self.check_win() != True   # return True if there are no blank spaces and no winner


    def new_game(self):
        global game_running
        new_game = input('Would you like to play again? (Y/N)')
        if new_game == 'Y':
            self.__init__()
        if new_game != 'Y':  # If anything other than Y, update game_running to False so the game stops
            game_running = False


#next player
def next_player(current_player):
    if current_player == 1:
        return 2
    if current_player == 2:
        return 1


#Let's play the game!

game_running = True

def play_game():
    current_player = 1          #set player 1 as the current_player
    plank = ttc_board()         #variable named plank because naming it board might get confusing and a blank is another word for a board right??
    while game_running:
        plank.display()
        turn = input('Hello Player ' + str(current_player) + '. Please choose a spot that has not been chosen! (1-9)')      #request current player pick a square
        if int(turn) not in range(1,10):                                                                                     #if number is not between 1 and 9 then have player re-enter number
            print('That number is invalid. Please select a number 1 through 9')
            continue
        if plank.board[int(turn)] != '_':                                                                     #if space has already been chosen have player choose new number
            print('That spot has already been chosen. Please select a different one.')
            continue
        if plank.board[int(turn)] == '_':                                                                     # if space has not been chosen then
            if current_player == 1:
                plank.board[int(turn)] = 'X'                                                                  # X for Player 1
            if current_player == 2:
                plank.board[int(turn)] = 'O'                                                                  # O for Player 2
        if plank.check_win():
            print('Congratulations Player ' + str(current_player) + '! You are the winner!')                  # Congratulate winning player
            plank.display()                                                                                   # Display board
            plank.new_game()                                                                                  # Ask to play again?
            continue
        if plank.check_tie():
            print('Tie Game!')                                                                                #Oops Tie Game
            plank.display()                                                                                   #Display board
            plank.new_game()                                                                                  #Ask to play again?
            continue
        current_player = next_player(current_player)                                                    #Change Player to next player (1 -> 2, 2 -> 1)
        continue

play_game()
