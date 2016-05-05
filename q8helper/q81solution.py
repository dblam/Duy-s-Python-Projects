from performance import Performance
from goody import irange
from graph_goody import random_graph, spanning_tree

# Put script here to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder
a_random_graph = None
def create_random(n : int):
    global a_random_graph 
    a_random_graph = random_graph(1000*2**n, lambda x: x * 10)

max_nodes = 128000
end_range = 0
while max_nodes != 1000:
    max_nodes = max_nodes / 2
    end_range += 1

for i in irange(0,end_range):
    p = Performance(lambda: spanning_tree(a_random_graph), 
                    lambda: create_random(i), 
                    5,
                    '\nSpanning Tree of size {0}'.format(1000*2**i))
    p.evaluate()
    p.analyze()
