# DUY B. LAM
# 61502602
# PROJECT 5 - LOGIC MODULE = IMPLEMENTS GAME LOGIC
#

class StartGame():
    def __init__(self, rowsQ, columnsQ, firstTurn, center, winRequirement):
        self.board_size = (rowsQ, columnsQ)
        self.center = center
        self.turn = firstTurn
        self.board = []
        self.input = None
        self.match_directions = []
        self.list_to_flip = []
        self.b_count = None
        self.w_count = None
        self.winner = None
        self.win_requirement = winRequirement
        self.both_passes = False
        self.one_passes = False
        self.directions_valid = True

    def define_winner(self)->str:
        '''
            Function declares winner based on user specifications passed over from Module2.
            '>' specification will declare player with MORE pieces on board the winner.
            '<' specification will declare player with LESS pieces on board the winner.
            In the case when players pieces are EQUAL, winner is defined as NONE.
        '''
        condition = self.win_requirement
        winner = ''
        if condition == '>':
            if self.b_count > self.w_count:
                winner = 'WINNER: BLACK'
                print('WINNER: BLACK')
            elif self.w_count > self.b_count:
                winner = 'WINNER: WHITE'
                print('WINNER: WHITE')
            elif self.b_count == self.w_count:
                winner = 'WINNER: NONE'
                print('WINNER: NONE')
        if condition == '<':
            if self.b_count < self.w_count:
                winner = 'WINNER: BLACK'
                print('WINNER: BLACK')
            elif self.w_count < self.b_count:
                winner = 'WINNER: WHITE'
                print('WINNER: WHITE')
            elif self.b_count == self.w_count:
                winner = 'WINNER: NONE'
                print('WINNER: NONE')
        return winner

    def get_directions_valid(self)-> bool:
        return self.directions_valid

    def get_players_count(self) -> (int, int):
        return (self.b_count, self.w_count)

    def get_both_passes(self)->bool:
        '''
            Function returns a boolean value used to determine if both players can or cannot make a VALID move.
            Returns FALSE if any player have a valid move.
            Returns TRUE if both players DO NOT have a valid move.
        '''
        return self.both_passes

    def get_input(self, userClicked = (int, int)) -> None:
        '''
            Function reads player inputs for next turn.
            While turn is a LEGAL move, function will assign player input to the 'self.input' variable.
            If turn is an ILLEGAL move, function will print: INVALID and wait for player to type in another set of coordinates.
        '''
        board = self.board
        try:
            x = (userClicked)
            #x = x.split()
            a = int(x[0])
            b = int(x[1])
            if board[a - 1][b - 1] == '.':
                self.input = (a, b)
                print(a,b)
        except:
            pass
        finally:
            if self.input == None:
                print('INVALID')
                
                #StartGame.get_input(self, userClicked)

        
    def possible_valid_moves (self)->list:
        '''
            Function is used as a pre-test to check if the current player have any valid move at current game state.
            If player B or W does not have a valid move, function will call itself to test validity of oppisite player.
            If opposite player and current player both have NO valid moves, function will assign True to self.both_passes variable.
        '''
        board = self.board
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (1, 1), (-1, -1), (1, -1), (-1, 1)]
        match_directions = []
        empty_slot = []
        for i in range(self.board_size[0]):
            for e in range(self.board_size[1]):
                if board[i][e] == '.':
                    temp = (i, e)
                    empty_slot.append(temp)
        try:
            for e in empty_slot:
                
                x = e[0]
                y = e[1]
                
                current_turn = self.turn
                StartGame.switch_turn(self)
                opposite_turn = self.turn
                StartGame.switch_turn(self)
                
                for element in directions:
                    row = x + element[0]
                    column = y + element[1]
                    while (0 <= row < self.board_size[0]) and (0 <= column < self.board_size[1]):
                        if board[row][column] == opposite_turn:
                            result = StartGame.test_direction_recursion(self, row, column, element)
                            if result != None:
                                match_directions.append(result)
                                break
                            else:
                                row += element[0]
                                column += element[1]
                        else:
                            break
            #for element in match_directions:
                #print(element)
        except:
            print('FUNCTION ERROR : possible_validmoves')
        finally:
            if match_directions == [] and self.one_passes == False:
                print('{:s} PLAYER PASSES!'.format(self.turn))
                StartGame.switch_turn(self)
                print('TURN: {:s}'.format(self.turn))
                self.one_passes = True
                StartGame.possible_valid_moves(self)
            if match_directions == [] and self.one_passes == True:
                print('{:s} PLAYER PASSES!'.format(self.turn))
                StartGame.switch_turn(self)
                print('TURN: {:s}'.format(self.turn))
                self.both_passes = True
            else:
                self.one_passes = False
                self.both_passes = False
            
                    
    def test_directions(self)->None:
        '''
            Function will test user input for match direction(s) of a legal move.
            Test Direction Cases: N, W, S, E, NW, NE, SW, SE  (is assigned to directions variable in the function)
            If player specified move is NOT VALID, function will print INVALID and wait for another set of coordinates.
            NOTE: Function test will call a recursion function defined as 'test_direction_recursion' to carry out it's processing.
                Function appends match directions to self.match_directions list if any match is found.           
        '''
        self.directions_valid = True
        board = self.board
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (1, 1), (-1, -1), (1, -1), (-1, 1)]
        match_directions = []

        try:
            #if board[self.input[0]][self.input[1]] == '.':
            x = self.input[0] - 1
            y = self.input[1] - 1

            print(x, y)
            
            current_turn = self.turn
            StartGame.switch_turn(self)
            opposite_turn = self.turn
            StartGame.switch_turn(self)
            
            for element in directions:
                row = x + element[0]
                column = y + element[1]
                while (0 <= row < self.board_size[0]) and (0 <= column < self.board_size[1]):
                    if board[row][column] == opposite_turn:
                        result = StartGame.test_direction_recursion(self, row, column, element)
                        if result != None:
                            match_directions.append(result)
                            break
                        else:
                            row += element[0]
                            column += element[1]
                    else:
                        break
            self.match_directions = match_directions
            #print(self.match_directions)
            #print('code ran')
        except:
            pass
        finally:
            if self.match_directions == []:
                print('INVALID Module.test_directions(self)')
                self.directions_valid = False
                #self.input = None
                #StartGame.get_input(self)
                #StartGame.test_directions(self)

    def test_direction_recursion(self, row, column, element) -> list or None:
        '''
            This is a helper function used to carry out test_directions function.
        '''
        row2 = row
        column2 = column
        current_turn = self.turn
        board = self.board
        result = None
        while (0 <= row2 < self.board_size[0]) and (0 <= column2 < self.board_size[1]):
            if board[row2][column2] == current_turn:
                result = element
                break
            row2 += element[0]
            column2 += element[1]
        return result
    
    def get_flip_elements(self)->None:
        '''
            Function uses self.match_directions list generated by test_directions function to find opposite pieces that should be flipped according to game rules.
            Note: Pieces that should be flipped according to VALID specified move will be appended to a list in format of [(rowNumber, columnNumber),...]
            The list of pieces to flip location will be stored in self.list_to_flip variable.
        '''
        self.directions_valid = True
        try:
            board = self.board
            
            current_turn = self.turn
            StartGame.switch_turn(self)
            opposite_turn = self.turn
            StartGame.switch_turn(self)
            
            x = self.input[0] - 1
            y = self.input[1] - 1
            temp_list = []
            
            for element in self.match_directions:
                row = x + element[0]
                column = y + element[1]
                while (0 <= row < self.board_size[0]) and (0 <= column < self.board_size[1]):
                    if board[row][column] == current_turn or opposite_turn:
                        if board[row][column] == opposite_turn:
                            temp = (row, column)
                            temp_list.append(temp)
                        elif board[row][column] == current_turn:
                            break
                        row += element[0]
                        column += element[1]
                    else:
                        break
            self.list_to_flip = temp_list
        except:
            pass
        finally:
            if self.list_to_flip == []:
                print('INVALID: Module.get_flip_elements()')
                self.directions_valid = False
##                StartGame.get_input(self)
##                StartGame.test_directions(self)
##                StartGame.get_flip_elements(self)
            elif self.list_to_flip != []:
                print('VALID')

    def flip_elements(self)->None:
        '''
            Function will read self.list_to_flip list for locations of pieces to flip.
            Flip process is applied throughout this function as well as assigning the current turn to user specified location. 
        '''
        try:
            board = self.board
            board[self.input[0] - 1][self.input[1] - 1] = self.turn
            #board[self.input[0]][self.input[1]] = self.turn
            for i in self.list_to_flip:
                board[i[0]][i[1]] = self.turn
        except:
            print('FUNCTION ERROR: flip_elements')

    def players_count(self)->None:
        '''
            Function will keep current game state count of each player's total pieces.
            BLACK peices will be counted and recorded to self.b_count.
            WHITE peices will be counted and recorded to self.w_count.
            Also, a print statement will identify black as B and white as W with their count projected.
        '''
        board = self.board
        b_count = 0
        w_count = 0
        for i in board:
            for e in i:
                if e == 'B':
                    b_count += 1
                if e == 'W':
                    w_count += 1
        self.b_count = b_count
        self.w_count = w_count
        print('B: {:d}  W: {:d}'.format(self.b_count, self.w_count))
                
    def next_move(self, userClicked = (int, int))->None:
        '''
            next_move function will call a set of functions in the order : (get_input > test_directions > get_flip_elements > flip_elements > players_count) 
        '''
        
        StartGame.get_input(self, userClicked)
        StartGame.test_directions(self)
        if self.directions_valid == True:
            StartGame.get_flip_elements(self)
        if self.directions_valid == True:
            StartGame.flip_elements(self)
        StartGame.players_count(self)
        
        
    def get_current_turn(self)-> str:
        '''
            Function will print the current player's turn of game instance.
        '''
        print('TURN: {:s}'.format(self.turn))
        a = ('TURN: {:s}'.format(self.turn))
        return self.turn
        
    
    def create_board(self)->None:
        '''
            Function creates a new game board based on center options as specified by user.
        '''
        rows = self.board_size[0]
        columns = self.board_size[1]
        board = self.board
        
        topRowCenter = int(rows/2) - 1
        topColumnCenter = int(columns/2) - 1

        a = ''
        b = ''
        if self.center == 'B':
            a = 'B'
            b = 'W'
        elif self.center == 'W':
            a = 'W'
            b = 'B'
        
        for i in range(0, rows):
            board.append(['.'] * columns)

        board[topRowCenter][topColumnCenter] = a
        board[topRowCenter][topColumnCenter +1] = b
        board[topRowCenter+1][topColumnCenter] = b
        board[topRowCenter+1][topColumnCenter+1] = a
    
    def switch_turn(self)->None:
        '''
            Function will switch current turn from black player to white, or white player to black based on when the command is called. 
        '''
        while self.turn == 'B' or 'W':
            if self.turn == 'B':
                self.turn = 'W'
                break
            elif self.turn == 'W':
                self.turn = 'B'
                break
            
    def print_board(self)->list:
        '''
            Function will print current state of board game stored in self.board (list)
        '''
        for i in range(self.board_size[0]):
            for e in range(self.board_size[1]):
                print(self.board[i][e], end = ' ')
                if e == (self.board_size[1] - 1):
                    print()
        return self.board

    def check_completeness(self) -> bool:
        '''
            Funtion checks if there is any open slot(s) in current board state for players to suggest a move. 
        '''
        board = self.board
        for i in range(self.board_size[0]):
            for e in range(self.board_size[1]):
                if board[i][e] == '.':
                    return False
        return True
