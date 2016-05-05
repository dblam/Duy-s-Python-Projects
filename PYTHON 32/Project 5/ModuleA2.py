import tkinter
import Module
import math



DEFAULT_FONT = ('Calibri', 14)

class inputDialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        #INTRODUCTION TO DIALOG
        intro_label = tkinter.Label(
            master = self._dialog_window,
            text = ('PLEASE SPECIFY GAME PRESETS:'), font = DEFAULT_FONT)
        intro_label.grid(
            row = 0, column = 0, columnspan = 3, sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)
        
        #ROW LABEL AND ENTRY BOX
        rows_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Rows: (between 4-16 even)', font = DEFAULT_FONT)
        rows_label.grid(
            row = 1, column = 0, columnspan = 2, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)
        self._rows_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._rows_entry.grid(
            row = 1, column = 3, sticky = tkinter.W)

        #COLUMN LABEL AND ENTRY BOX
        columns_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Columns: ( between 4-16 even )', font = DEFAULT_FONT)
        columns_label.grid(
            row = 2, column = 0, columnspan = 2, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)
        self._columns_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._columns_entry.grid(
            row = 2, column = 3, sticky = tkinter.W)

        #FIRST TURN LABEL AND ENTRY BOX
        first_turn_label = tkinter.Label(
            master = self._dialog_window,
            text = 'First Turn: ( B or W )', font = DEFAULT_FONT)
        first_turn_label.grid(
            row = 3, column = 0, columnspan = 2, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)
        self._first_turn_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._first_turn_entry.grid(
            row = 3, column = 3, sticky = tkinter.W)

        #DISC ARRANGEMENT LABEL AND ENTRY BOX
        disc_arrangement_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Four Discs Arrangement: ( B or W )', font = DEFAULT_FONT)
        disc_arrangement_label.grid(
            row = 4, column = 0, columnspan = 2, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)
        self._disc_arrangement_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._disc_arrangement_entry.grid(
            row = 4, column = 3, sticky = tkinter.W)

        #WINNER SPECIFIER LABEL AND ENTRY BOX
        winner_specifier_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Winner Specifier: ( > or < )', font = DEFAULT_FONT)
        winner_specifier_label.grid(
            row = 5, column = 0, columnspan = 2, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)
        self._winner_specifier_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._winner_specifier_entry.grid(
            row = 5, column = 3, sticky = tkinter.W)

        # OK AND CANCEL BUTTONS
        button_frame = tkinter.Frame(master = self._dialog_window)
        button_frame.grid(
            row = 6, column = 3, columnspan = 3, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)
        ok_button = tkinter.Button(master = button_frame, text = 'OK', font = DEFAULT_FONT,
                                   command = self._on_ok_button)
        ok_button.grid(row = 0, column = 0, padx = 5, pady = 5)
        cancel_button = tkinter.Button(master = button_frame, text = 'CANCEL', font = DEFAULT_FONT,
                                       command = self._on_cancel_button)
        cancel_button.grid(row = 0, column = 1, padx = 5, pady = 5)

        #BALANCE ROWS AND COLUMNS ON INPUT DIALOG RESIZE
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)

        #VARIABLES FOR USER INPUTS and BOOL INDICATORS        
        self._ok_clicked = False
        self._rows = 4
        self._columns = 4
        self._first_turn = ''
        self._disc_arrangement = ''
        self._winner_specifier = ''

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._rows = self._rows_entry.get()
        self._columns = self._columns_entry.get()
        self._first_turn = self._first_turn_entry.get()
        self._disc_arrangement = self._disc_arrangement_entry.get()
        self._winner_specifier = self._winner_specifier_entry.get()

        self._dialog_window.destroy()

    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_inputs(self) -> list:
        temp_list = []
        temp_list.append(self._rows)
        temp_list.append(self._columns)
        temp_list.append(self._first_turn)
        temp_list.append(self._disc_arrangement)
        temp_list.append(self._winner_specifier)
        return temp_list

    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()    

class Layout:
    def __init__(self):
        
        self._root_window = tkinter.Tk()
        self._board_specifications = []

        #INTRODUCTION LABEL
        intro_label = tkinter.Label(
            master = self._root_window,
            text = 'Please press button below to enter pre-game specifications:\n', font = DEFAULT_FONT)
        intro_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)
    
        #BUTTON TO GET USER INPUTS
        button1 = tkinter.Button(
            master = self._root_window, font = DEFAULT_FONT, text = 'GET USER INPUTS',
            command = self._on_button1_clicked)
        button1.grid(
            row = 1, column = 0, 
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        #BALANCE ROWS AND COLUMNS ON WINDOW RESIZE
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self) -> None:
        self._root_window.mainloop()

    def _on_button1_clicked(self) -> None:
        dialog = inputDialog()
        dialog.show()
        if dialog.was_ok_clicked():
            input_list = dialog.get_inputs()
        for element in input_list:
            print(element)
        self._board_specifications = input_list
        
        board = Board(self._board_specifications)
        board.show()
        
    def get_board_specifications(self) -> list:
        return self.board_specifications()

class Board:
    
    def __init__(self, specifications_list) -> None:
        
        self._board_window = tkinter.Toplevel()
        self._board_specifications = specifications_list

        self._canvas_width = int(self._board_specifications[1]) * 40
        self._canvas_height = int(self._board_specifications[0]) * 40

        self.width_frac = 1
        self.height_frac = 1

        self.x_axis = []
        self.y_axis = []

        self.cirle_color = ''
        
        self._canvas = tkinter.Canvas(
            master = self._board_window,
            width = self._canvas_width, height = self._canvas_height,
            background = 'blue')
        
        self._canvas.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        #CALL FUNCTION TO REDRAW ALL SHAPES ON BOARD RESIZE 
        self._canvas.bind('<Configure>', self._on_canvas_resized)

        #CALL FUNCTION ON MOUSE CLICK
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        
        #STRING VARIABLE FOR SCORES LABEL AND UPDATES
        self._score = tkinter.StringVar(value = 'test current scores string var')
        current_score = tkinter.Label(
            master = self._board_window, font = DEFAULT_FONT,
            textvariable = self._score)
        current_score.grid(
            row = 1, column = 0, sticky = tkinter.W)

        #STRING VARIABLE FOR CURRENT TURN LABEL AND UPDATES
        self._current_turn = tkinter.StringVar(value = 'test current turn string var')
        current_turn = tkinter.Label(
            master = self._board_window, font = DEFAULT_FONT,
            textvariable = self._current_turn)
        current_turn.grid(
            row = 1, column = 1, sticky = tkinter.W)

        #BALANCE ROWS AND COLUMNS ON BOARD RESIZE
        self._board_window.rowconfigure(0, weight = 1)
        self._board_window.columnconfigure(0, weight = 1)

        #TO DRAW CHESS BOARD 
        self.draw_rectangles()

        #in progress.. Sync GUI with GameLOGIC > START NEW GAME INSTANCE IF CREATE BOARD
        self.gameInstance = Module.StartGame(int(self._board_specifications[0]),
                                        int(self._board_specifications[1]),
                                        self._board_specifications[2].upper(),
                                        self._board_specifications[3].upper(),
                                        self._board_specifications[4])
        print('gameInstance created')
        self.gameInstance.create_board()
        print('gameInstance.creat_board() ran.')
        self.gameInstance.players_count()
        print('gameInstance.players_count() ran.')
        self._game_board = self.gameInstance.print_board()
        print('gameInstance.print_board() ran.')
        self.gameInstance.get_current_turn()
        print('gameInstance.current_turn()')
        
        score_tuple = (2, 2)
        score_tuple = self.gameInstance.get_players_count()
        self._score.set('B: {:d}  W: {:d}'.format(score_tuple[0], score_tuple[1]))
        current_player = ''
        current_player = self.gameInstance.get_current_turn()
        self._current_turn.set('TURN: {:s}'.format(current_player))
        
        
    def check_score_and_turn(self):
        #check current turn and update click-circle-color accordingly
        current_player = self.gameInstance.get_current_turn()
        self._current_turn.set('TURN: {:s}'.format(current_player))
        if current_player == 'B':
            self.circle_color = 'black'
        if current_player == 'W':
            self.circle_color = 'white'
        #check current score and update accordingly
        score_tuple = self.gameInstance.get_players_count()
        self._score.set('B: {:d}  W: {:d}'.format(score_tuple[0], score_tuple[1]))
        
        
        

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:    
        row = math.floor(event.y / 40)
        column = math.floor(event.x / 40)
        #self.check_score_and_turn()
        print(row,column)
        #self.draw_circle(column, row, column+1, row+1)
        

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._canvas.delete(tkinter.ALL)
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self.width_frac = canvas_width / self._canvas_width
        self.height_frac = canvas_height / self._canvas_height

        self.draw_rectangles()
        #self.draw_circles(self._board_specifications[3])
        self.draw_circles()
        
    def draw_circle(self, x1, y1, x2, y2) -> None:
        random = self.circle_color
        cir = self._canvas.create_oval(x1 * 40 * self.width_frac, y1 * 40 * self.height_frac,
                                       x2 * 40 * self.width_frac, y2 * 40 * self.height_frac,
                                       fill = random)
    def draw_circles(self):
        board = self._game_board
        for i in range(int(self._board_specifications[0])):
            for e in range(int(self._board_specifications[1])):
                if board[i][e] == 'B':
                    self.circle_color = 'black'
                    self.draw_circle(e, i, e+1, i+1)
                if board[i][e] == 'W':
                    self.circle_color = 'white'
                    self.draw_circle(e, i, e+1, i+1)
                
        

##    def draw_standard_circles(self, arrangement: str) -> None:
##        column_mid = int((int(self._board_specifications[1])/2) - 1)
##        row_mid = int((int(self._board_specifications[0])/2) - 1)
##        if self._board_specifications[3].upper() == 'B':
##            
##            TL_Cir = self._canvas.create_oval(column_mid * 40 * self.width_frac,
##                                              row_mid * 40 * self.height_frac,
##                                              (column_mid+1) * 40 * self.width_frac,
##                                              (row_mid+1) * 40 * self.height_frac,
##                                              outline = 'black', fill = 'black')
##            BL_Cir = self._canvas.create_oval((column_mid+1) * 40 * self.width_frac,
##                                              (row_mid+1) * 40 * self.height_frac,
##                                              (column_mid+2) * 40 * self.width_frac,
##                                              (row_mid+2) * 40 * self.height_frac,
##                                              outline = 'black', fill = 'black')
##
##            TR_Cir = self._canvas.create_oval((column_mid+1) * 40 * self.width_frac,
##                                              row_mid * 40 * self.height_frac,
##                                              (column_mid+2) * 40 * self.width_frac,
##                                              (row_mid+1) * 40 * self.height_frac,
##                                              outline = 'white', fill = 'white')
##            BR_Cir = self._canvas.create_oval((column_mid) * 40 * self.width_frac,
##                                              (row_mid+1) * 40 * self.height_frac,
##                                              (column_mid+1) * 40 * self.width_frac,
##                                              (row_mid+2) * 40 * self.height_frac,
##                                              outline = 'white', fill = 'white')
##            
##        if self._board_specifications[3].upper() == 'W':
##            TL_Cir = self._canvas.create_oval(column_mid * 40 * self.width_frac,
##                                              row_mid * 40 * self.height_frac,
##                                              (column_mid+1) * 40 * self.width_frac,
##                                              (row_mid+1) * 40 * self.height_frac,
##                                              outline = 'white', fill = 'white')
##            TR_Cir = self._canvas.create_oval((column_mid+1) * 40 * self.width_frac,
##                                              row_mid * 40 * self.height_frac,
##                                              (column_mid+2) * 40 * self.width_frac,
##                                              (row_mid+1) * 40 * self.height_frac,
##                                              outline = 'black', fill = 'black')
##            BL_Cir = self._canvas.create_oval((column_mid+1) * 40 * self.width_frac,
##                                              (row_mid+1) * 40 * self.height_frac,
##                                              (column_mid+2) * 40 * self.width_frac,
##                                              (row_mid+2) * 40 * self.height_frac,
##                                              outline = 'white', fill = 'white')
##            BR_Cir = self._canvas.create_oval((column_mid) * 40 * self.width_frac,
##                                              (row_mid+1) * 40 * self.height_frac,
##                                              (column_mid+1) * 40 * self.width_frac,
##                                              (row_mid+2) * 40 * self.height_frac,
##                                              outline = 'black', fill = 'black')




    def draw_rectangle(self, x1, y1, x2, y2) -> None:
        rec = self._canvas.create_rectangle(x1, y1, x2, y2)
        

    def draw_rectangles(self) -> None:
        rows = int(self._board_specifications[0])
        rows_list = []
        for i in range(rows):
            rows_list.append(i)
            
        columns = int(self._board_specifications[1])
        columns_list = []
        for i in range(columns):
            columns_list.append(i)

        self.x_axis = columns_list
        self.y_axis = rows_list
            
        for r_num in self.y_axis:
            for c_num in self.x_axis:
                x1 = c_num * 40 * self.width_frac
                y1 = r_num * 40 * self.height_frac
                x2 = (c_num + 1) * 40 * self.width_frac
                y2 = (r_num + 1) * 40 * self.height_frac
                self.draw_rectangle(x1, y1, x2, y2)

                
        
                
        
    def show(self) -> None:
        self._board_window.grab_set()
        self._board_window.wait_window()

if __name__ == '__main__':
    app = Layout()
    app.start()
