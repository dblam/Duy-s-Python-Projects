from goody import type_as_str
from builtins import IndexError, AttributeError
from math import floor

class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        assert 0 <= hour <=23 and type(hour)==int, (AssertionError, 'hour: {0} is not in correct format'.format(hour))
        assert 0 <= minute <= 59 and type(minute)==int, (AssertionError, 'minute: {0} is not in correct format'.format(minute))
        assert 0 <= second <= 59 and type(second)==int, (AssertionError, 'second: {0} is not in correct format'.format(second))
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __getitem__(self,index):
        if type(index) is not tuple:
            index =(index,)
        if not all(type(i) is int and 1<=i<=3 for i in index):
            raise IndexError('Time.__getitem__: illegal argument in '+str(index))
        answer = tuple(self.hour if i==1 else self.minute if i==2 else self.second for i in index)
        if len(answer)==1:
            answer = answer[0]
        return answer
        '''
    def __getitem__(self, index):
        if (type(index) is int) and (index == 1 or 2 or 3):
            if index == 1:
                return self.hour
            if index == 2:
                return self.minute
            if index == 3:
                return self.second
        if (type(index) is tuple):
            return_tuple = []
            for i in index:
                if (type(i) is int) and (i == 1 or 2 or 3):
                    if i == 1:
                        return_tuple.append(self.hour)
                    if i == 2:
                        return_tuple.append(self.minute)
                    if i == 3:
                        return_tuple.append(self.second)
                if i > 3 or i < 1:raise IndexError
            return tuple(return_tuple)
        else:raise IndexError'''
    
    def __repr__(self):
        return('Time({0},{1},{2})'.format(self.hour, self.minute, self.second))
    
    def __str__(self):
        am_pm = ''
        if 0 < self.hour <= 12:
            am_pm = 'am'
        if self.hour >= 12:
            am_pm = 'pm'
            if self.hour > 12:
                self.hour -= 12
        if self.hour == 0:
            am_pm = 'am'
            self.hour = 12
        return('{0}:{1:02d}:{2:02d}{3}').format(self.hour, self.minute, self.second, am_pm)
    def __bool__(self):
        return self.hour != 0 or self.minute != 0 or self.second != 0
#         if (self.hour == 0):
#             if (self.minute == 0):
#                 if (self.second == 0):
#                     return False
#         return True
    
    def __len__(self):
        return(int(self.hour*60*60 + self.minute*60 + self.second))
    
    def __lt__(self, right):
        if type(right) == float: raise TypeError
        self_v = int(self.hour*60*60 + self.minute*60 + self.second)
        if type(right) is not int:
            right_v = int(right.hour*60*60 + right.minute*60 + right.second)
        else:
            right_v = right
        return(self_v < right_v)
    def __eq__(self, right):
        return type(right) is Time and self[1,2,3] == right[1,2,3]
#         if type(right) == float: raise TypeError
#         self_v = int(self.hour*60*60 + self.minute*60 + self.second)
#         if type(right) is not int:
#             right_v = int(right.hour*60*60 + right.minute*60 + right.second)
#         else:
#             right_v = right
#         return(self_v == right_v)
    
    def __add__(self, right):
        return_sec = 0
        if type(right) is float:raise TypeError
        if type(right) is int:
            return_sec = int(self.hour*60*60 + self.minute*60 + self.second) + right 
        if type(right) is not int:
            return_sec = int((self.hour*60*60 + self.minute*60 + self.second)
                          + (right.hour*60*60 + right.minute*60 + right.second))
        if return_sec >= (86400):
            return_sec -= (86400)
        hour = floor(return_sec/60/60)
        minute = int(floor(return_sec/60) - (hour*60))
        second = return_sec - (hour*60*60 + minute*60)
        if hour == 0: hour = 12
        if hour > 12: hour -= 12
        am_pm = 'am'
        return('{0}:{1:02d}:{2:02d}{3}').format(hour, minute, second, am_pm)
    
    def __radd__(self, left):
        '''
        return_sec = left
        if type(left) is float:raise TypeError
        if type(left) is int:
            return_sec += (self.hour*60*60 + self.minute*60 + self.second)
        #if type(left) is not int:
           # return_sec = int((self.hour*60*60 + self.minute*60 + self.second)
            #              + (left.hour*60*60 + left.minute*60 + left.second))
        if return_sec >= (86400):
            return_sec -= (86400)
        hour = floor(return_sec/60/60)
        minute = int(floor(return_sec/60) - (hour*60))
        second = return_sec - (hour*60*60 + minute*60)
        if hour == 0: hour = 12
        if hour > 12: hour -= 12
        am_pm = 'am'
        return('{0}:{1:02d}:{2:02d}{3}').format(hour, minute, second, am_pm)'''
        return self + left
    
    def __call__(self, hour, minute, second):
        '''
        assert 0 <= hour <=23 and type(hour)==int, (AssertionError, 'hour: {0} is not in correct format'.format(hour))
        assert 0 <= minute <= 59 and type(minute)==int, (AssertionError, 'minute: {0} is not in correct format'.format(minute))
        assert 0 <= second <= 59 and type(second)==int, (AssertionError, 'second: {0} is not in correct format'.format(second))
        self.hour = hour
        self.minute = minute
        self.second = second'''
        self.__init__(hour, minute, second)
    
if __name__ == '__main__':
    # Put in simple tests for Time before allowing driver to run
    new = Time(10,10,10)
    
    repr(new)
    
    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()



        
        
        
        
        
