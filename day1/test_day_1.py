import unittest

"""
Part one:
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

Part two:
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.

"""


def part_one(n):
    sum = 0

    str_input = str(n)
    str_input = str_input + str_input[0]

    for i in xrange(1, len(str_input)):
        prev_char = str_input[i-1]
        current_char = str_input[i]

        if current_char == prev_char:
            sum += int(current_char)

    return sum


def part_two(n):
    sum = 0

    str_input = str(n)
    input_len = len(str_input)
    midpoint = input_len / 2

    for i in xrange(0, midpoint):
        if str_input[i] == str_input[i + midpoint]:
            sum += int(str_input[i])

    sum *= 2
    return sum


class TestDayOnePartTwo(unittest.TestCase):

    def test_example_one(self):
        input = 1212
        result = part_two(input)

        self.assertEquals(result, 6)

    def test_example_two(self):
        input = 1221
        result = part_two(input)

        self.assertEquals(result, 0)

    def test_example_three(self):
        input = 123425
        result = part_two(input)

        self.assertEquals(result, 4)

    def test_example_four(self):
        input = 123123
        result = part_two(input)

        self.assertEquals(result, 12)

    def test_example_five(self):
        input = 12131415
        result = part_two(input)

        self.assertEquals(result, 4)

    def test_input(self):
        with open('part_two_input.txt') as f:
            input = f.read()
            result = part_two(int(input))
            print '\nPart two solution:', result
            expected_output = 1232
            self.assertEquals(result, expected_output)


class TestDayOnePartOne(unittest.TestCase):

    def test_example_one(self):
        input = 1122
        expected_output = 3
        result = part_one(input)

        self.assertEquals(result, expected_output)

    def test_example_two(self):
        input = 1111
        expected_output = 4
        result = part_one(input)

        self.assertEquals(result, expected_output)

    def test_example_three(self):
        input = 1234
        expected_output = 0
        result = part_one(input)

        self.assertEquals(result, expected_output)

    def test_example_four(self):
        input = 91212129
        expected_output = 9
        result = part_one(input)

        self.assertEquals(result, expected_output)

    def test_example_five(self):
        with open('test5.txt') as f:
            input = f.read()
            result = part_one(int(input))

            print '\nPart one solution:', result

            expected_output = 1390
            self.assertEquals(result, expected_output)
