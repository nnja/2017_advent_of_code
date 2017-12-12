directions = {
    'n': lambda x, y, z: (x, y + 1, z - 1),
    's': lambda x, y, z: (x, y - 1, z + 1),

    'nw': lambda x, y, z: (x - 1, y + 1, z),
    'ne': lambda x, y, z: (x + 1, y, z - 1),

    'sw': lambda x, y, z: (x - 1, y, z + 1),
    'se': lambda x, y, z: (x + 1, y - 1, z),
}


def day11(input):

    start = (0, 0, 0)
    end = (0, 0, 0)

    furthest = 0

    for direction in input.strip().split(','):
        end = directions[direction](end[0], end[1], end[2])
        furthest = max(furthest, distance(end))

    print 'Furthest point:', furthest
    return distance(end)

def distance(destination):
        x, y, z = destination
        return (abs(x) + abs(y) + abs(z)) / 2 

assert day11('ne,ne,ne') == 3
assert day11('ne,ne,sw,sw') == 0
assert day11('ne,ne,s,s') == 2
assert day11('se,sw,se,sw,sw') == 3

print 'Part1:', day11(open('input.txt').read())
