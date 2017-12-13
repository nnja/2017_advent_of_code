# Answer Part1: 1704

from pprint import pprint
from collections import defaultdict

def day13(input, delay=0):

    foo = defaultdict(int)
    for line in input.strip().splitlines():
        level, range = line.split(': ')
        level = int(level)
        range = int(range)
        foo[level] = range

    level += 1
    firewall_levels = [[]] * level
    for l in xrange(level):
        firewall_levels[l] = [False] * foo[l]

        if firewall_levels[l]:
            firewall_levels[l][0] = True

    severity = 0

    # True = forward, False = backward
    loop_directions = defaultdict(lambda: True)

    run_times = 0
    player_pos = 0

    while player_pos < len(firewall_levels):

        # print player_pos
        is_caught = firewall_levels[player_pos][0] is True if firewall_levels[player_pos] else False
        if is_caught:
            # print 'Caught on player_pos', player_pos, 'which has num scanners:', len(firewall_levels[player_pos])
            severity +=  player_pos * len(firewall_levels[player_pos]) # level_num * len(level)

        for level_num, level in enumerate(firewall_levels):
            run_times += 1
            scanner_pos = 0
            # print 'level_num', level_num, 'scanner pos:', scanner_pos


            if not level:
                continue

            scanner_pos = level.index(True)

            level[scanner_pos] = False
            scanner_pos = scanner_pos + 1 if loop_directions[level_num] else scanner_pos -1
            level[scanner_pos] = True

            if scanner_pos == 0:
                loop_directions[level_num] = True
            elif scanner_pos + 1 == len(level):
                loop_directions[level_num] = False


        player_pos += 1

    return severity

if __name__ == '__main__':
    input = open('input.txt').read()
    delay = 0
    severity = day13(input, delay)
    while severity != 0:
        print 'delay', delay
        severity = day13(input, delay)
        delay += 1



# sample_input = (
# """
# 0: 3
# 1: 2
# 4: 4
# 6: 4
# """)
# result = day13(sample_input)
# print(result)
# assert result == 24

print 'Result Part1:', day13(open('input.txt').read())
