# Part1: ehdpincaogkblmfj
# Part2: bpcekomfgjdlinha

programs = [chr(c) for c in range(ord('a'), ord('a') + 16)]

def spin(n):
    global programs
    n = int(n)
    programs = programs[-n:] + programs[:len(programs)-n]

def exchange(pos_a, pos_b):
    pos_a = int(pos_a)
    pos_b = int(pos_b)

    programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]

def partner(a, b):
    pos_a = programs.index(a)
    pos_b = programs.index(b)
    exchange(pos_a, pos_b)

operations = {
    's': lambda x, y: spin(x),
    'x': lambda x, y: exchange(x, y),
    'p': lambda x, y: partner(x, y),
}

ops = open('input.txt').read().split(',')
def day16():
    seen = []
    for i in range(1000000000):
        target = ''.join(programs)
        if target in seen:
            print(seen[1000000000 % i])
            return
        seen.append(target)

        for op in ops:
            command = op[0]
            a, *b = op[1:].split('/')
            operations[command](a, b[0] if b else None)

day16()
