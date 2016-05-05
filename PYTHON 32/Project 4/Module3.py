

class StartGame():
    def __init__(self, rowsQ, columnsQ, firstTurn, center):
        self.board_size = (rowsQ, columnsQ)
        self.center = center
        self.turn = firstTurn
        self.board = []
        
    def next_move(self):
        pass

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
    
    def print_board(self) -> None:
        for element in self.board:
            print(element)
            
    def switch_turn(self) -> None:
        while self.turn == 'B' or 'W':
            if self.turn == 'B':
                self.turn = 'W'
                break
            elif self.turn == 'W':
                self.turn = 'B'
                break
            
    def check_completeness(self) -> bool:
            board = self.board
            for rows in board:
                for element in rows:
                    if element == '.':
                        return False
                    else:
                        return True
