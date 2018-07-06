"""
Crypto-cube Sololearn challenge

TASK:
Write a program that encrypts a given string by randomly rotating the
corresponding cubes, as well as decrypts the string, given the encrypted string
and the rotation sequence.

For instance, for the text "I love coding and SoloLearn" you will need 4 cubes
and here's a random sample of rotations:
0:U:U:L:R,1:U,2:D:R,3:U:R

0, 1, 2 or 3 are the numbers of the cubes, U, L R D are the rotation directions
(Up, Left, Right, Down). Cube rotations are comma-separated. Each cube can have
multiple rotations, separated by colons.

Code Summary:
> Uses a Cube class to simulate each cube and its rotations
> Uses a CubeHandler to run higher level formatting and generate Cubes
> Runs infinite input loop for user to encrypt/decrypt words

02.07.18
Miles Crighton
"""

import random


class Cube():

    def __init__(self, s):
        # 3 coordinate translation tables
        self.ord_og = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0),
                       (1, 0, 1), (1, 1, 1), (0, 1, 1), (0, 0, 1)]
        self.ord_lr = [(0, 0, 1), (0, 1, 1), (0, 1, 0), (0, 0, 0),
                       (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)]
        self.ord_ud = [(0, 1, 0), (0, 1, 1), (1, 1, 1), (1, 1, 0),
                       (1, 0, 0), (1, 0, 1), (0, 0, 1), (0, 0, 0)]
        self.nodes = {}

        for i, cord in enumerate(self.ord_og):
            # If string too short, fill nodes with spaces
            if i < len(s):
                self.nodes[cord] = s[i]
            else:
                self.nodes[cord] = ' '

        self._nodes = self.nodes.copy()

    def r(self, dir):
        # Pass translation cords based on direction
        cords = {'U': zip(self.ord_ud, self.ord_og),
                 'D': zip(self.ord_og, self.ord_ud),
                 'L': zip(self.ord_lr, self.ord_og),
                 'R': zip(self.ord_og, self.ord_lr)}

        for cord_a, cord_b in cords[dir]:
            self.nodes[cord_a] = self._nodes[cord_b]

    def node_list(self):
        return list(self.nodes.values())


class CubeHandler():

    def __init__(self):
        self.cubes = []
        self.r_seq = ''
        self.decrypt = True

    def generate_cubes(self, str_in):
        # Divide string into 8s and pass into Cubes
        for i in range((len(str_in) // 8 + 1)):
            self.cubes.append(Cube(str_in[i * 8:(i + 1) * 8]))

    def generate_seq(self):
        # Generate random rotation sequence
        for i in range(len(self.cubes)):
            self.r_seq += (str(i) + ':')
            for j in range(random.randint(1, 5)):
                cmd = random.choice('UDLR')
                self.r_seq += (cmd + ':')
            self.r_seq = self.r_seq[:-1]
            self.r_seq += ','
        self.r_seq = self.r_seq[:-1]

    def run(self, word, r_seq=''):
        self.cubes = []
        self.generate_cubes(word)

        # Determine mode
        if r_seq == '':
            self.decrypt = False
            self.generate_seq()
            print('Encrypt Mode')
        else:
            self.decrypt = True
            self.r_seq = r_seq
            print('Decrypt Mode')

        self.rotate_cubes()
        self.print_out()

    def rotate_cubes(self):
        for cmd in self.r_seq.split(','):
            # Extract cube n and rotation list
            i, *rs = cmd.split(':')

            # Invert sequence if decryption
            if self.decrypt:
                trantab = str.maketrans('UDLR', 'DURL')
                rs = [r.translate(trantab) for r in rs]

            # Perform rotations on cube
            for r in rs:
                self.cubes[int(i)].r(r)

    def print_out(self):
        out = ''
        for cube in self.cubes:
            out += ''.join(cube.node_list())
        print('Word: {}'.format(out))
        print('Sequence: {}'.format(self.r_seq))


m = CubeHandler()

print('To encrypt:\n\t> Provide word\n\t> Leave sequence empty')
print('To decrypt:\n\t> Provide word\n\t> Provide sequence')
print("Type 'q' to exit.")

while True:
    word = input('Word: ')
    if word == 'q':
        break
    seq = input('Sequence: ')
    if seq == 'q':
        break

    if seq:
        m.run(word, seq)
    else:
        m.run(word)
