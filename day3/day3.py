import unittest
from unittest import skip
from math import sqrt, ceil, floor
from pprint import pprint

up = lambda x, y: (x, y - 1)
down = lambda x, y: (x, y + 1)
left = lambda x, y: (x - 1, y)
right = lambda x, y: (x + 1, y)
operations = [right, up, left, down]

diag_down_left = lambda x, y: (x - 1, y + 1)
diag_down_right = lambda x, y: (x + 1, y + 1)
diag_up_left = lambda x, y: (x - 1, y - 1)
diag_up_right = lambda x, y: (x + 1, y - 1)
sum_operations = (operations +
                  [diag_down_left, diag_down_right, diag_up_left, diag_up_right])


def steps_from_1(target):

    _, _,  coord_one, coord_target, _ = generate_spiral_grid(target)
    return abs(coord_one[0] - coord_target[0]) + abs(coord_one[1] - coord_target[1])

def calculate_surrounding_sum(x, y, grid):

    sum = 0
    for op in sum_operations:
        try:
            test_x, test_y = op(x, y)
            if test_x >= 0 and test_y >= 0:
                value = grid[test_y][test_x]
                sum += value
        except:
            pass
    return sum

def generate_spiral_grid(target):

    grid_size = int(ceil(sqrt(target)))
    grid = [[0 for i in xrange(grid_size)] for i in xrange(grid_size)]
    sum_grid = [[0 for i in xrange(grid_size)] for i in xrange(grid_size)]
    center = int(floor(grid_size / 2))

    # Special case for even sized grids
    if grid_size % 2 == 0:
        x = center - 1
    else:
        x = center
    y = center

    grid[y][x] = sum_grid[y][x] = 1
    start_coord = target_coord = (x, y)

    operation_counter = 0
    num_steps = 1
    num = 2

    done = False
    part_two_answer = 0

    while not done:

        for op in operations:
            if operation_counter == 2:
                num_steps += 1
                operation_counter = 0

            for st in xrange(num_steps):


                if num > target:
                    done = True
                    break

                x, y = op(x, y)
                grid[y][x] = num

                surrounding_sum = calculate_surrounding_sum(x, y, sum_grid)
                sum_grid[y][x] = surrounding_sum

                if surrounding_sum > target and part_two_answer == 0:
                    part_two_answer = surrounding_sum

                if num == target:
                    target_coord = (x, y)

                num += 1

            operation_counter += 1

    return grid, sum_grid, start_coord, target_coord, part_two_answer


class TestDayThree(unittest.TestCase):

    def test_part_2(self):
        sample_output = [
            [147, 142, 133, 122, 59],
            [304, 5, 4, 2, 57],
            [330, 10, 1, 1, 54],
            [351, 11, 23, 25, 26],
            [362, 747, 806],
        ]

        grid, sum_grid, _, _, part_two_answer = generate_spiral_grid(23)
        self.assertEquals(part_two_answer, 25)

    def test_part_2_puzzle_input(self):

        _, _, _, _, part_two_answer = generate_spiral_grid(325489)
        print '\nSolution Part 2:', part_two_answer
        self.assertEquals(330785, part_two_answer)

    def test_example_1(self):
        result = steps_from_1(1)
        self.assertEquals(result, 0)

    def test_example_2(self):
        result = steps_from_1(12)
        self.assertEquals(result, 3)

    def test_example_3(self):
        result = steps_from_1(23)
        self.assertEquals(result, 2)

    def test_example_4(self):
        result = steps_from_1(1024)
        self.assertEquals(result, 31)

    def test_given_input(self):
        result = steps_from_1(325489)
        print '\nSolution Part 1:', result
        self.assertEquals(result, 552)
