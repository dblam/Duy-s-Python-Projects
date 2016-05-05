from functools import reduce # for use in peaks
from tkinter.constants import RIGHT

def separate(p,l):
    '''
    takes a predicate = (bool) and a list
    returns a 2tuple([list of 'True' values], [list of 'False' values]
    '''
    a = []
    b = []
    try:
        if len(l) != 0:
            a = [i for i in l if p(i) == True]
            b = [i for i in l if p(i) == False]
            separate(p, l)
        else: return((list(),list()))
    except:pass
    finally: return((a,b))
    
    
                

def is_sorted(s):
    '''
    takes a list
    returns a bool=True if values in list are in non-decending order
        lowest to highest allowing repetitions
    '''
    bool_val = True
    try:
        if len(s) != 0:
            one = s[0]
            extra_s = s[1:]
            two = extra_s[0]
            if one <= two: bool_val = is_sorted(extra_s)
            else: bool_val = False
        else: bool_val = True
    except: pass
    finally: return bool_val
    
def sort(l):
    '''
    1. takes a list
    2. returns a list in descending order
    '''
    if is_sorted(l): return(l)
    a = l[0]
    b = [[i for i in l[1:] if i <= a],[i for i in l[1:] if i > a]]
    if len(b[0]) and len(b[1]) != 0:
        if b[1][0] > a:b[0].append(a)
        else:b[1].append(a)
    if len(b[0]) == 0:b[0] = [a]
    if len(b[1]) == 0:b[1] = [a]
    c = sort(b[0]) + sort(b[1])
    return(c)

def compare(a,b):
    '''
    takes two str arguments -> a,b
    returns one of three values ('<', '=', '>')
        ->indicates the relationship between the first and second parameter
    '''
    if len(a) == 0: 
        if len(b) == 0:return '='
        else: return '<'
    if len(b) == 0:return '>'
    if a[0] < b[0]: return '<'
    if a[0] > b[0]: return '>'
    #if a[0] == b[0]: return '='
    return(compare(a[1:], b[1:]))
 
def triple(x,y): 
    '''
    calling reduce from peaks with this function converts alll interable
    values into overlapping triples 
    '''
    if len(x[0]) < 3:
        x[0].append(y)
    else: x.append([x[len(x)-1][1], x[len(x)-1][2], y])
    return(x)

def peaks(alist):
    '''
    takes an iterable
    returns a list of int for values that are bigger than 
    the value preceding and following them
    ex: peaks([0,1,-1,3,8,4,3,5,4,3,8]) 
        -> returns [1,8,5]
        return list contains values strictly bigger than the value 
        preceding and following them 
        iterable -> alist
    '''
    reduced   = reduce(triple, alist, [[]])#reduce produces a list of triples: note []
    if len(reduced[0]) < 3: return list()
    filtered  = filter((lambda x: x[0]<x[1] and x[1]>x[2]), reduced)    #filter out triples not representing peaks
    mapped   = map((lambda x: x[1]), filtered)    #map triple to its middle value
    return list(mapped)                     #map is a generator; store its values in list 
    




if __name__=="__main__":
    import predicate,random,driver
    from goody import irange
    
    print('Testing separate')
    print(separate(predicate.is_positive,[]))
    print(separate(predicate.is_positive,[1, -3, -2, 4, 0, -1, 8]))
    print(separate(predicate.is_prime,[i for i in irange(2,20)]))
    print(separate(lambda x : len(x) <= 3,'to be or not to be that is the question'.split(' ')))
     
    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))
    
    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = [i+1 for i in range(30)]
    random.shuffle(l)
    print(l)
    print(sort(l))
    
    print('\nTesting compare')
    print(compare('','abc'))
    print(compare('abc',''))
    print(compare('',''))
    print(compare('abc','abc'))
    print(compare('bc','abc'))
    print(compare('abc','bc'))
    print(compare('aaaxc','aaabc'))
    print(compare('aaabc','aaaxc'))
    
    print('\nTesting triple and peaks')
    print(triple([[]],'a'))
    print(triple([['a']],'b'))
    print(triple([['a','b']],'c'))
    print(triple([['a','b','c']],'d'))
    print(triple([['a','b','c'],['b','c','d']],'e'))
    print(triple([['a','b','c'],['b','c','d'],['c','d','e']],'f'))
    
    print(peaks([0,1,-1,3,8,4,3,5,4,3,8]))
    print(peaks([5,2,4,9,6,1,3,8,0,7]))
    print(peaks([1,2,3,4,5]))
    print(peaks(int(predicate.is_prime(p)) for p in irange(1,20)))
    
    driver.default_file_name = 'bsc.txt'
#     driver.default_show_traceback         = True
#     driver.default_show_exception         = True
#     driver.default_show_exception_message = True
    driver.driver()
    
