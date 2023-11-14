import twophase.solver as sv
import cubemodel
import random
import time

random.seed(9)
rubikscube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"


def cubereset():
    """
    Sets the rubikscube variable to initial/solved state
    """
    global rubikscube
    rubikscube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"


def scramblecube(cube):
    """
    Returns a scrambled cube string

    Parameters:
        cube (string): string of 54 characters representing facelets

    Returns:
        cube (string): same string, but scrambled using cube conventions
    """

    moves = 10 # number of moves to scramble
    
    for i in range(moves):
        random_key = random.choice(list(cubemodel.rubiksmoves))
        rotations = random.randint(1,3)
        print(random_key, rotations)

        for j in range(0, rotations):
            cube = cubemodel.rubiksmoves[random_key](cube)

    return cube


rubikscube = scramblecube(rubikscube)
print(cubemodel.encode(rubikscube))


print(rubikscube)
solution = sv.solve(rubikscube).replace("3", "'").replace("1", "")
print(solution)

"""
def solvingmoves(moves):
    for x in moves:
        for i in range(int(x[1])):
            cubemodel.rubiksmoves[x[0]]
"""