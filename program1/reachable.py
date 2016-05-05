import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    temp_list = sorted(file.read().split())
    #print(temp_list)
    return_dict = defaultdict(set)
    for i in temp_list:
        return_dict[i[0:1]].add(i[2:3])
    #print(return_dict)
    return return_dict


def graph_as_str(graph : {str:{str}}) -> str:
    #print(sorted(list(graph)))
    a_String = ''
    for i in sorted(list(graph)):
        a_String += ('  '+i + ' -> ' + str(sorted(list(graph[i]))) + '\n')
    return(a_String)
    #print(a_String)

        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    #while graph.get(start, 0) != 0:
    return_set = set()
    exploring_List = [start]
    while len(exploring_List) != 0:
        for a in exploring_List:
            return_set.add(exploring_List.pop(exploring_List.index(a)))
            destination = [i for i in graph.get(a, '')]
            if len(destination) == 0:
                pass
            else:
                for i in destination:
                    if i not in return_set:
                        exploring_List.append(i)
        if len(exploring_List) == 0:
            break
    if len(return_set) == 1:
        print('Entry Error: \'{0}\'; Illegal: not a source node'.format(return_set.pop()))
    #print(sorted(return_set, reverse = True))
    return(return_set)
        #break
    #for i in a_Set:
    #    a_List.append(i)
    #return(a_Set)





if __name__ == '__main__':
    # Write script here
    file = goody.safe_open('Enter the name of a file with a graph', 'r', 'Illegal file name')
    a = read_graph(file)
    b = graph_as_str(a)
    start_node = input('Enter a name of a starting node:')
    #print(start_node, type(start_node))
    while start_node != None:
        if start_node == 'quit':
            break
        else:
            b = reachable(a, start_node)
            start_node = input('Enter a name of a starting node:')
    #print(a)
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
