# Steven Vi 74537668 Duy Lam 61502602 Lab 12 pm-1:50 pm Project 2
# Console Version

import connectfour

def new_game_state():
    return connectfour.new_game()

def userInput(game_state: 'GameState'):
    game_board = game_state
    columns = connectfour.BOARD_COLUMNS
##    winner = winner_is_chosen(game_board)
    try:
        while winner_is_chosen(game_board) == connectfour.NONE:
            userInput = input('Input what action you want first then number:\n').strip().lower()
            usercommand = userInput.split()
            if usercommand[0] == 'drop':
                if (columns >=  int(usercommand[1]) > 0):
                    game_board = drop_piece(game_board, int(usercommand[1])-1)
                    print_connectfour = print_board(game_board)
                    current_turn = _game_state_turn(game_board)
            elif usercommand[0] == 'pop':
                if 0 < int(usercommand[1]) <= columns: 
                    game_board = pop_piece(game_board, int(usercommand[1])-1)
                    print_connectfour = print_board(game_board)
                    current_turn = game_state_turn(game_board)
                else:
                    print('The column number you specified is not correct. Try again.')
            else:
                print('ERROR.')
                game_board = game_board
    except connectfour.InvalidMoveError: #This handles when the user is putting in full column or cannot pop at that spot
        print('Action connect be fulfilled. Try again.')
        game_board = userInput(game_board)
    except ValueError: #This handles the user input when they input the wrong thing.
        print('The second command is not correct. Try again')
        game_board = userInput(game_board)
    except TypeError:
        print('The number you tried to input is a string.')
        game_board = userInput(game_board)

    finally:
        print('Game is over.')

            
def drop_piece(game_state: 'GameState', col_num: int):
    new_state = connectfour.drop(game_state, col_num)
    return new_state

def pop_piece(game_state: 'GameState', col_num: int):
    new_state = connectfour.pop(game_state, col_num)
    return new_state

def print_board(game_state):
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
    winner = connectfour.winner(game_state)
    if winner == connectfour.NONE:
        return winner
    else:
        return winner

def _game_state_turn(game_state: 'GameState'):
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
    new_game = new_game_state()
    userInput(new_game)
