# Part1: 648042 or 12803
# Part2: 6425

def calc_groups(input): 
    total_score = current_score = 0
    skip_next = False
    in_garbage = False
    total_garbage = 0

    stack = []
    garbage_stack = []

    for char in input:
        peek = '' if not stack else stack[-1]
        is_garbage = peek == '<'

        if is_garbage and not skip_next and not char == '!':
            garbage_stack.append(char)

        if skip_next:
            skip_next = False
            continue
        elif char == '{':
            if not is_garbage:
                stack.append('{')
                total_score += len(stack)
        elif char == '}':
            if not is_garbage:
                stack.pop()
                # num_groups += 1
        elif char == '<':
            if not is_garbage:
                stack.append('<')
        elif char == '>':
            stack.pop()
            if garbage_stack:
                garbage_stack.pop()

        elif char == '!':
            skip_next = True

    print total_score, len(garbage_stack)
    return total_score, len(garbage_stack)


# Assertions calculating the number of groups
# assert 1 == calc_groups('{}')
# assert 3 == calc_groups('{{{}}}')
# assert 3 == calc_groups('{{},{}}')
# assert 6 == calc_groups('{{{},{},{{}}}}')
# assert 1 == calc_groups('{<{},{},{{}}>}')
# assert 1 == calc_groups('{<a>,<a>,<a>,<a>}')
# assert 5 == calc_groups('{{<a>},{<a>},{<a>},{<a>}}')
# assert 2 == calc_groups('{{<!>},{<!>},{<!>},{<a>}}')

# Assertions calculating the group score
assert 1 == calc_groups('{}')[0]
assert 6 == calc_groups('{{{}}}')[0]
assert 5 == calc_groups('{{},{}}')[0]
assert 16 == calc_groups('{{{},{},{{}}}}')[0]
assert 1 == calc_groups('{<a>,<a>,<a>,<a>}')[0]
assert 9 == calc_groups('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0]
assert 9 == calc_groups('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0]
assert 3 == calc_groups('{{<a!>},{<a!>},{<a!>},{<ab>}}')[0]

assert 0 == calc_groups('<>')[1]
assert 17 == calc_groups('<random characters>')[1]
assert 3 == calc_groups('<<<<>')[1]
assert 2 == calc_groups('<{!>}>')[1]
assert 0 == calc_groups('!!')[1]
assert 0 == calc_groups('<!!!>>')[1]
assert 10 == calc_groups('<{o"i!a,<{i<a>')[1]

part1 = calc_groups(open('input.txt').read())[0]
part2 = calc_groups(open('input.txt').read())[1]
assert part1 == 648042
assert part2 == 6425
# print('Part1: %s' % part1)
# print('Part2: %s' % part2)
