import re

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. 

# Use days_in and is_leap_year in your advance_to function

day_dict ={ 1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
           10 : 31, 
           11 : 30,
           12 : 31} 

def is_leap_year(month:int)->bool:
    return (month%4 == 0 and month%100 != 0) or month%400==0

def days_in(month:int, year:int)->int:
    return (29 if month==2 and is_leap_year(year) else day_dict[month])


def future_date(date:str, advance:int, year_now:int) -> str:
    '''
    takes a string = possible date, 
        advance = # of days, year_now = current year
    returns a string representing the future date
    ex:
        future_date('3/27/16', 10, 2016)
        returns: '4/6/16'
        OR
        future_date('3/27', 10, 2016)
        returns: '4/6'
    Note:
        raise AssertionError IF:
            date:str is illegal
            by specification in 2a 
            or day specified is not in month (leaf year)
        &
            IF: advance is negative
    '''
    date_specification = '^([1-9]|1[0-2])\/(\s?[1-9]|[0-2][0-9]|3[0-1])(?:\/([0-9]{2}))?$'
    result = re.match(date_specification, date)
    assert result != None, 'input date does not match 2a specifications'
    result_list = result.group().split('/')
    
    current_date = int(result_list[1])
    current_month = int(result_list[0])
    current_year = year_now % 100 #int(str(year_now)[2:]) -> another way to collect the last 2 digit of a 4-digits number
    
    if len(result_list) == 3: current_year = int(result_list[2])
    assert current_date <= days_in(current_month, current_year), 'date does not match calendar'
    assert advance >= 0, 'cannot advance with a non-positive input'
    day_dict_copy = day_dict.copy()
    while advance != 0:
        if is_leap_year(current_year): day_dict_copy[2] = 29
        if (current_date + advance) > (day_dict_copy[current_month]):
            advance -= (day_dict_copy[current_month] - current_date + 1)
            current_date = 1
            if current_month == 12: 
                current_month = 1 
                current_year += 1
            else: current_month += 1
        if (current_date + advance) <= (day_dict_copy[current_month]): 
            current_date += advance
            advance = 0
        day_dict_copy[2] = 28
    if len(result_list) == 3:
        return(('/').join([str(current_month), str(current_date), str(current_year)]))
    else:
        return(('/').join([str(current_month), str(current_date)]))
        
    
    
    
    

def compare_files(f1 : open, f2 : open) -> [(int,str,str)]:
    '''
    function takes 2 text files as parameters and compares the two by each line
        comparison will end when one file does not have a line to match with the other
    returns an list of tuples -> [(int, str, str),...]
        each tuple = (line#, f1_line, f2_line)
    '''
    return_list = []
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()
    r_total = (len(f2_lines) if len(f2_lines) < len(f1_lines) else len(f1_lines))
    for i in range(r_total):
        if re.match(f1_lines[i], f2_lines[i]) == None:
            return_list.append(((i+1), f1_lines[i].strip(), f2_lines[i].strip()))
    return(return_list)
    
    



    
if __name__ == '__main__':
    # Put your own function calls here to test the regular expressions
    #   or functions
   
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
