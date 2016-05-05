from collections import defaultdict


class History:
    def __init__(self):
        self._history = defaultdict(list)

    
    def __getattr__(self,name):
        temp = name.count('_prev')
        assert temp == 0 or name.endswith('_prev'), NameError
        r_name = name[: -5*temp]
        assert r_name in self._history, NameError
        o = self._history[r_name]
        #return (o[-temp-1] if back < len(o) else None)
        


    def __getitem__(self,index):
        assert index < 0, AssertionError('_History.__getitem__')
        return {k:v[index-1] if abs(index) < len(v) else None for k,v in self._history.items()}

    
    def __setattr__(self,name,value):
        #print('C.__setattr__', name, value)
        if name.find('_rev') != -1: 
            raise NameError('_History.__setattr__: name({0}) cannot conntain _prev'.format(name))
        if '_history' in self.__dict__:
            self._history[name].append(value)
        self.__dict__[name] = value
        # Until you put code here, self.n = v will do nothing,
        # because __setattr__ does nothing.




if __name__ == '__main__':
    # Put in simple tests for History before allowing driver to run

    print()
    import driver
    
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
