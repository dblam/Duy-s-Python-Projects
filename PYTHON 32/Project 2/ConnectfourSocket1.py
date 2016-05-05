# Steven Vi Duy Lab Project 2
# Socket Version

# Host: 192.168.1.101
# Host name: woodhouse.ics.uci.edu
# Port:  4444

import socket
import Console
import connectfour



def input_host():
    require_host = input('Input the host\'s name.\n').strip()
    return require_host

def input_port():
    require_port = None
    try:
        while require_port == None:
            require_port = input('Input the port\'s name.\n')
            if int(require_port) > 0 and int(require_port) <= 65535:
                return int(require_port)
            else:
                print('Try again.')
    except ValueError:
        print('That is not a valid port.')
        require_port = None

def username():
    username = input('Give a username with no spaces between.\n')
    return username

def connectSocket(host_name: str, port_num: int) -> 'connection':
    s = socket.socket()
    connect_address = (host_name, port_num)
    s.connect(connect_address)
    s_input = s.makefile('r')
    s_output = s.makefile('w')
    print('Successfully connected.')
    return(s, s_input, s_output)
    
    
def introduction(connection: 'connection', input_str: str):
    # This is used to send client introduction to server
    # Use username() function
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
        #print('Server: ' +serverReply)
        #userInput(newGame, connection)
    
        
        while Console.winner_is_chosen(newGame) == connectfour.NONE:

            userCommand = []
            if newGame.turn == 1:
                clientInput = ''
                clientInput = input('Client: ')
                userCommand = (clientInput).split()
                if 0 < int(userCommand[1]) <= len(newGame[0]):
                    if userCommand[0].lower() == 'drop':
                        newGame = Console.drop_piece(newGame, int(userCommand[1])-1)
                        Console.print_board(newGame)
                        send_to_server(s_output, userCommand[0].upper()+' ' +str(userCommand[1]))
                        print(receive_from_server(s_input))
                    elif userCommand[0].lower() == 'pop':
                        newGame = Console.pop_piece(newGame, int(userCommand[1])-1)
                        Console.print_board(newGame)
                        send_to_server(s_output, userCommand[0].upper()+' ' +str(userCommand[1]))
                        print(receive_from_server(s_input))
                else:
                    clientInput = receive_from_server(s_input)
                    print(clientInput)
                     
            elif newGame.turn == 2:
                serverInput = receive_from_server(s_input)
                serverInput = serverInput.split('\r\n')
                serverInput = serverInput[0].split()
                for i in serverInput:
                    print (i, end = ' ')
                print()
                if serverInput[0].lower() == 'drop':
                    newGame = Console.drop_piece(newGame, int(serverInput[1])-1)
                    Console.print_board(newGame)
                    #send_to_server(s_output, serverInput[0].upper()+' ' +str(serverInput[1]))
                    print(receive_from_server(s_input))
                elif serverInput[0].lower() == 'pop':
                    newGame = Console.pop_piece(newGame, int(serverInput[1])-1)
                    Console.print_board(newGame)
                    #send_to_server(s_output, serverInput[0].upper()+' ' +str(serverInput[1]))
                    print(receive_from_server(s_input))
                elif serverInput[0].lower() == 'invalid':
                    print()
                
                #print(Input[:len(Input)])
        else:
            print('UserName: ERROR')
        #return
    #send_to_server(s_output, ('DROP 3'))

    #print('Client: DROP 3')
    #check_client_move(s_input)

def sendGameRequest(connection: 'connection'):
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
    # This is used to send to the server based from user input
    s_output = connection
    #message = (input_str + '\r\n').encode(encoding = 'utf-8')
    #s_output.send(message)
    s_output.write(input_str + '\r\n')
    s_output.flush()
    #my_connection.flush()
##    return connection   

def receive_from_server(connection: 'connection') -> None: # Receive from the server and then send back
    s_input = connection
    return s_input.readline()[:-1]

def server_input_to_gameboard(input_str: str):
    # Use those moves from server and put in on the board
    pass
def print_board(game_state: 'GameState'):
    # This is used to print the board after the server sends their move
    pass

def check_client_move(connection: 'connection'):
    # This is used to check status move after each input
    s_input = connection
    expectedString = 'OKAY'
    receivedString = receive_from_server(s_input)
    if expectedString == receivedString:
        print('ServerCHECK: '+receivedString)
        
def winner_given():
    # This is used to check whether player or server has won
    pass


if __name__ == '__main__':
    host = input_host()
    port = input_port()
    my_connection = connectSocket(host, port)
    #print(my_connection)
    #s = my_connection[0]
    #s_input = my_connection[1]
    #s_output = my_connection[2]
    introduction(my_connection, 'I32CFSP_HELLO')
    
    
    
    
