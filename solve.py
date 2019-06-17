import copy
import sys
import random

solve_all = True
shuffle_cube_order = False
rotate_cube_face_start = False

# normal die
#  1
# 235
#  6
#  4
# paths plus reverse and rotations
# 1265  0,1,4,3
# 1562 rev
# 1463  0,5,4,2
# 1364 rev
# 2354  1,2,3,5
# 2453 rev

rotations = []
face_seed = []
face_seed.append([0,1,4,3])
face_seed.append([0,2,4,5])
face_seed.append([1,2,3,5])
for faces in face_seed:
    for i in range(4):
        rotations.append(copy.copy(faces))
        rotations.append(list(reversed(faces)))
        faces.append(faces.pop(0))
rot_len = len(rotations)

cube = []
#             1   2   3   5   6   4
cube.append(('G','B','W','W','R','R'))
cube.append(('B','R','W','R','R','G'))
cube.append(('B','G','W','R','B','G'))
cube.append(('G','R','B','B','W','W'))
if shuffle_cube_order:
    random.shuffle(cube)
# this does not work
if rotate_cube_face_start:
    new_cube = []
    for c in cube:
        c = list(c)
        for _ in range(random.randint(0,5)):
            c.append(c.pop(0))
        new_cube.append(tuple(c))
    cube = new_cube


def get_cube(cube_idx, rot_idx):
    return tuple(cube[cube_idx][ri] for ri in rotations[rot_idx])

def check(a, b, c, d):
    correct = 0
    for s1,s2,s3,s4 in zip(a, b, c, d):
        cube_side = (s1, s2, s3, s4)
        if len(set(cube_side)) != 4:
            return False
        correct += 1 
    return True

cnt = 0
solve_cnt = 0
for ai in range(rot_len):
    a = get_cube(0, ai)
    for bi in range(rot_len):
        b = get_cube(1, bi)
        for ci in range(rot_len):
            c = get_cube(2, ci)
            for di in range(rot_len):
                d = get_cube(3, di)
                cnt += 1
                solved = check(a, b, c, d)
                if solved:
                    solve_cnt += 1
                    print('solved after',cnt,'test')
                    print(a)
                    print(b)
                    print(c)
                    print(d)
                    if not solve_all:
                        sys.exit()

if solve_all:
    print(solve_cnt, "solutions")
print('total count of tests', cnt)

