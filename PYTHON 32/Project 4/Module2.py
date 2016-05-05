# DUY B. LAM
# 61502602
# PROJECT 4 - MODULE 2 = IMPLEMENTS USER INTERFACE
#

import Module

class new_game():
    def __init__(self):
        self.rows_Qty = None
        self.columns_Qty = None
        self.first_turn = None
        self.center = None
        self.win_requirement = None

    def get_rows_Qty(self) -> int:
        '''
        Method returns the number of rows specified by user to create board
        '''
        return self.rows_Qty
    
    def get_columns_Qty(self) -> int:
        '''
        Method returns the number of columns specified by user to create board
        '''
        return self.columns_Qty
    
    def get_first_turn(self) -> str:
        ''' 
        Method returns 'W' if user wants 'W' to go first
        Method returns 'B' if user wants 'B' to go first
        '''
        return self.first_turn
    
    def get_center(self) -> str:
        ''' 
        Method returns 'W' if user wants TOP center row to be 'W B'
        Method returns 'B' if user wants TOP center row to be 'B W'
        '''
        return self.center
    
    def get_win_requirement(self) -> str:
        '''
            Function will return self.win_requirement of current instance of game. 
        '''
        return self.win_requirement
        
    
    def set_rows_columns_Qty(self) -> None:
        '''
            Function will read user input for specified board size (rows, columns).
            The specified quantities will be recorded to self.rows_Qty and self.columns_Qty accordingly.
        '''
        try:
            r = int(input())
            c = int(input())
            if (r%2 == 0) and (4 <= r <= 16):
                self.rows_Qty = r
            if (c%2 == 0) and (4 <= c <= 16):
                self.columns_Qty = c 
        except:
            print('Module 1 Function Error: set_rows_columns_Qty')
        finally:
            if (self.rows_Qty or self.columns_Qty) == None:
                print('INVALID')
                game.set_rows_columns_Qty(self)
        
    def set_first_turn(self) -> None:
        '''
            Function will set first move to 'W' or 'B'; specified by the user.
            Used to determine Player 1 and Player 2 in Module1.
        '''
        try:
            turn = input()
            if turn.upper() == 'B':
                self.first_turn = turn.upper()
            elif turn.upper() == 'W':
                self.first_turn = turn.upper()
        except:
            print('Module 2 FUnction error: set_first_turn')
        finally:
            if self.first_turn == None:
                print('INVALID')
                game.set_first_turn(self)

    def set_center(self) -> None:
        '''
            If user specifies TOP center row to be 'B W', method will assign
            'B' to self.center_x
            
            If user specifies TOP center row to be 'W B', method will asssign
            'W' to self.center_x

            Else: Method will print: 'invalid center - user input'
        '''
        try:
            key = input()
            if key.upper() == 'B':
                self.center = 'B'
            elif key.upper() == 'W':
                self.center = 'W'
        except:
            print('Module 2 Function Error: set_center')
        finally:
            if self.center == None:
                print('INVALID')
                game.set_center(self)
        
    def set_win_requirement(self)->None:
        '''
            Function will get user specifications for winning condition.
            Condition '>' or '<' will be recorded under self.win_requirement variable.
        '''
        try:
            userInput = input()
            while (userInput == '>' or '<'):            
                if userInput == '>':
                    self.win_requirement = '>'
                    break
                elif userInput == '<':
                    self.win_requirement = '<'
                    break
        except:
            print('MODULE 2 FUNCTION ERROR: set_win_requirement')
        finally:
            if self.win_requirement == None:
                print('INVALID')
                game.set_win_requirement(self)
            
        
if __name__ == '__main__':
    #CODE BLOCK RECORDS FIRST 5 USER INPUTS/SPECIFICATIONS
    game = new_game()
    game.set_rows_columns_Qty()
    game.set_first_turn()
    game.set_center()
    game.set_win_requirement()
    
    
    gameInstance = Module.StartGame(game.get_rows_Qty(),
                                     game.get_columns_Qty(),
                                     game.get_first_turn(),
                                     game.get_center(),
                                     game.get_win_requirement())
    print('FULL') 
    gameInstance.create_board()
    gameInstance.players_count()
    gameInstance.print_board()
    gameInstance.get_current_turn()

    gameCompleteness = gameInstance.check_completeness()
    while gameCompleteness == False:
        gameInstance.possible_valid_moves()
        if gameInstance.get_both_passes() == True:
            break
        gameInstance.next_move()
        gameInstance.switch_turn()
        gameCompleteness = gameInstance.check_completeness()
        if gameCompleteness == True:
            break
        gameInstance.print_board()
        gameInstance.get_current_turn()
        

    gameInstance.print_board() 
    gameInstance.define_winner()










    
