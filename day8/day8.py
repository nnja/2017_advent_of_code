import re
import unittest
from collections import defaultdict


conditionals = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
}

operations = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y
}

pattern = r'(\S*) (inc|dec) (-?\d*) if (\S*) (\W*) (-?\d*)'
registers = defaultdict(int)


def day8(instructions):
    max_value = 0
    instructions = [instruction.strip() for instruction in instructions.splitlines()]

    for instruction in instructions:
        mo = re.match(pattern, instruction)
        register, action, number, o_register, conditional, cond_num = mo.groups()

        should_proceed = conditionals[conditional](registers[o_register], int(cond_num))
        if should_proceed:
            registers[register] = operations[action](registers[register], int(number))
        max_value = max(max_value, max(registers.values()))

    return max(registers.values()), max_value


if __name__ == '__main__':
    print 'Part 1 & 2', day8(open('input.txt').read())


class DayEightTest(unittest.TestCase):

    def test_part_one(self):
        data = """b inc 5 if a > 1
        a inc 1 if b < 5
        c dec -10 if a >= 1
        c inc -20 if c == 10"""

        result = day8(data)
        self.assertEquals(result, 1)
