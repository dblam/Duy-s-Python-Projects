import goody
from collections import defaultdict


def read_fa(file : open) -> {str:{str:str}}:
    '''
        returns a dictionary -> finite automation
        key = start state, value = {key = number input: value: new state}
    '''
    file_lines = file.read().split('\n')
    return_dict = defaultdict(dict)
    for line in file_lines:
        a = line.split(';')
        b = []
        c = []
        for i in range(1, len(a)):
            if (i%2) == 0:
                b.append(a[i])
            else:
                c.append(a[i])
        if a[0] != '':
            return_dict[a[0]] = dict(zip(c,b))
    #print(return_dict)
    return (return_dict)


def fa_as_str(fa : {str:{str:str}}) -> str:
    '''
        takes dictionary built by read_fa function and
        returns a string with each line separated by '\n'
    format: "  even transitions: [('0', 'even'), ('1', 'odd')]\n 
             odd transitions: [('0', 'odd'), ('1', 'even')]\n"
    
    return_string = ''
    for default_state in fa:
        return_string += '  {0} transitions: ['.format(default_state)
        for num_input, new_state in fa[default_state].items():
            return_string += '(\'{0}\', \'{1}\'), '.format(num_input, new_state)
            #print(default_state, num_input, new_state)
        return_string = return_string.rstrip(', ') + ']\n'
    #print(return_string)
    return(return_string)
    '''
    return_string = ''
    for default_state in sorted(fa.keys()):
        return_string += '  {0} transitions: ['.format(default_state)
        for num_input in sorted(fa[default_state].keys()):
            return_string += '(\'{0}\', \'{1}\'), '.format(num_input, fa[default_state][num_input])
            #print(default_state, num_input, new_state)
        return_string = return_string.rstrip(', ') + ']\n'
    #print(return_string)
    return(return_string)

def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    '''
        function takes fa dictionary, state as 'startstate', and list of inputs as arguments
    returns a list = ['startstate', tuple('userinput', 'newstate')]
    '''
    try:
        return_list = [state]
        current_state = state
        for i in range(len(inputs)):
            inputs[i] = inputs[i].strip()
            if fa[current_state][inputs[i]] != current_state: #a
                return_list.append((inputs[i], fa[current_state][inputs[i]]))
                current_state = fa[current_state][inputs[i]]
            else:
            #elif fa[current_state][inputs[i]] == current_state: #b
                return_list.append((inputs[i], current_state))
            #else:
                #return_list.append((inputs[i], None))
                #return return_list
        #print(temp_tuple)
        return(return_list)
    except KeyError:
        #print('{0} ->> NONE'.format(fa['odd'][inputs[i]]))
        return_list.append((inputs[i], None))
        return return_list

def interpret(fa_result : [None]) -> str:
    '''
        function takes list created by F(process) to show: 
        the processing of inputs and its starting state
    returns a string of each step separated by '\n'
    '''
    return_string = 'Start state = {0}\n'.format(fa_result[0])
    for i in range(1, len(fa_result)):
        if fa_result[i][1] == None:
            return_string += '  Input = {0}; illegal input: simulation terminated\n'.format(fa_result[i][0])
        else:
            return_string += '  Input = {0}; new state = {1}\n'.format(fa_result[i][0], fa_result[i][1])
    return_string += 'Stop state = {0}\n'. format(fa_result[len(fa_result) - 1][1])
    return(return_string)
    



if __name__ == '__main__':
    # Write script here
    file = goody.safe_open('Enter the name of a file with a finite automation', 'r', 'FA FILE : FILE NOT FOUND')
    r_fa = read_fa(file)
    r_fa_str = fa_as_str(r_fa)
    print('\nFinite Automation\n'+r_fa_str)
    file2 = goody.safe_open('Enter the name of a file with the start-state and input', 'r', 'START STATE AND INPUT : FILE NOT FOUND')
    simulation_list = file2.readlines()
    for line in simulation_list:
        print('\nStarting new simulation')
        line_list = line.split(';')
        test_list = line_list[1:]
        r_process = interpret(process(r_fa, line_list[0], test_list))
        #print(simulation_list)
        print(r_process)
    
    #r_process = process(r_fa, 'even', ['1','0','1'])
    #interpret(r_process)
    
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
