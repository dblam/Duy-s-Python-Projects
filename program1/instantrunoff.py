import goody
from collections import defaultdict

def read_voter_preferences(file : open):
    '''
        Uses file argument to return a dictionary.
        key = each voter, value = voter preference 
    '''
    temp_list = sorted(file.read().split())
    return_Dict = defaultdict(list)
    for i in range(len(temp_list)):
        i_list = (temp_list[i]).split(';')
        #print(i_list)
        return_Dict[i_list[0]] = ((i_list[1:]))
    #print(return_Dict)
    return return_Dict
    
    


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    '''
    Function is used to print voter preference dictionary and vote count dictionary
    for each ballot.
    
        returns a 'multi-line' string of all Voter Preferences
        key -> determines the ordering
        bool -> determines 'Reverse = True/False' of order format
    '''
    return_String = ''
    a = (sorted(d, key = key, reverse = reverse))
    #print(a)
    for i in a:
        return_String += '  {0} -> {1}\n'.format(i, d[i])
        #return_String += '  {0} -> {1}\n'.format(i[0], i[1])
    #print(return_String)
    return return_String


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    '''
        vp = dict -> voter preferences from read_voter_preferences()
        cie = set -> remaining candidates
    function returns a dictionary
        key = candidate, value = number of votes received on current ballot
        note: count only 1 vote per voter
    '''
    return_Dict = {}
    for i in cie:
        return_Dict[i] = 0
    for voter in vp:
        for e in range(len(vp[voter])):
            if vp[voter][e] in cie:
                return_Dict[vp[voter][e]] += 1
                break
    return return_Dict
        


def remaining_candidates(vd : {str:int}) -> {str}:
    '''
        vd = dictionary -> key = candidate, value = votes count
    function returns a set of candidates after removing least vote count candidate.
    '''
    return_Set = {k for k,v in vd.items() if v != min(vd.values())}
    return return_Set

    
        
        


def run_election(vp_file : open) -> {str}:
    '''
    function takes vp_file and incorporates all functions above 
    to process votes completely
    '''
    RVP_return = read_voter_preferences(vp_file)
    ballot_count = 1
    return_String = dict_as_str(RVP_return)
    print('Voter Preferences\n{0}'.format(return_String))
    candidates = set([v for v in RVP_return.values()][0])
    votes_rank = evaluate_ballot(RVP_return, candidates)
    while len(candidates) != 1 or 0 or None:
        print('Vote count on ballot #{0} with candidates (alphabetical order): remaining candidates = {1}'.format(ballot_count,candidates))
        print(dict_as_str(votes_rank))
        print('Vote count on ballot #{0} with candidates (numerical order): remaining candidates = {0}'.format(ballot_count,candidates))
        print(dict_as_str(votes_rank, key=lambda x: votes_rank[x], reverse=True))
        candidates = remaining_candidates(votes_rank)
        votes_rank = evaluate_ballot(RVP_return, candidates)
        ballot_count += 1
        if len(candidates) == 0:
            break
    
    
    print('Winner is ',{k for k in votes_rank.keys()})
    return {k for k in votes_rank.keys()}

  
  
  
  
    
if __name__ == '__main__':
    # Write script here
    file = goody.safe_open('Enter name of a file with voter preferences',
                           'r','Illegal file name')                 
    a = run_election(file)
    
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
