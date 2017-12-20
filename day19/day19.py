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

ordered_directions = [down, left, right, up]

def change_direction(grid, direction, x, y):

    # can't go back in original direction
    valid_directions = []

    curr = grid[y][x]
    if direction == up or direction == down:
        target = '-'
    if direction == left or direction == right:
        target = '|'

    for d in ordered_directions:
        try:
            new_x, new_y = directions[d](x, y)
            val = grid[new_y][new_x]
            if val == target or val.isalpha():
                valid_directions.append(d)
        except:
            pass


    if len(valid_directions) == 1 and (direction in valid_directions):
        return -1

    if len(valid_directions) > 1:
        try:
            if direction == down:
                valid_directions.remove(up)
            if direction == up:
                valid_directions.remove(down)
            if direction == left:
                valid_directions.remove(right)
            if direction == right:
                valid_directions.remove(left)
        except:
            pass

    return valid_directions[0]


def day19(input):
    grid = [list(line) for line in input.splitlines() if line]
    seen = []

    direction = down
    x = grid[0].index('|')
    y = 0

    num_steps = 0

    while True:
        curr = val = grid[y][x]

        if curr == ' ' or direction == -1:
            print(''.join(seen))
            print('num steps: %s' % num_steps)
            break
        if curr.isalpha():
            seen.append(curr)
        if curr == '+':
            direction = change_direction(grid, direction, x, y)

        x, y = directions[direction](x, y)
        num_steps += 1


example_input = ("""
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+
""")
day19(example_input)
day19(open('input.txt').read())
