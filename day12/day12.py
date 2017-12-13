import re
import networkx as nx

regex = '(.*) <-> (.*)'

def day12(lines):
    G = nx.MultiGraph()

    for line in lines:
        key, values = re.match(regex, line).groups()
        import ipdb; ipdb.set_trace()
        G.add_edges_from((key, v) for v in values.split(', '))

    print 'Part1:', len(nx.node_connected_component(G, '0'))
    print 'Part2:', nx.number_connected_components(G)

day12(open('input.txt').readlines())
