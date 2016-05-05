# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v
        
def start_when(iterable,p):
    '''
    1. takes an iterable item and a predicate
        predicate - fuction of one argument that returns a bool
    2. produces every value from the iter item from first value
        note: predicate should return True
    ex: for i in start_when('combustible', lambda x: x >= 'q'):
            print(i, end = '')
                -> returns 'ustible: u is the fist char > than q
    '''
    temp_iter = iter(iterable)
    bin = []
    while True:
        try:
            a = next(temp_iter)
            if p(a) == True:
                bin.append(a)
                break
        except: pass
    while True:
        try: bin.append(next(temp_iter))
        except: break
    for i in bin: yield i
    '''    
    temp_bin = [e for e in iterable]
    start_i = 0
    for i in range(len(temp_bin)):
        if p(temp_bin[i]) == True:
             start_i = i
             break
    bin = temp_bin[start_i:]
    yield ('').join(bin)'''
          
def differences(iterable1,iterable2):
    '''
    1. takes two iterable items
    2. If a char from one iter item doesn't match the other compared by index:
        function produces 3tuple(index, char(iterable1[index]), char(interable2[index]) for each mismatch
    ex: for i in differences('3.14159265', '3x14129285'):
            print(i, end='')
                ->returns (2, '.', 'x') (6, '5', '2') (9, '6', '8')
    '''
    temp_bin1 = tuple(enumerate(iterable1, start=1))#[e for e in iterable1]
    temp_bin2 = tuple(enumerate(iterable2, start=2))#[e for e in iterable2]
    temp_combine = tuple(zip(temp_bin1, temp_bin2))
    print(temp_combine)
    #bin = []
    for element in temp_combine:
        if element[0][1] != element[1][1]:
            yield((element[0][0], element[0][1], element[1][1]))
    '''for i in range(len(temp_bin1)):
        if temp_bin1[i] != temp_bin2[i]:
            if type(temp_bin1[i]) and type(temp_bin2[i]) is int:
                bin.append((i+1, (temp_bin1[i]), (temp_bin2[i])))
            else:bin.append((i+1, str(temp_bin1[i]), str(temp_bin2[i])))
    for i in bin:
        yield i'''
   

                       
def once_in_a_row(iterable):
    '''
    1. takes an iter item
    2. produces every value form iterable BUT never the same value twice in a row
    ex: for i in once_in_a_row(hide('abcccaaabddeee')):
            print(i,end='')
                -> returns  abcabde
    '''
    '''
    temp_bin = [e for e in iterable]
    bin = []
    for i in range(len(temp_bin) - 1):
        if temp_bin[i] != temp_bin[i+1]:
            bin.append(temp_bin[i])
    if temp_bin[len(temp_bin) - 1] != bin[len(bin) - 1]:
        bin.append(temp_bin[len(temp_bin) - 1])
    for i in bin:
        yield i'''
    '''
    prev_element = str()
    iter_item = iter(iterable)
    for element in iter_item:
        if element == prev_element:
            prev_element = element
        else:
            prev_element = element
            yield prev_element'''
    test_char = ''
    while test_char == '':
        try:
            my_iter = iter(iterable)
            for character in my_iter:
                if test_char == character:
                    test_char = character
                elif test_char != character:
                    test_char = character
                    yield_value = character
                    yield yield_value
                else:pass
        except: print('one in row fuction while loop ERROR')
        finally: test_char = iterable
            

         
def alternate(*args):
    '''
    1. takes any number of iterables as parameters
    2. returns each value of each iterble item for all items
    ex: for i in alternate_all('abcde','fg','hijk'): 
            print(i,end='')
                -> return afhbgic
    '''
    bin = []
    iter_list = []
    for i in args:
        b = iter(a for a in i)
        iter_list.append(b)
    while True:
        try:
            for it in iter_list:
                bin.append(next(it))
        except: break
    for i in bin:
        yield i
        
def windows(iterable,n,m=1):
    '''
    1. takes an iter item and two ints
    2. produces lists of: using n for list values and m for recurrence values
    ex: for i in windows('abcdefghijk', 4,2):
            print(i,end='') 
                -> returns ['a','b','c','d'] 
                            ['c','d','e','f'] 
                            ['e','f','g','h'] 
                            ['g','h','i','j']
    '''
    
    #temp_bin = iter([e for e in iterable])
    temp_bin = iter(iterable)
    bin = [[next(temp_bin) for i in range(n)]]
    while True:
        try:
            a = (bin[len(bin) - 1][m:]) #[]
            #a.extend(bin[len(bin) - 1][m:])
            while len(a) < n:
                a.extend(next(temp_bin))
            bin.append(a)
        except:break
    for i in bin:
        yield i
    
        
def ascending(n,iterable):
    '''
    1. takes an integer and an iter item (all comparable)
    2. returns list[tuple(int, int)]
        whose values are the first and last values in a sequence that ascends
        for n or more numbers
    ex: ascending(3,[5,5,2,4,6,2,4])
            -> returns [(2,6)]
    ex2: ascending(3,[2,3,1,4,6,7,2,0,2,4,3])
            -> returns [(1,7), (0, 4)]
    NOTE: raise AssertionError if n < 2
    '''
    
    assert n >= 2, 'n less than 2'
    bin = []
    a = iter(iterable)
    start = next(a)
    prev = start
    curr = next(a)
    up = 1
    while True:
        try:
            if prev > curr:
                if up >= n:
                    if start != prev:
                        bin.append((start, prev))
                    start = curr
                    prev = start
                    curr = next(a)
                    up = 2
                if up < n:
                    start = curr
                    prev = curr
                    curr = next(a)
                    up = 1
            if prev < curr:
                #if up >= n:print('found {0} {1}'.format(start, curr))
                prev = curr
                curr = next(a)
                up += 1
            if prev == curr:
                start = curr
                prev = curr
                curr = next(a)
                up += 1
        except: 
            if start < curr:
                if up+1 >= n:
                    bin.append((start, curr))
            #print('found {0} {1} {2} {3}'.format(prev, start, curr, up))
            break
    return(bin)
    
    

 
 

if __name__ == '__main__':
    from goody import irange
    
    # Test start_when; you can add your own test cases
    print('Testing start_when')
    for i in start_when('combustible', lambda x : x >= 'q'):
        print(i,end='')
    print('\n')

    print('Testing start_when on hidden')
    for i in start_when(hide('combustible'), lambda x : x >= 'q'):
        print(i,end='')
    print('\n\n')
    
    
    # Test differences; you can add your own test cases
    print('Testing differences')
    for i in differences('3.14159265', '3x14129285'):
        print(i,end=' ')    
    print('\n')

    print('Testing differences on hidden')
    for i in differences(hide('3.14159265'), hide('3x14129285')):
        print(i,end=' ')    
    print('\n\n')

              
    # Test once_in_a_row; you can add your own test cases
    print('Testing once_in_a_row')
    for i in once_in_a_row('abcccaaabddeee'):
        print(i,end='')    
    print('\n')

    print('Testing once_in_a_row on hidden')
    for i in once_in_a_row(hide('abcccaaabddeee')):
        print(i,end='')    
    print('\n\n')

              
    # Test alternate; you can add your own test cases
    print('Testing alternate')
    for i in alternate('abcde','fg','hijk'):
        print(i,end='')
    print('\n')
    
    print('Testing alternate on hidden')
    for i in alternate(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print('\n\n')
       
         
    # Test windows; you can add your own test cases
    print('Testing windows')
    for i in windows('abcdefghijk',4,2):
        print(i,end=' ')
    print('\n')
    
    print('Testing windows on hidden')
    for i in windows(hide('abcdefghijk'),4,2):
        print(i,end=' ')
    print('\n\n')
       
    
    # Test ascending; add your own test cases
    print('Testing ascending')
    print('  on [5,5,2,4,6,2,4]')
    print('n=2:',ascending(2,[5,5,2,4,6,2,4]))
    print('n=3:',ascending(3,[5,5,2,4,6,2,4]))
    print('n=4:',ascending(4,[5,5,2,4,6,2,4]))
    print()

    print('  on [2,3,1,4,6,7,2,0,2,4,3]')
    print('n=2:',ascending(2,[2,3,1,4,6,7,2,0,2,4,3]))
    print('n=3:',ascending(3,[2,3,1,4,6,7,2,0,2,4,3]))
    print('n=4:',ascending(4,[2,3,1,4,6,7,2,0,2,4,3]))
    print('n=5:',ascending(5,[2,3,1,4,6,7,2,0,2,4,3]))
    print()

    print('  on [1,2,1,2,3]')
    print('n=2:',ascending(2,[1,2,1,2,3]) )
    print('n=3:',ascending(3,[1,2,1,2,3]) )
    print('n=4:',ascending(4,[1,2,1,2,3]) )
    print()

    print('  hidden testing')
    print(ascending(2,hide([5,5,2,4,6,2,4])))
    print(ascending(3,hide([2,3,1,4,6,7,2,0,2,4,3])))
    print(ascending(2,hide([1,2,1,2,3])))
    print('\n')
    

         
         
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
