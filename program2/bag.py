# Submitter: dblam(Lam, Duy)
# Partner  : cindyt9(Tran, Cindy)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from collections import defaultdict
from goody import type_as_str


class Bag:
    def __init__(self, iter_item = []):
        r_dict = {}
        for item in iter_item:
            if item in r_dict:
                r_dict[item] += 1
            else: r_dict[item] = 1
        self.iter_item_dict = r_dict
        self.iter_item = (iter_item)
        #self.iter_index = len([k for k in self.iter_item_dict for i in range(self.iter_item_dict[k])]) - 1
        self.variable = ''
    def __repr__(self):
        return('Bag({0})'.format(str([k for k in self.iter_item_dict for i in range(self.iter_item_dict[k])])))
   
    def __str__(self):
        return_tuple = ','.join(k + '[' + str(v) + ']' for k,v in self.iter_item_dict.items())
        return('Bag({0})'.format(return_tuple))
    
    def __len__(self):
        sum_o = 0
        for v in self.iter_item_dict.values():
            sum_o += v 
        return(sum_o)
    
    def unique(self):
        return(len(self.iter_item_dict.keys()))
    
    def count(self, x):
        if x in self.iter_item_dict.keys():
            return(self.iter_item_dict[x])
        else: return 0
        
    def add(self, x):
        if x in self.iter_item_dict.keys():
            self.iter_item_dict[x] += 1 #pretty much all we need for this function
        else: self.iter_item_dict[x] = 1
        
    def __contains__(self, item):
        return item in self.iter_item_dict
    
    def __add__(self, right):
        if (type(self) and type(right)) is not Bag: raise TypeError('argument is not of type Bag')
        a = [k for k in self.iter_item_dict for i in range(self.iter_item_dict[k])]
        a.extend([k for k in right.iter_item_dict for i in range(right.iter_item_dict[k])])
        return Bag(a)
    
    def remove(self, x):
        if self.iter_item_dict[x] == 0:
            trash_x = self.iter_item_dict.pop(x)
        else: self.iter_item_dict[x] -= 1
        if x not in self.iter_item_dict: raise ValueError('DID NOT FIND X')
        
    def __eq__(self,right):
        if (type(self) and type(right)) is not Bag: return False
        return self.iter_item_dict == right.iter_item_dict
    
    def __iter__(self):
        c_list = ([k for k in self.iter_item_dict for i in range(self.iter_item_dict[k])])
        def generator(x):
            for e in x:
                yield e
        return generator(c_list)
    
        
            

if __name__ == '__main__':
    # You can put your own code to test Bags here
    new = Bag(['a','c'])
    new2 = Bag(['c','b'])
    print(new + new2)
    print(type(new))
    
    
    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
