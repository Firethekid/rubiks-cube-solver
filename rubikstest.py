import twophase.solver as sv
import cubemodel
import random

random.seed(6)
rubikscube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"


def cubereset():
    global rubikscube
    rubikscube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"


cubereset()


def scramblecube(cube):

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
solution = sv.solve(rubikscube)
print(solution)



"""
cubemodel.encode(rubikscube)
solution = sv.solve("DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL").split()
solution.pop()
print(solution)

"""

def solvingmoves(moves):
    for x in moves:
        for i in range(int(x[1])):
            cubemodel.rubiksmoves[x[0]]

#solvingmoves(solution)
