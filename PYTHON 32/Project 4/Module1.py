# DUY B. LAM
# 61502602
# PROJECT 4 - MODULE 1 = IMPLEMENTS GAME LOGIC
# 

class StartGame():
    def __init__(self, rowsQ, columnsQ, firstTurn, center):
        self.rows_Qty = rowsQ
        self.columns_Qty = columnsQ
        #self.match = (int, int)
        self.center = center #see Module2 for bool value specifications
        self.row_cord = int()
        self.column_cord = int()
        self.board = []
        self.turn = firstTurn

##    def define_variables(self):
##        if self.first_turn == 'B':
##            self.turn = 'B'
##        elif self.first_turn == 'W':
##            self.turn = 'W'
##        else:
##            print('Module1: variables are invalid (not B or W)')
        
    def create_board(self):
        rows = self.rows_Qty
        columns = self.columns_Qty
        topRowCenter = int(rows/2)-1
        topColumnCenter = int(columns/2)-1
        board = self.board
        a = ''
        b = ''
        if self.center == 'B':
            a = 'B'
            b = 'W'
        elif self.center == 'W':
            a = 'W'
            b = 'B'
        #CODE BLOCK CREATES AN EMPTY BOARD USING SPECIFIED ROWS AND COLUMNS NUMBER
        for i in range(0, rows):
            board.append(['.'] * columns)
        #CODE WILL EDIT EMPTY BOARD TO ADJUST PREGAME CENTER BASED ON USER INPUT
        board[topRowCenter][topColumnCenter] = a
        board[topRowCenter][topColumnCenter +1] = b
        board[topRowCenter+1][topColumnCenter] = b
        board[topRowCenter+1][topColumnCenter+1] = a

    def next_move(self):
        row_cord = None
        column_cord = None
        board = self.board
        emptySlot = True
        matchElement = False
        match = None
        
        while ((row_cord or column_cord) == None) :
            row_cord = int(input())
            column_cord = int(input())
            if row_cord != 0:
                row_cord -= 1
            if column_cord != 0:
                column_cord -= 1

            if (0 <= row_cord < self.rows_Qty) and (0 <= column_cord < self.columns_Qty): 
            
                #checks if specified slot is empty    
                if board[row_cord][column_cord] != '.':
                    print('FILLED SLOT : ILLEGAL MOVE!')
                    row_cord = None
                    column_cord = None
                    emptySlot = False
                else:
                    emptySlot = True
                    print('empty loop ran')

                #checks if specified slot is still empty and if it matches with specified rules    
                while (emptySlot == True and matchElement == False):
                    #look one element up from specified slot
                    while (row_cord - 1 >= 0):
                        if board[row_cord-1][column_cord] != (self.turn):
                            if board[row_cord-1][column_cord] != ('.'):
                                double_check = row_cord - 1
                                for i in range(double_check, 0, -1):
                                    if board[i][column_cord] == self.turn:
                                        print('Top OPPOSITE MATCH : Found')
                                        match = 'N'
                                        matchElement = True
                        break

                    #look one element down from specified slot
                    while (row_cord + 1 < self.rows_Qty):
                        if board[row_cord + 1][column_cord] != (self.turn):
                            if board[row_cord + 1][column_cord] != ('.'):
                                double_check = row_cord + 1
                                for i in range(double_check, self.rows_Qty):
                                    if board[i][column_cord] == self.turn:
                                        match = 'S'
                                        print(match)
                                        matchElement = True
                        break

                    #look one element left from specified slot
                    while (column_cord - 1 >= 0):
                        if board[row_cord][column_cord - 1] != (self.turn):
                            if board[row_cord][column_cord - 1] != ('.'):
                                double_check = column_cord - 1
                                for i in range(double_check, 0, -1):
                                    if board[row_cord][i] == self.turn:
                                        match = 'W'
                                        print(match)
                                        matchElement = True
                        break
                            
                    #look one element right from specified slot
                    while (column_cord + 1 < self.columns_Qty):
                        if board[row_cord][column_cord + 1] != (self.turn):
                            if board[row_cord][column_cord + 1] != ('.'):
                                double_check = column_cord +1
                                for i in range(double_check, self.columns_Qty):
                                    if board[row_cord][i] == self.turn:
                                        match = 'E'
                                        print(match)
                                        matchElement = True
                        break

                    #look NorthWest of board for match
                    while (row_cord - 1 >= 0) and (column_cord - 1 >= 0):
                        if board[row_cord - 1][column_cord - 1] != (self.turn):
                            if board[row_cord - 1][column_cord - 1] != ('.'):
                                double_check_row = row_cord - 1
                                double_check_column = column_cord - 1
                                while (double_check_row - 1 >= 0) and (double_check_column - 1 >= 0):
                                        if board[double_check_row][double_check_column] == self.turn:
                                            match = 'NW'
                                            print(match)
                                            matchElement = True
                                            break
                                        double_check_row -= 1
                                        double_check_column -= 1
                        break
                    #look SouthEast of board for match
                    while (row_cord + 1 < self.rows_Qty) and (column_cord + 1 < self.columns_Qty):
                        print('LOOP started')
                        if board[row_cord + 1][column_cord + 1] != (self.turn):
                            if board[row_cord + 1][column_cord + 1] != ('.'):
                                double_check_row = row_cord + 1
                                double_check_column = column_cord + 1
                                while (double_check_row + 1 < self.rows_Qty) and (double_check_column + 1 < self.rows_Qty):
                                        if board[double_check_row][double_check_column] == self.turn:
                                            match = 'SE'
                                            print(match)
                                            matchElement = True
                                            break
                                        double_check_row += 1
                                        double_check_column += 1
                        break
                        
                    
                    if matchElement == False:
                        print('OPPOSITE MATCH : NOT Found')
                        row_cord = None
                        column_cord = None
                        emptySlot = False
                        topElement = False

                
            
                        
            # resets cordinates to None and restart INPUT loop
            #       if specified coordinates are out of range           
            else:
                print('specified coordinates out of range. try again')
                row_cord = None
                column_cord = None
                
##                else:
##                    print('OPPOSITE MATCH : Found')
##                    topElement = True
##                    print(row_cord, column_cord)
##                    break
                
        #assigns TESTED coordinates to self variables
        #   self.row_cord = row_cord
        #   self.column_cord = column_cord
        #board = self.board
        board[row_cord][column_cord] = self.turn
        self.row_cord = row_cord
        self.column_cord = column_cord
        print('coordinates tested and recorded')
        print(match)


        #CODE BLOCK USED TO FIND MATCH OF SPECIFIED SLOT
        match_coordinates = None
        while match_coordinates == None:
            #print('while match_coordinates loop started') to double check
            if match == 'N':
                while (row_cord >= 0):
                    if board[row_cord][column_cord] == '.':
                        row_rev = row_cord
                        while row_cord <= row_rev <= self.row_cord:
                            row_rev += 1
                            if board[row_rev][column_cord] == self.turn:
                                match_coordinates = (row_rev+1, column_cord+1)
                                print(match_coordinates)
                                break
                        break
                    row_cord -= 1
            if match == 'S':
                while (row_cord < self.rows_Qty):
                    if board[row_cord][column_cord] == '.':
                        #print('bottom . found ' + str(row_cord)) to double check
                        row_rev = row_cord
                        print(row_rev)
                        while  self.row_cord < row_rev <= row_cord:
                            row_rev -= 1
                            if board[row_rev][column_cord] == self.turn:
                                #print('match variable found') to double check
                                match_coordinates = (row_rev+1, column_cord+1)
                                #print(match_coordinates) to double check
                                break
                        break
                    row_cord += 1
            if match == 'W':
                while (column_cord >= 0):
                    if board[row_cord][column_cord] == '.':
                        column_rev = column_cord
                        print(column_rev)
                        print(self.column_cord)
                        while column_cord <= column_rev < self.column_cord:
                            #print('L rev loop started') to double check
                            column_rev += 1
                            if board[row_cord][column_rev] == self.turn:
                                match_coordinates = (row_cord+1, column_rev+1)
                                #print(match_coordinates) to double check
                                break
                        break
                    column_cord -= 1
            if match == 'E':
                while (column_cord < self.rows_Qty):
                    if board[row_cord][column_cord] == '.':
                        column_rev = column_cord
                        while self.column_cord < column_rev <= column_cord:
                            column_rev -= 1
                            if board[row_cord][column_rev] == self.turn:
                                match_coordinates = (row_cord+1, column_rev+1)
                                #print(match_coordinates) to double check
                                break
                        break
                    column_cord += 1
            #print('match coordinates loop ended') to double check
                    
            if match == 'NW':
                while (row_cord >= 0) and (column_cord >= 0):
                    if board[row_cord][column_cord] == '.':
                        column_rev = column_cord
                        row_rev = row_cord
                        while (column_cord <= column_rev < self.column_cord) and (row_cord <= row_rev <= self.row_cord):
                            column_rev += 1
                            row_rev += 1
                            if board[row_rev][column_rev] == self.turn:
                                match_coordinates = (row_rev +1, column_rev +1)
                                print('found')
                                break
                            print('notfound')
                        break
                    column_cord -= 1
                    row_cord -= 1

            if match == 'SE':
                while (row_cord < self.rows_Qty) and (column_cord < self.columns_Qty):
                    if board[row_cord][column_cord] == '.':
                        column_rev = column_cord
                        row_rev = row_cord
                        while (column_cord <= column_rev < self.column_cord) and (row_cord <= row_rev <= self.row_cord):
                            column_rev -= 1
                            row_rev -= 1
                            if board[row_rev][column_rev] == self.turn:
                                match_coordinates = (row_rev +1, column_rev +1)
                                print('found')
                                break
                            print('notfound')
                        break
                    column_cord += 1
                    row_cord += 1
                    
            break
        print(match_coordinates)
        print(type(match_coordinates))
        
        row_difference = abs(self.row_cord - match_coordinates[0])
        column_difference = abs(self.column_cord - match_coordinates[1])

        while row_difference != 0:
            if self.row_cord > match_coordinates[0]:
                for i in range(match_coordinates[0], self.row_cord):
                    board[i][self.column_cord] = self.turn
                break
            if self.row_cord < match_coordinates[0]:
                for i in range(self.row_cord, match_coordinates[0]):
                    board[i][self.column_cord] = self.turn
                break
        while column_difference != 0:
            if self.column_cord > match_coordinates[1]:
                for i in range(match_coordinates[1], self.column_cord):
                    board[self.row_cord][i] = self.turn
                break
            if self.column_cord < match_coordinates[1]:
                for i in range(self.column_cord, match_coordinates[1]):
                    board[self.row_cord][i] = self.turn
                break
            
        #row_difference = None
        #column_difference = None
        #match_coordinates = None
                            
            
            
        



    #fill slot with current turn and pass turn to next player
    def switch_turn(self):
        while self.turn == 'B' or 'W':
            if self.turn == 'B':
                self.turn = 'W'
                break
            elif self.turn == 'W':
                self.turn = 'B'
                break
        
            

        
                
                
                    
        # ****IMPORTANT CODE!!!, DOUBLE CHECK BEFORE DELETE*** 
##        board = self.board
##        board[row_cord][column_cord] = self.turn
##        while self.turn == 'B' or 'W':
##            if self.turn == 'B':
##                self.turn = 'W'
##                break
##            elif self.turn == 'W':
##                self.turn = 'B'
##                break
        
        
    def check_completeness(self) -> bool:
        board = self.board
        for rows in board:
            for element in rows:
                if element == '.':
                    return False
                else:
                    return True
        

    def print_board(self):
        for element in self.board:
            print(element)
