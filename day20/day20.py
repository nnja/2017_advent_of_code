# Answer Part 1: 157
# Answer Part 2: 499
from collections import namedtuple, defaultdict
import re
from pprint import pprint
import itertools


class Coord(namedtuple('Coord', 'x, y z')):

    def __repr__(self):
        return '{},{},{}'.format(self.x, self.y, self.z)


pattern = 'p=<(\S*),(\S*),(\S*)>, v=<(\S*),(\S*),(\S*)>, a=<(\S*),(\S*),(\S*)>'


def update_particle(particle):
    particle['velocity'] = Coord(
        particle['velocity'].x + particle['acceleration'].x,
        particle['velocity'].y + particle['acceleration'].y,
        particle['velocity'].z + particle['acceleration'].z
    )

    particle['pos'] = Coord(
        particle['pos'].x + particle['velocity'].x,
        particle['pos'].y + particle['velocity'].y,
        particle['pos'].z + particle['velocity'].z
    )


def day20(lines):
    particles = []
    num_no_collisions = 0
    for line in lines:
        if not line.split(): continue

        coords = list(map(int, re.match(pattern, line).groups()))
        pos = Coord(coords[0], coords[1], coords[2])
        vel = Coord(coords[3], coords[4], coords[5])
        acc = Coord(coords[6], coords[7], coords[8])
        particles.append({'velocity': vel, 'acceleration': acc, 'pos': pos})

    while True:
        for particle in particles:
            update_particle(particle)

        positions = defaultdict(list)
        for index, particle in enumerate(particles):
            pos = particle['pos']
            positions[pos] += [index]

        to_remove = sorted(itertools.chain(*[i for i in positions.values() if len(i) > 1]), reverse=True)

        for i in to_remove:
            del particles[i]

        if not to_remove:
            num_no_collisions += 1

        if num_no_collisions > 500:  # Wild guess as to how many times we need to run to ensure no collisions
            return len(particles)


input = open('input.txt').readlines()
print('Part 2',  day20(input))
