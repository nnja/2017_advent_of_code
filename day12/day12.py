import re
import networkx as nx

regex = '(.*) <-> (.*)'

def day12(input):
    G = nx.MultiDiGraph()

    for line in input.strip().split('\n'):
        key, values = re.match(regex, line).groups()
        values = [value.strip() for value in values.split(',')]

        for value in values:
            G.add_edge(key, value)

    num_connected = 0

    for node in G.nodes.keys():
        try:
            nx.bidirectional_shortest_path(G, '0', node)
            num_connected += 1
        except:
            pass

    return num_connected


input = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""

assert day12(input) == 6

print 'Part1:', day12(open('input.txt').read().strip())
