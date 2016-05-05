import connectfour

rows = connectfour.BOARD_ROWS
columns = connectfour.BOARD_COLUMNS
new_board = connectfour.new_game()

def userInput():
##    game_board = new_board
##    while winner_is_chosen(game_board) == False:
    userInput = input('Please choose which column number from 1-7:\n').strip().lower()
    usercommand = userInput.split()
    if usercommand[0] == 'drop':
        pieces_drop = drop_piece(int(usercommand[1]) - 1)
        game_board = print_board(pieces_drop)
    elif usercommand[0] == 'pop':
        pop_piece(int(usercommand[1]) - 1)
    else:
        pass
            
def drop_piece(col_num: int):
    new_state = connectfour.drop(new_board, col_num)
    return new_state

def pop_piece(col_num: int):
    new_state = connectfour.pop(new_board, col_num)
    return pop_piece

def print_board(game_state):
    # this function will format the board later on
    print(game_state.board)
    board_state = game_state.board
    count = []
    board = []
    print('\n')
    
    columnNum = []
    for i in range(0, columns):
        columnNum.append(i+1)
    board.append(columnNum)          
    for i in range(0, rows):
        rowList = []
        for a in range(0, columns):
            rowList.append(board_state[a][i])
        board.append(rowList)
        #print(board[i])
        
    for i in range (0, columns):
        print(board[i])
        
    
    '''
    for i in range(0, columns):
        count.append(i+1)
    for item in count:
        print(item, end =' ')
    print('\n')
    #print(type(board_state))
    
    for column in board_state:
        integer = 0
        board_state[integer][0]
        print(board_state[0][len(board_state[0])-1])
        for element in column:
            
            if element == 0:
                #board[integer] = ( '.') board[integer].insert('.')
                #row.replace(0, '.')
                print(row, end = ' ')
                #print('.', end = ' ')
            elif element == 1:
                #board[integer] = 'R' #board[integer].insert('R')
                print('R', end = ' ')
            elif element == 2:
                #board[integer] = 'Y'#board[integer].insert('Y')
                print('Y', end = ' ')
            else:
                pass
        integer += 1
        print ('\n')
    for item in board:
        print(item)
           ''' 
    
            
    # Will return the board
    return game_state
def winner_is_chosen(game_state):
    winner = connectfour.winner(game_state)
    if winner == connectfour.NONE:
        return True
    else:
        return False


if __name__ == '__main__':
    userInput()
