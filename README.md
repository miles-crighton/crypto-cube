# crypto-cube
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
