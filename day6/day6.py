# Part 1 answer: 14029
# Part 2 answer: 2765

import unittest

def day6(banks):
    num_cycles = 0
    end_loop = 0
    seen = set()

    while True:
        num_cycles += 1
        seen.add(tuple(banks))

        num_blocks = max(banks)
        start_at = banks.index(num_blocks)
        banks[start_at] = 0

        for i in xrange(1, num_blocks + 1):
            index = (start_at + i) % len(banks)
            banks[index] += 1

        if tuple(banks) in seen:
            break

    return num_cycles

def day6_2(banks):
    num_cycles = 0
    num_redis_cycles = 0
    end_loop = 0
    seen = []

    found_seen = False

    while True:

        if found_seen:
            num_redis_cycles +=1 

        num_cycles += 1
        seen.append(tuple(banks))

        num_blocks = max(banks)
        start_at = banks.index(num_blocks)
        banks[start_at] = 0

        for i in xrange(1, num_blocks + 1):
            index = (start_at + i) % len(banks)
            banks[index] += 1

        if tuple(banks) in seen:
            if found_seen and banks == target:
                break

            found_seen = True
            target = banks
            seen = []

    return num_redis_cycles

if __name__ == '__main__':
    banks = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'.split()
    banks = map(int, banks)
    print 'Result:', day6(banks)
    print 'Result Part 2:', day6_2(banks)

class TestDay6(unittest.TestCase):

    def test_part_one(self):
        banks = [0, 2, 7, 0]
        result = day6(banks)
        self.assertEquals(result, 5)

    def test_part_two(self):
        banks = [0, 2, 7, 0]
        result = day6_2(banks)
        self.assertEquals(result, 4)
