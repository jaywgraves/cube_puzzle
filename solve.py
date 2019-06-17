import random
import copy


# normal die
#  1
# 235
#  6
#  4
cube = []
#             1   2   3   5   6   4
cube.append(('G','B','W','W','R','R'))
cube.append(('B','R','W','R','R','G'))
cube.append(('B','G','W','R','B','G'))
cube.append(('G','R','B','B','W','W'))
#random.shuffle(cube)

rotations = []

face_seed = []
face_seed.append([0,2,4,5])
face_seed.append([1,2,3,5])
for faces in face_seed:
    for i in range(4):
        rotations.append(copy.copy(faces))
        rotations.append(list(reversed(faces)))
        faces.append(faces.pop(0))

rot_len = len(rotations)

def get_cube(cube_idx, rot_idx):
    return tuple(cube[cube_idx][ri] for ri in rotations[rot_idx])

def check(a, b, c, d):
    correct = 0
    for s1,s2,s3,s4 in zip(a, b, c, d):
        cube_side = (s1, s2, s3, s4)
        if len(set(cube_side)) != 4:
            if correct > 2:
                print('correct =',correct)
            return False
        correct += 1 
    return True

cnt = 0
for ai in range(rot_len):
    a = get_cube(0, ai)
    for bi in range(rot_len):
        b = get_cube(1, bi)
        for ci in range(rot_len):
            c = get_cube(2, ci)
            for di in range(rot_len):
                d = get_cube(3, di)
                cnt += 1
                #print('rotations', ai, bi, ci, di)
                solved = check(a, b, c, d)
                #print('a rot', ai, 'b rot', bi, 'c rot', ci, 'd rot', di)
                #q = input('?')
                if solved:
                    print(a)
                    print(b)
                    print(c)
                    print(d)
print('count', cnt)

