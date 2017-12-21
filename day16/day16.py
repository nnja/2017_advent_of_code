programs = [chr(c) for c in range(ord('a'), ord('a') + 16)]

def spin(n):
    global programs
    n = int(n)
    programs = programs[-n:] + programs[:len(programs)-n]

def exchange(pos_a, pos_b):
    pos_a = int(pos_a)
    pos_b = int(pos_b)

    keep = programs[pos_a]
    programs[pos_a] = programs[pos_b]
    programs[pos_b] = keep

def partner(a, b):
    pos_a = programs.index(a)
    pos_b = programs.index(b)
    exchange(pos_a, pos_b)

operations = {
    's': lambda x, y: spin(x),
    'x': lambda x, y: exchange(x, y),
    'p': lambda x, y: partner(x, y),
}

def day16(input):
    for op in input.split(','):
        command = op[0]
        a, *b = op[1:].split('/')
        operations[command](a, b[0] if b else None)

    print('Part1: ' + ''.join(programs))


# test_input = 's1,x3/4,pe/b'
# test_output = 'baedc'
# day16(test_input)
day16(open('input.txt').read())

# input = open('input.txt').read()
# for i in range(10000):
#     if i % 10000000 == 0:
#         print('.')
#     foo = day16(input)
# print('Part2: %s' % foo)
