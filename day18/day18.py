# ans part 1: 3423
# ans part 2: 7493

from collections import defaultdict


def day18(instructions, pid):
    registers = defaultdict(int)
    registers['p'] = pid
    pos = 0
    send_queue = []

    while pos < len(instructions):
        command, arg1, *opt_arg = instructions[pos].strip().split()
        if opt_arg:
            val = opt_arg[0]
            arg2 = registers[val] if val in registers else int(val)

        if command == 'add':
            registers[arg1] = registers[arg1] + arg2
        if command == 'mul':
            registers[arg1] = registers[arg1] * arg2
        if command == 'mod':
            registers[arg1] = registers[arg1] % arg2
        if command == 'set':
            registers[arg1] = arg2
        if command == 'snd':
            send_queue.append(registers[arg1])
        if command == 'rcv':
            registers[arg1] = yield send_queue
            send_queue = []
        if command == 'jgz':
            if registers[arg1] if arg1 in registers else int(arg1) > 0:
                pos += arg2
                continue

        pos += 1


instructions = open('input.txt').readlines()

p0 = day18(instructions, pid=0)
p1 = day18(instructions, pid=1)

send_to_1, send_to_0 = next(p0), next(p1)
answer = 0

while True:
    while send_to_0:
        yielded_by_0 = p0.send(send_to_0.pop(0))
        if yielded_by_0:
            send_to_1 += yielded_by_0
    while send_to_1:
        yielded_by_1 = p1.send(send_to_1.pop(0))
        if yielded_by_1:
            send_to_0 += yielded_by_1
            answer += len(yielded_by_1)

    if not (send_to_0 or send_to_1):
        break

print('Part 2: %s' % answer)

