from bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle, random.randint
  #random.shuffle(alist) mutates its alist argument, to be a random permutation
  #random.randint(1,10)  returns a random number in the range 1-10 inclusive
  


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
        
    def test_len(self):
        self.assertEqual(len(self.alist),7)
        len_size = 7
        random.shuffle(self.alist)
        for i in self.alist:
            self.bag.remove(i)
            len_size -= 1
            self.assertEqual(len(self.bag), len_size)
        self.assertEqual(len(self.bag), 0)
    
    def test_unique(self):
        self.assertEqual(len(self.bag.counts),4)
        random.shuffle(self.alist)
        for i in self.alist:
            self.bag.remove(i)
            self.assertEqual(len(self.bag.counts),self.bag.unique())
    
    def test_contains(self):
        for x in ['a','b','c','d']:
            self.assertIn(x,self.alist)
        self.assertNotIn('x',self.alist)
        
    def test_count(self):
        self.assertTrue(self.bag.counts['a'] == 1)
        self.assertTrue(self.bag.counts['b'] == 2)
        self.assertTrue(self.bag.counts['c'] == 1)
        self.assertTrue(self.bag.counts['d'] == 3)
        self.assertTrue(self.bag.counts['x'] == 0)
        random.shuffle(self.alist)
        s_counts = sum(self.bag.counts.values())
        for i in self.alist:
            self.bag.remove(i)
            s_counts -= 1
            self.assertEqual(len(self.bag),s_counts)
            
    
    def test_eq(self):
        temp_list = [random.randint(1,10) for i in range(1,1001)]
        b1 = Bag(temp_list)
        random.shuffle(temp_list)
        b2 = Bag(temp_list)
        self.assertEqual(b1,b2)
        b2.remove(temp_list[0])
        self.assertNotEqual(b1,b2)
    
    def test_add(self):
        temp_list = [random.randint(1,10) for i in range(1,1001)]
        b1 = Bag(temp_list)
        b2 = Bag()
        random.shuffle(temp_list)
        for i in temp_list:
            b2.add(i)
        self.assertEqual(b1,b2)

               
    def test_remove(self):
        temp_list = []
        for i in range(1,1001):
            temp_list.append(random.randint(1,10))
        b1 = Bag(temp_list)
        self.assertRaises(ValueError,self.bag.remove,33)
        b2 = Bag(temp_list)
        for i in temp_list:
            b2.add(i)
            b2.remove(i)
        self.assertEqual(b1,b2)

