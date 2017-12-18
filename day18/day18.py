# ans day 1: 3423
from collections import defaultdict


registers = defaultdict(int)


def day18(lines):
    pos = 0
    last_freq = None
    command = None

    while pos < len(lines):
        line = lines[pos]
        line_input = line.split()

        command = line_input[0]
        first_op = line_input[1]
        second_op = line_input[2] if len(line_input) == 3 else None

        if command == 'snd':
            last_freq = registers[first_op]
        elif command == 'rcv':
            if registers[first_op] != 0:
                return last_freq
        elif command == 'jgz':
            if registers[first_op] > 0:
                step = get_value(second_op)
                pos += step
                continue
        else:
            do_command(command, first_op, second_op)

        pos += 1


def get_value(second_op):
    return (int(second_op)
            if second_op not in registers
            else registers[second_op])


def do_command(command, arg1, arg2):
    value = get_value(arg2)
    if command == 'add':
        registers[arg1] = registers[arg1] + value
    if command == 'mul':
        registers[arg1] = registers[arg1] * value
    if command == 'mod':
        registers[arg1] = registers[arg1] % value
    if command == 'set':
        registers[arg1] = value


file_input = open('input.txt').read()
print day18(file_input.splitlines())
