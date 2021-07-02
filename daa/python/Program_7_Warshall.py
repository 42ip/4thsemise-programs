# TODO:DOCUMENT THIS


import numpy as np
def warshall(mat):
    for k in range(0,len(mat)):
        new = mat # new is going to be matrix k
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                if mat[i][j] == 1 or (mat[i][k] == mat[k][j] == 1):
                    new[i][j] = 1
        mat = new
    print(np.matrix(mat))
# print("enter matrix one by one")
# s = []
# for i in range(0,int(input())):
#     inp = [int(i) for i in input().split(sep=" ")]
#     s = s + [inp]
l = [[0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0]]
warshall(l)

