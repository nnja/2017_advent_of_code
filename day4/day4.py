import unittest
from collections import Counter

def check_passphrase(line, part=1):
    # 386 wass the right answer for part1.
    # 208 for part 2

    words = (word.strip() for word in line.split())
    uniques = set()

    for word in words:
        sorted_word = ''.join(sorted(word))

        if part == 1:
            if word in uniques:
                return False
            uniques.add(word)
        else:
            if sorted_word in uniques:
                return False
            uniques.add(sorted_word)

    return True

def check_input():
    part_one_sum = 0
    part_two_sum = 0

    with open('input.txt') as f:
        for line in f:
            if check_passphrase(line, part=1):
                part_one_sum += 1
            if check_passphrase(line, part=2):
                part_two_sum += 1

    return part_one_sum, part_two_sum


if __name__ == '__main__':
    print 'Solutions:', check_input()


class TestDayFour(unittest.TestCase):

    def test_inputs_part_one(self):
        phrase = 'aa bb cc dd ee'
        self.assertTrue(check_passphrase(phrase))

        phrase = 'aa bb cc dd aa'
        self.assertFalse(check_passphrase(phrase))

        phrase = 'aa bb cc dd aaa'
        self.assertTrue(check_passphrase(phrase))

    def test_inputs_part_two(self):
        phrase = 'abcde fghij'
        self.assertTrue(check_passphrase(phrase, 2))

        phrase = 'abcde xyz ecdab'
        self.assertFalse(check_passphrase(phrase, 2))

        phrase = 'a ab abc abd abf abj'
        self.assertTrue(check_passphrase(phrase, 2))

        phrase = 'iiii oiii ooii oooi oooo'
        self.assertTrue(check_passphrase(phrase, 2))

        phrase = 'oiii ioii iioi iiio'
        self.assertFalse(check_passphrase(phrase, 2))

