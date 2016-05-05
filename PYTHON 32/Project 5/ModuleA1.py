import tkinter



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
            text = 'Columns: (between 4-16 even)', font = DEFAULT_FONT)
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
            text = 'First Turn: (Black or White)', font = DEFAULT_FONT)
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
            text = 'Four Discs Arrangement: (Black or White)', font = DEFAULT_FONT)
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
            text = 'Winner Specifier: Winner = (MORE or LESS)', font = DEFAULT_FONT)
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
        
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500, height = 500,
            background = 'blue')
        
        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        #STRING VARIABLE FOR LABEL AND UPDATES
        self._score = tkinter.StringVar(value = 'test string var')
        self._score.set('resized string var test')

        current_score = tkinter.Label(
            master = self._root_window, font = DEFAULT_FONT,
            textvariable = self._score)
        current_score.grid(
            row = 1, column = 0, sticky = tkinter.W)
        
        #BUTTON TO GET USER INPUTS
        button1 = tkinter.Button(
            master = self._root_window, font = DEFAULT_FONT, text = 'GET USER INPUTS',
            command = self._on_button1_clicked)
        button1.grid(
            row = 1, column = 1, 
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        #Draws a rectangle
        rec = self._canvas.create_rectangle(0, 0, 100, 100)
        
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

if __name__ == '__main__':
    app = Layout()
    app.start()
