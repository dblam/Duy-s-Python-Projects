import goody
from collections import defaultdict


def read_ndfa(file : open) -> {str:{str:{str}}}:
    '''
       returns dictionary1 (key = state, value = dictionary2)
           dictiondary2 (key = input, value = set of states input can lead to)
   '''
    return_dict = {}
    file_list = file.read().split()
    for line in file_list:
        line_list = line.split(';')
        temp_dict = defaultdict(set)
        for i in range(1, len(line_list)):
            if ((i+1) % 2) == 0: #for i = odd
                temp_dict[line_list[i]].add(line_list[i+1])
        return_dict[line_list[0]] = dict(temp_dict)
    return(return_dict)


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    '''
    function takes dict returned from F(read_ndfa) as a parameter
    returns a string representing the contents of NDFA
    end transitions: []\n  near transitions: [('1', ['end'])]\n  
      start transitions: [('0', ['near', 'start']), ('1', ['start'])]\n"
    '''
    return_string = ''
    for state in sorted(ndfa):
        a = sorted([(k, sorted(v)) for k,v in ndfa[state].items()])
        return_string += '  {0} transitions: {1}\n'.format(state, a)
    return(return_string)

def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    '''
     function takes dictionary returned by F(read_ndfa), a start state, and list of inputs
        returns ['begin state', ('input num', {'resulting state',...}),...]
    '''
    return_list = [state]
    current_state = [state]
    for i in range(len(inputs)):
        result_set = []
        for state in current_state:
            if state in ndfa:
                if inputs[i] in ndfa[state]:
                    result_set.extend(sorted(list(ndfa[state][inputs[i]].copy())))
        return_list.append((inputs[i], set(result_set)))
        if len(result_set) == 0: break
        current_state = result_set[:]
    return(return_list)
    
    
def interpret(result : [None]) -> str:
    '''
   function takes list created by F(process) to display results
   return a one line string that split each display line by '\n'
   example:
   "Start state = start\n
      Input = 1; new possible states = ['start']\n
      Input = 0; new possible states = ['near', 'start']\n
      Input = 1; new possible states = ['end', 'start']\n
      Input = 1; new possible states = ['start']\n
      Input = 0; new possible states = ['near', 'start']\n
      Input = 1; new possible states = ['end', 'start']\n
    Stop state(s) = ['end', 'start']\n"
    '''
    return_string = 'Start state = {0}\n'.format(result[0])
    for i in range(1, len(result)):
        return_string += '  Input = {0}; new possible states = {1}\n'.format(result[i][0], sorted(result[i][1]))
    return_string += 'Stop state(s) = {0}\n'. format(sorted(result[len(result) - 1][1]))
    return(return_string)

if __name__ == '__main__':
    # Write script here
    file1 = goody.safe_open('Enter the name of a file with a non-deterministic finite automation', 'r', 'NDFA FILE NOT FOUND')
    r_read_ndfa = read_ndfa(file1)     
    s = ndfa_as_str(r_read_ndfa)
    print('\nNon-Deterministic Finite Automation\n' + s)
    file2 = goody.safe_open('Enter the name of a file with the start-state and input', 'r', 'NDFA FILE NOT FOUND')
    file2_list = file2.read().split('\n')
    print()
    for e in file2_list:
        temp_list = e.split(';')
        r_process = process(r_read_ndfa, temp_list.pop(0), temp_list)     
        s = interpret(r_process)
        print('Starting new simulation\n'+s)
        
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
