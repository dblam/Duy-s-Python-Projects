import cProfile
from graph_goody import random_graph,spanning_tree
import pstats

# Put script here to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder

cProfile.run('spanning_tree(random_graph(50000, lambda x: 10* x))', 'one')
cProfile.run('spanning_tree(random_graph(100000, lambda x: 10* x))', 'two')

p = pstats.Stats('one')
# uncomment the line below to print all the the information above
#p.strip_dirs().sort_stats(-1).print_stats()
p.sort_stats('ncalls').print_stats()
#p.sort_stats('cumulative').print_stats(10)
p.sort_stats('tottime').print_stats()

p2 = pstats.Stats('two')
# uncomment the line below to print all the the information above
#p.strip_dirs().sort_stats(-1).print_stats()
p2.sort_stats('ncalls').print_stats()
#p.sort_stats('cumulative').print_stats(10)
p2.sort_stats('tottime').print_stats()


