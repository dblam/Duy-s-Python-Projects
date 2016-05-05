# Steven Vi 74537668 Duy Lam 61502602 Lab 11-12:50 Project 2
# Socket Version

# Host: 192.168.1.101
# Host name: woodhouse.ics.uci.edu
# Port:  4444

import socket
import Console


def input_host():
    ''' Input hostname or ip address'''
    while True:
        require_host = input('Input the host\'s name.\n').strip()
        if len(require_host) == 0:
            print('Try again.')
        else:
            return require_host

def input_port():
    ''' Input port number.'''
    require_port = None
    while require_port == None:
        try:
            require_port = input('Input the port\'s name.\n')
            if int(require_port) > 0 and int(require_port) <= 65535:
                return int(require_port)
            else:
                print('Try again.')
        except ValueError:
            print('That is not a valid port.')
            require_port = None

def username():
    ''' Input username.'''
    while True:
        username = input('Give a username with no spaces between.\n').strip().split()
        if len(username) == 0:
            print('You did not put in a username. Try again')
        elif len(username) == 1:
            for i in username:
                return str(i)
        else:
            print('You have input space into your username. Try again')

def connectSocket() -> 'connection':
    '''Connecting to specified socket'''
    submit = 0
    while submit == 0:
        try:
            host = input_host()
            port = input_port()
            connectfour_socket = socket.socket()
            connect_address = (host, port)
            print('Connecting to server...')
            
            connectfour_socket.connect(connect_address)
            connectfour_socket_input = connectfour_socket.makefile('r')
            connectfour_socket_output = connectfour_socket.makefile('w')
            print('Successfully connected.')
            return(connectfour_socket, connectfour_socket_input, connectfour_socket_output)
        except ConnectionRefusedError:
            print('Cannot connect to server at this time.')
        except socket.gaierror:
            print('Cannot connect to server because internet is down.')
        except TypeError:
            print('Port num is incorrect. Too big.')



def userInterface(connection: 'connection', input_str: str):
    ''' Introduces the user to the server and plays the game
    '''
    s_output = connection[2]
    s_input = connection[1]
    user = username()
    newGameCall = (input_str + ' ' + user)
    send_to_server(s_output, newGameCall)
    print('Client: ' + newGameCall)
    serverReply = receive_from_server(s_input)
    print('Server: ' + (serverReply))
    expectedReply = 'WELCOME ' + user.strip()
    if serverReply == expectedReply:
        newGame = sendGameRequest(connection)
        winner = Console.winner_is_chosen(newGame)
        
        while winner == 0:
            try:
                userCommand = []
                if newGame.turn == 1:
                    clientInput = ''
                    clientInput = input('Client: ')
                    userCommand = (clientInput).split()
                    if len(userCommand) == 2:
                        if 0 < int(userCommand[1]) <= len(newGame[0]):
                            if userCommand[0].lower() == 'drop':
                                newGame = Console.drop_piece(newGame, int(userCommand[1])-1)
                                Console.print_board(newGame)
                                send_to_server(s_output, userCommand[0].upper()+' ' +str(userCommand[1]))
                                print('Server: ', end = '')
                                print(receive_from_server(s_input))
                                winner = Console.winner_is_chosen(newGame)
                                if winner != 0:
                                    print('Game is over.')
                                    break
                            elif userCommand[0].lower() == 'pop':
                                try:
                                    newGame = Console.pop_piece(newGame, int(userCommand[1])-1)
                                    Console.print_board(newGame)
                                    send_to_server(s_output, userCommand[0].upper()+' ' +str(userCommand[1]))
                                    print('Server: ', end = '')
                                    print(receive_from_server(s_input))
                                    winner = Console.winner_is_chosen(newGame)
                                    if winner != 0:
                                        print('Game is over.')
                                        break
                                except:
                                    print('That\'s not a valid move.')
                                    winner = 0
                            else:
                                print('The column number you specified is not correct.')
                                winner = 0       
                        else: 
                            print('The col number you specified is greater.')
                            winner = 0
                    else:
                        print('The move is invalid. Try again')
                        winner = 0
                         
                elif newGame.turn == 2:
                    serverInput = receive_from_server(s_input)
                    serverInput = serverInput.split('\r\n')
                    serverInput = serverInput[0].split()
                    output = str()
                    for i in serverInput:
                        output += i + ' '
                    print('Server: ' + output)
                    if serverInput[0].lower() == 'drop':
                        newGame = Console.drop_piece(newGame, int(serverInput[1])-1)
                        print('Server: ' + receive_from_server(s_input))
                        Console.print_board(newGame)
                        winner = Console.winner_is_chosen(newGame)
                    elif serverInput[0].lower() == 'pop':
                        newGame = Console.pop_piece(newGame, int(serverInput[1])-1)
                        print('Server: ' + receive_from_server(s_input))
                        Console.print_board(newGame)
                        winner = Console.winner_is_chosen(newGame)
                    elif serverInput[0].lower() == 'invalid':
                        print()
                    
                else:
                    print('UserName: ERROR')
            except ValueError:
                print('The number you attempt to put is not correct. Try again.')
                winner = 0
            except TypeError:
                print('The number you tried to input is not correct format.')
                winner = 0

def sendGameRequest(connection: 'connection'):
    ''' Sending game information to server to start the game. '''
    s_output = connection[2]
    s_input = connection[1]
    string = 'AI_GAME' 
    send_to_server(s_output, string)
    print('Client: ' + string)
    serverReply = receive_from_server(s_input)
    if serverReply == 'READY':
        newGame = Console.new_game_state()
        Console.print_board(newGame)
        print('Server: ' +serverReply)
        return newGame
    else:
        print('GameRequest: ERROR')




def send_to_server(connection: 'connection', input_str: str) -> None:
    ''' Send the server the user\'s input'''
    s_output = connection
    s_output.write(input_str + '\r\n')
    s_output.flush() 

def receive_from_server(connection: 'connection') -> None:
    ''' Reads the server\'s input'''
    s_input = connection
    return s_input.readline()[:-1]


def check_client_move(connection: 'connection'):
    ''' Checks if the client move is valid to the server. '''
    s_input = connection
    expectedString = 'OKAY'
    receivedString = receive_from_server(s_input)
    if expectedString == receivedString:
        print('ServerCHECK: '+receivedString)
        
def user_interface():
    pass


if __name__ == '__main__':
    my_connection = connectSocket()
    userInterface(my_connection, 'I32CFSP_HELLO')
    
    
    
    
