# Steven Vi 74537668 Duy Lam 61502602 Lab 12 pm-1:50 pm Project 2
# Console Version

import connectfour

def new_game_state():
    '''New game state of ConnectFour'''
    return connectfour.new_game()

def userInput():
    ''' Play ConnectFour Console Version'''
    game_board = new_game_state()
    columns = connectfour.BOARD_COLUMNS
    print('It is currently RED\'s turn.')
    winner = winner_is_chosen(game_board)
    while winner == 0:
        try:
            userInput = input('Input what action you want first then number:\n').strip().lower()
            usercommand = userInput.split()
            if len(usercommand) == 2:
                if usercommand[0] == 'drop':
                    if 0 < int(usercommand[1]) <= columns:
                        game_board = drop_piece(game_board, int(usercommand[1])-1)
                        print_connectfour = print_board(game_board)
                        current_turn = _game_state_turn(game_board)
                        winner = winner_is_chosen(game_board)
                        if winner != 0:
                            print('Game is over.')
                            break
                    else:
                        print('The column number you specified is not correct. Try again.')
                        winner = 0
                elif usercommand[0] == 'pop':
                    if 0 < int(usercommand[1]) <= columns: 
                        game_board = pop_piece(game_board, int(usercommand[1])-1)
                        print_connectfour = print_board(game_board)
                        current_turn = _game_state_turn(game_board)
                        winner = winner_is_chosen(game_board)
                        if winner != 0:
                            print('Game is over.')
                            break
                    else:
                        print('The column number you specified is not correct. Try again.')
                        winner = 0
                else:
                    print('ERROR.')
                    winner = 0
            else:
                print('That\s not a correct move. Try again')
                winner = 0
        except connectfour.InvalidMoveError: 
            print('Action cannot be fulfilled. Try again.')
            winner = 0
        except ValueError:
            print('The second command is not correct. Try again')
            winner = 0
        except TypeError:
            print('The number you tried to input is a string.')
            winner = 0


            
def drop_piece(game_state: 'GameState', col_num: int):
    ''' Drops a piece in the game board and returns it'''
    new_state = connectfour.drop(game_state, col_num)
    return new_state

def pop_piece(game_state: 'GameState', col_num: int):
    ''' Pops a piece in the game board and returns it'''
    new_state = connectfour.pop(game_state, col_num)
    return new_state

def print_board(game_state):
    ''' Prints the board '''
    board_state = game_state.board
    columnNum = []
    board = []
    
    for i in range(0, connectfour.BOARD_COLUMNS):
        columnNum.append(i+1)
    board.append(columnNum)
    for i in range(0, connectfour.BOARD_ROWS):
        rowList = []
        for a in range(0, connectfour.BOARD_COLUMNS):
            rowList.append(board_state[a][i])
        board.append(rowList)
    for i in range(0, connectfour.BOARD_COLUMNS):
        print(board[0][i], end = ' ')
    print()
        
    converted = []
    for i in range(1, len(board)):
        row = []
        for a in range(0, len(board[i])):
            if board[i][a] == 0:
                row.append('.')
            elif board[i][a] == 1:
                row.append('R')
            elif board[i][a] == 2:
                row.append('Y')
        converted.append(row)
    for i in range(0, connectfour.BOARD_ROWS):
        for a in range(0, connectfour.BOARD_COLUMNS):
            print(converted[i][a] , end = ' ')
        print()
        

def winner_is_chosen(game_state):
    ''' Checks if the game board has a winner in it'''
    winner = connectfour.winner(game_state)
    if winner == connectfour.NONE:
        return winner
    else:
        return winner

def _game_state_turn(game_state: 'GameState'):
    ''' Checks whose turn is it.'''
    if winner_is_chosen(game_state) == connectfour.NONE:
        if game_state.turn == 1:
            print('It is Red\'s turn.')
        elif game_state.turn == 2:
            print('It is now Yellow\'s turn.')
    elif winner_is_chosen(game_state) != connectfour.NONE:
        if winner_is_chosen(game_state) == 1:
            print('Red is the winner.')
        elif winner_is_chosen(game_state) == 2:
            print('Yellow is the winner')

if __name__ == '__main__':
    userInput()
