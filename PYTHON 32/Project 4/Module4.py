# DUY B. LAM
# 61502602
# PROJECT 4 - MODULE 1 = IMPLEMENTS GAME LOGIC
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

    def define_winner(self):
        condition = self.win_requirement
        if condition == '>':
            if self.b_count > self.w_count:
                print('WINNER: BLACK')
            elif self.w_count > self.b_count:
                print('WINNER: WHITE')
            elif self.b_count == self.w_count:
                print('WINNER: NONE')
        if condition == '<':
            if self.b_count < self.w_count:
                print('WINNER: BLACK')
            elif self.w_count < self.b_count:
                print('WINNER: WHITE')
            elif self.b_count == self.w_count:
                print('WINNER: NONE')

    def get_both_passes(self):
        return self.both_passes

    def get_input(self) -> None:
        board = self.board
        try:
            #print('get input started')
            x = (input())
            x = x.split()
            #print(type(x))
            a = int(x[0])
            b = int(x[1])
            if board[a - 1][b - 1] == '.':
                self.input = (a, b)
            #print(a, b)
            #StartGame.test_directions(self)
            #print('get input ended')
        except:
            #print('FUNCTION ERROR: get_input')
            pass
        finally:
            if self.input == None:
                print('INVALID')
                StartGame.get_input(self)

        
    def possible_valid_moves (self):
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
        #print('possible_valid_moves started')
        #print(empty_slot)
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
            #self.match_directiomatch_directions
            #print(match_directions)
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
            
            
            
##            if match_directions != []:
##                print('VALID MOVES FOUND')
        

        
    def test_directions(self):
        board = self.board
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (1, 1), (-1, -1), (1, -1), (-1, 1)]
        match_directions = []

        try:
            x = self.input[0] - 1
            y = self.input[1] - 1
            
            current_turn = self.turn
            StartGame.switch_turn(self)
            opposite_turn = self.turn
            StartGame.switch_turn(self)
            
            for element in directions:
                row = x + element[0]
                column = y + element[1]
                while (0 <= row < self.board_size[0]) and (0 <= column < self.board_size[1]):
                    #print('test_directions started')
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
                        #row += element[0]
                        #column += element[1]
            #print('test directions ended')
            self.match_directions = match_directions
        except:
            #print('FUNCTION ERROR: test_directions')
            pass
        finally:
            if match_directions == []:
                print('INVALID')
                self.input = None
                StartGame.get_input(self)
                StartGame.test_directions(self)

    def test_direction_recursion(self, row, column, element):
        row2 = row
        column2 = column
        current_turn = self.turn
        board = self.board
        result = None
        while (0 <= row2 < self.board_size[0]) and (0 <= column2 < self.board_size[1]):
            if board[row2][column2] == current_turn:
                #print('test_direction_loop found')
                result = element
                break
            row2 += element[0]
            column2 += element[1]
        return result
    
    def get_flip_elements(self):
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
                    #print('get_flip_elements loop started')
                    #print(board[row][column])
                    #print(current_turn, opposite_turn)
                    if board[row][column] == current_turn or opposite_turn:
                        #print('b or w found')
                        if board[row][column] == opposite_turn:
                            #print('opposite match found')
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
            #print('FUNCTION ERROR: get_flip_elements')
            pass
        finally:
            if self.list_to_flip == []:
                #print('list_to_flip is empty')
                print('INVALID')
                StartGame.get_input(self)
                StartGame.test_directions(self)
                StartGame.get_flip_elements(self)
            elif self.list_to_flip != []:
                print('VALID')

    def flip_elements(self):
        try:
            board = self.board
            board[self.input[0] - 1][self.input[1] - 1] = self.turn
            for i in self.list_to_flip:
                board[i[0]][i[1]] = self.turn
        except:
            print('FUNCTION ERROR: flip_elements')

    def players_count(self):
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
        #print('W = {:d}'.format(self.w_count))
                
    def next_move(self):
        StartGame.get_input(self)
        StartGame.test_directions(self)#will fill slot with current turn if directions: FOUND | turn is not yet flipped
        StartGame.get_flip_elements(self)
        StartGame.flip_elements(self)
        StartGame.players_count(self)
        
        
        #print(self.input, self.match_directions, self.list_to_flip)
        
    def get_current_turn(self)->None:
        print('TURN: {:s}'.format(self.turn))
        
    
    def create_board(self):
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
    
    #fill slot with current turn and pass turn to next player
    def switch_turn(self):
        while self.turn == 'B' or 'W':
            if self.turn == 'B':
                self.turn = 'W'
                break
            elif self.turn == 'W':
                self.turn = 'B'
                break
            
    def print_board(self):
        for i in range(self.board_size[0]):
            for e in range(self.board_size[1]):
                print(self.board[i][e], end = ' ')
                if e == (self.board_size[1] - 1):# and i != (self.board_size[0] - 1):
                    print()
        #print()
        #for element in self.board:
            #print(str(element))

    def check_completeness(self) -> bool:
        board = self.board
        for i in range(self.board_size[0]):
            for e in range(self.board_size[1]):
                if board[i][e] == '.':# and i != (self.board_size[0] - 1):
                    return False
        return True
##        for rows in board:
##            for element in rows:
##                if element == '.':
##                    return False
##                else:
##                    return True
