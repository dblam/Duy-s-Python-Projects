#Duy B Lam - 61502602


from collections import defaultdict

# Associates grades (str) with grade points (float)
UCI = {'A+': 4.0, 'A': 4.0, 'A-': 3.7,
       'B+': 3.3, 'B': 3.0, 'B-': 2.7,
       'C+': 2.3, 'C': 2.0, 'C-': 1.7,
       'D+': 1.3, 'D': 1.0, 'D-': 0.7,
       'F': 0.0}


def  derivative(f : callable, delta : float) -> callable:
    '''
        Takes a callable function and a float variable value name delta.
        Function returns the derivative function of the callable function with
        delta applied to the equation. 
        Finally, if delta is 0 or negative, an AssertionError will be raised.
    
    try:
        a_Function = lambda x: ((f(x + delta) - f(x)) / delta)
        return a_Function
    except:
        pass
    finally:
        if delta <= 0:
            raise AssertionError
            '''
    assert delta > 0, 'delta('+str(delta)+') must be > 0'
    # assert will run error message only if condition statement is False
    #a short way to catch error by specifying the LEGAL condition
    def d(x):
        return (f(x+delta)-f(x))/delta
    return d
    #return lambda x : (f(x+delta)-f(x))/delta
    #F(G(x))

        
    #NEED TO RAISE EXCEPTION
def keys_with (d : {str:int}) -> callable:  
    '''
        Takes a dictionary d for d['str'] = int and returns a function.
        The returned function returns a set for keys that are associated with 
        that argument.
        
        a = keys_with(d) <- keys_with returns a function that takes an integer value to retrieve keys
        print(a(3))
    a_Function = lambda x: {k for k, v in d.items() if v == x}
    return a_Function'''
    def fn_times (x : int):
        return {k for k,v in d.items() if v == x}
    return fn_times
    #return lambda x : {k for k,v in d.items() if v == x}

def flatten (db : { str: { (str,str) } } ) -> [(str,str,str)]:
    '''
        Takes a dictionary and returns a list of 3-str tuples. 
        Each tuple (str, str, str) will have (ClassName, StudentName, StudentGrade).
    
    a_Set = []
    for k in db.keys():
        for i in (db[k]):
            a_Set.append((str(k), str(i[0]), str(i[1])))
    a_Set = set(a_Set)
    return a_Set
    '''
    return {(c,n,g) for c,v in db.items() for n,g in v}


def roster (db : {str:{(str,str)}}) -> {str:[str]}:
    '''
        Takes a dictionary and returns a dictionary.
        keys = ClassName, values = [StudentNames]->sorted alphabetically
    
    a_Dict = dict()
    for k in db.keys():
        temp = []
        for i in (db[k]):
            temp.append(i[0])
        a_Dict[k] = sorted(temp)
    return a_Dict
    '''
    return {c:[n for n,_g in sorted(ng)] for c,ng in db.items()}
#{c: [list] for c,ng in db.items()}
# list = [n for n,_g in sorted(ng)] -> ng is each value set in keys


def averages (db : {str:{(str,str)}}) -> {str:float}:
    '''
        Takes a dictionary and returns a ditionary.
        keys = ClassName, values = avg(AllStudentsGPA)
    
    a_Dict = dict()
    for k in db.keys():
        grades = 0
        students = 0
        for i in (db[k]):
            grades += UCI[i[1]]
            students += 1
        a_Dict[k] = (grades/students)
    return a_Dict
    '''
    return {c:sum(UCI[g] for _n,g in ng)/len(ng) for c,ng in db.items()}



def grades1 (db : {str:{(str,str)}}) -> {str:[(str,float)]}:
    '''
        Returns a dictionary. 
        keys = ClassName, values = [(StudentName, StudentGrade)] 
            -> sorted by decreasing grade points
    '''
    a_Dict = dict()
    for k in db.keys():
        temp = []
        for i in db[k]:
            temp.append((i[0], UCI[i[1]]))
        a_Dict[k] = sorted(temp, key = lambda x: x[1], reverse = True)
    return a_Dict


def grades2 (db : {str:{(str,str)}}) -> {str:[str]}:
    '''
        Returns a dictionary
        keys = ClassName, values = [StudentName] 
            -> sorted by decreasing grade points
            if two students have the equal grade points, 
            their names must appear in ascending order
    '''
    a_Dict = dict()
    for k in db.keys():
        temp = []
        for i in db[k]:
            temp.append((i[0], UCI[i[1]]))
        a_Dict[k] = sorted(temp, key = lambda x: (-x[1], x[0]), reverse = False)
    for k in a_Dict.keys():
        a = []
        for i in a_Dict[k]:
            a.append(i[0])
        a_Dict[k] = a
    return a_Dict


def student_view (db : {str:{(str,str)}}) -> {str:{(str,str)}}:
    '''
    Returns a dictionary. 
    key = StudentName, values = {(ClassName, StudentGrade)} -> lists all classes taken
    '''
    a_Dict = defaultdict(set)
    for k in db.keys():
        for i in db[k]:
            a_Dict[i[0]].add((k, i[1]))
    return a_Dict
            

def student_averages (db : {str:{(str,str)}}) -> {str:float}:
    '''
    Returns a dictionary.
    key = StudentName, values = StudentGPA -> for all classes taken
    '''
    a_Dict = defaultdict(list)
    for k in db.keys():
        for i in db[k]:
            a_Dict[i[0]].append(UCI[i[1]])
    #print(a_Dict)
    b_Dict = {}
    for k in a_Dict.keys():
        a = 0
        for i in a_Dict[k]:
            a += i
        b_Dict[k] = a / len(a_Dict[k])
    return b_Dict
            
                    
            
    
    
    
    pass
            
 
if __name__ == '__main__':
    from goody import irange
    from math import log
    # Feel free to test other cases as well
    
    
    print('Testing derivative')
    d = derivative (lambda x : 3*x**2 + 2*x - 2, .000001)
    print( [(a,d(a)) for a in irange(0,10)] )
    d = derivative (lambda x : log(x), .000001) # derivative of log(x) is 1/x
    print( [(a,d(a)) for a in irange(1,10)] )
     
    print('\nTesting keys_with')
    d = {'A':3,'B':2,'C':3,'D':2,'E':2,'F':4,'G':1,'H':4}
    kw = keys_with(d)
    print([(x,kw(x)) for x in sorted(set(d.values()))])
    d = {'A':1,'B':4,'C':2,'D':3,'E':1,'F':8,'G':3,'H':6,'I':4,'J':1}
    kw = keys_with(d)
    print([(x,kw(x)) for x in sorted(set(d.values()))])
         
    print('\nTesting flatten')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}} 
    print(flatten(db))
 
    print('\nTesting roster')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}} 
    print(roster(db))
 
    print('\nTesting averages')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}} 
    print(averages(db))
 
    print('\nTesting grades1')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}} 
    print(grades1(db))
 
    print('\nTesting grades2')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B'), ('Zeke','B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}} 
    print(grades2(db))
 
    print('\nTesting student_view')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}} 
    print(student_view(db))
     
    
    print('\nTesting student_averages')
    db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')},
          'Math-3A': {('Bob', 'B'), ('Alice', 'A')}} 
    print(student_averages(db))
     
    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           
