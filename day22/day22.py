# answer part1: 5433
# answer part2: 2512599
import pprint

left = 'left'
right = 'right'
up = 'up'
down = 'down'

directions = {
    left: lambda x, y: (x - 1, y),
    right: lambda x, y: (x + 1, y),
    up: lambda x, y: (x, y - 1),
    down: lambda x, y: (x, y + 1),
}

infected = '#'
clean = '.'
weakened = 'W'
flagged = 'F'

def expand(grid, x, y):
    if x < 0:
        for row in grid:
            row.insert(0, '.')
        x = 0
    if x == len(grid[0]):
        for row in grid:
            row.append('.')
    if y < 0:
        grid.insert(0, ['.'] * len(grid[0]))
        y = 0
    if y == len(grid):
        grid.append(['.'] * len(grid[0]))
    return x, y


def day22(input):

    grid = [list(line) for line in input.splitlines() if line]
    center = int(len(grid) / 2)

    direction = up
    x = center
    y = center
    counter = 0

    for i in range(10000000):
        curr_node = grid[y][x]

        if curr_node == infected:  # turn to the right
            if direction == left: direction = up
            elif direction == up: direction = right
            elif direction == right: direction = down
            elif direction == down:direction = left

            grid[y][x] = flagged

        elif curr_node == clean:  # turn to the left
            if direction == left: direction = down
            elif direction == up: direction = left
            elif direction == right: direction = up
            elif direction == down: direction = right

            grid[y][x] = weakened

        elif curr_node == flagged:
            if direction == up: direction = down
            elif direction == down: direction = up
            elif direction == left: direction = right
            elif direction == right: direction = left

            grid[y][x] = clean

        elif curr_node == weakened:
            grid[y][x] = infected
            counter += 1

        x, y = directions[direction](x, y)
        x, y = expand(grid, x, y)

    return counter

test_input = (
"""
..#
#..
...
"""
)
# print(day22(test_input))
print(day22(open('input.txt').read()))

