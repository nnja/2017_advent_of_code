import unittest
import copy

# Part 1 answer: 354121
# Part 2 answer: 27283023

func_one = lambda x: 1
func_two = lambda x: -1 if x >= 3 else 1

def steps_to_exit(jumps, offset_func):
    num_jumps = 0
    curr_pos = next_pos = 0

    while True:
        if next_pos < 0 or next_pos >= len(jumps):
            break

        offset = jumps[curr_pos]
        next_pos = curr_pos + offset

        calced_offset = offset_func(offset)
        jumps[curr_pos] += calced_offset
        num_jumps += 1

        curr_pos = next_pos

    return num_jumps

def calc(step_func):
    with open('input.txt') as f:
        jumps = map(int, f.readlines())
        return steps_to_exit(jumps, step_func)

if __name__ == '__main__':
    print 'Result Part1:', calc(func_one)
    print 'Result Part2:', calc(func_two)

class TestDayFive(unittest.TestCase):

    def test_part_one(self):
        jumps = [0, 3, 0, 1,-3]

        result = steps_to_exit(jumps, func_one)
        self.assertEquals(result, 5)

    def test_part_two(self):
        jumps = [0, 3, 0, 1,-3]
        result = steps_to_exit(jumps, func_two)
        self.assertEquals(result, 10)
