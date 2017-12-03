from itertools import permutations as perms
import unittest

def min_max(values):
    return max(values) - min(values)

def even_div(values):
    return sum(x / y for x, y in perms(values, 2) if x % y == 0)

def solution(spreadsheet, func):
    return sum(func(map(int, line.split()))
               for line in spreadsheet.splitlines())


class TestDayTwo(unittest.TestCase):

    def test_part1_example_spreadsheet(self):
        sheet = """5 1 9 5
                   7 5 3
                   2 4 6 8"""

        result = solution(sheet, func=min_max)
        self.assertEquals(result, 18)

    def test_part2_example_spreadsheet(self):
        sheet = """5 9 2 8
                   9 4 7 3
                   3 8 6 5"""

        result = solution(sheet, func=even_div)
        self.assertEquals(result, 9)

    def test_given_input(self):
        with open('input.txt') as f:
            data = f.read()

            result = solution(data, func=min_max)
            print '\nSolution Part 1:', result
            self.assertEquals(result, 39126)

            result = solution(data, func=even_div)
            print '\nSolution Part 2:', result
            self.assertEquals(result, 258)
