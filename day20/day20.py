# Answer Part 1: 157
from collections import namedtuple
import re
from pprint import pprint

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


def calc_distance_from_origin(particle):
    return (abs(particle['pos'].x)
            + abs(particle['pos'].y)
            + abs(particle['pos'].z)
)

def day20(lines):
    particles = []
    for line in lines:
        coords = list(map(int, re.match(pattern, line).groups()))
        pos = Coord(coords[0], coords[1], coords[2])
        vel = Coord(coords[3], coords[4], coords[5])
        acc = Coord(coords[6], coords[7], coords[8])
        particles.append({'velocity': vel, 'acceleration': acc, 'pos': pos})

    for i in range(10000):
        if i % 10000 == 0:
            print('.')

        map(update_particle, particles)

        min_pos = -1
        min_distance = 1000000000000000
        for pos, particle in enumerate(particles):
            distance = calc_distance_from_origin(particle)
            if distance < min_distance:
                min_distance = distance
                min_pos = pos

    return min_pos

test_input = ("""p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>""")
input = test_input.splitlines()
input = open('input.txt').readlines()
print('Part 1',  day20(input))
