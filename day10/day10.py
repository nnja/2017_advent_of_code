# part1: 13760

def part1(input_lengths, list_size=256):
    nums = list(range(list_size))
    curr_pos = 0
    skip_size = 0

    for length in input_lengths:

        if length > 1:
            end = (curr_pos + length) % list_size
            end_index = max(curr_pos, end)
            start_index = min(curr_pos, end)

            if end > curr_pos:
                reversed_nums = nums[start_index:end_index]
                reversed_nums.reverse()
                indicies = list(range(start_index, end_index))
            else:
                reversed_nums = (list(reversed(nums[:start_index])) + list(reversed(nums[end_index:])))
                indicies = list(range(end_index, list_size)) + list(range(0, start_index))

            for index, num in zip(indicies, reversed_nums):
                nums[index] = num

        curr_pos = (curr_pos + length + skip_size) % list_size
        skip_size += 1

    return nums[0] * nums[1]

def run_part2(byte_string, list_size=256):

    nums = list(range(list_size))
    input_lengths = [ord(char) for char in byte_string] + [17, 31, 73, 47, 23]
    curr_pos = 0
    skip_size = 0

    for round in xrange(64):
        curr_pos, skip_size= part2(input_lengths, curr_pos, nums, skip_size)

    sparse_hash = nums
    dense_hash = []

    indicies = range(0, 257, 16)
    for start, end in zip(indicies[0:-1],  indicies[1:]):
        block = nums[start:end]

        value = 0
        for num in block:
            value = value ^ num
        dense_hash.append(value)

    result = ''
    for value in dense_hash:
        hex_val = str(hex(value))[-2:]
        result += '0' + hex_val[-1] if hex_val[0] == 'x' else hex_val

        # if result == '3efbe78a8d82f29979':
        #     import ipdb; ipdb.set_trace()
    return result


def part2(input_lengths, curr_pos, nums, skip_size):
    list_size = 256
    # nums = list(range(list_size))

    for length in input_lengths:

        if length > 1:
            end = (curr_pos + length) % list_size
            end_index = max(curr_pos, end)
            start_index = min(curr_pos, end)

            if end > curr_pos:
                reversed_nums = nums[start_index:end_index]
                reversed_nums.reverse()
                indicies = list(range(start_index, end_index))
            else:
                reversed_nums = (list(reversed(nums[:start_index])) + list(reversed(nums[end_index:])))
                indicies = list(range(end_index, list_size)) + list(range(0, start_index))

            for index, num in zip(indicies, reversed_nums):
                nums[index] = num

        curr_pos = (curr_pos + length + skip_size) % list_size
        skip_size += 1

    return curr_pos, skip_size

ex_list = [0, 1, 2, 3, 4]
input_lengths = [3, 4, 1, 5]

assert part1(input_lengths, list_size=5) == 12

input_lengths = map(int, open('input.txt').read().split(','))
print 'Part1:', part1(input_lengths)

# assert run_part2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
input1 = str(run_part2('AoC 2017'))
print(input1)
assert input1  == '33efeb34ea91902bb2f59c9920caa6cd'

input2 = str(run_part2('1,2,3'))
print(input2)
assert input2 == '3efbe78a8d82f29979031a4aa0b16a9d'

input3 = str(run_part2('1,2,4'))
print(input3)
assert input3  == '63960835bcdc130f0b66d7ff4f6a5a8e'

input = open('input.txt').read().strip()
print(repr(input))

print 'Part2:', run_part2(input)
