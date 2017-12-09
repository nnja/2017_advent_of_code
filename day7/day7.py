# Part 1 answer: mwzaxaj
# Part 2 answer: 1219

import unittest
import re

# Yucky global variable. Sorry, not sorry.
node_dict = {}

class Node:
    def __init__(self, name, weight, children, parent=None):
        self.name = name
        self.weight = weight
        self.children = self.create_children(children or [])
        self.parent = parent

    def create_children(self, children):
        for child_name in children:
            if child_name in node_dict:
                child = node_dict[child_name]
                child.parent = self.name
            else:
                child = Node(child_name, 0, None, self.name)
                node_dict[child_name] = child
        return children

    def __repr__(self):
        return 'Name: {} Weight: {} Parent: {} Children: {}'.format(self.name, self.weight, self.parent, self.children)

def get_parent(input):
    lines = input.splitlines()
    for line in lines:
        tokens =  re.split('\W+', line.strip())

        name = tokens[0]
        weight = int(tokens[1])
        children = tokens[2:]

        parent = None
        if name in node_dict:
            parent = node_dict[name].parent
        node_dict[name] = Node(name, weight, children, parent)

    for node in node_dict.values():
        if not node_dict[node.name].parent:
            return node

def day7_2(root):
    weights = sum_of_weights(root)
    return weights

def sum_of_weights(node):
    weight = node.weight

    if not node.children:
        return weight
    else:
        child_weights = [sum_of_weights(node_dict[child_node]) for child_node in node.children]
        if not all(cw == child_weights[0] for cw in child_weights):
            max_weight = max(child_weights)
            min_weight = min(child_weights)
            difference = max_weight - min_weight

            # find the index of the wrong weight
            # that's the index of the child with the bad weight. 

            bad_child_loc = child_weights.index(max_weight)
            bad_child = node_dict[node.children[bad_child_loc]]
            good_weight = bad_child.weight - difference
            print('Result Part 2: %s' % good_weight)
            child_weights[bad_child_loc] = min_weight
        return weight + sum(child_weights)


if __name__ == '__main__':
    file_contents = open('input.txt', "r").read()
    parent = get_parent(file_contents)
    print 'Result Part 1:', parent.name
    day7_2(parent)


class TestDay7(unittest.TestCase):

    def setUp(self):
        node_dict = {}
        self.input = """pbga (66)
        xhth (57)
        ebii (61)
        havc (66)
        ktlj (57)
        fwft (72) -> ktlj, cntj, xhth
        qoyq (66)
        padx (45) -> pbga, havc, qoyq
        tknk (41) -> ugml, padx, fwft
        jptl (61)
        ugml (68) -> gyxo, ebii, jptl
        gyxo (61)
        cntj (57)"""

    def test_sample_input(self):
        result = get_parent(self.input)
        self.assertEquals(result.name, 'tknk')
