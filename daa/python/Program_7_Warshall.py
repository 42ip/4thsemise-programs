# # Q:7
# Algorithm to Find the transitive closure of a graph using warshalls algorithm
#  Time compexity: O(n^3) since it goes through 3 for loops
# Space complexity: O(1) if we change the original matrix or O(n^2) if we create a new matrix each time

# INPUT PORTION: 

#uncomment below if you want to use a preconfigured input
l = [[0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0]]

# uncomment below if you want to enter an adjacency matrix
# print("enter matrix one by one")
# l = []
# for i in range(0,int(input())):
#     inp = [int(i) for i in input().split(sep=" ")]
#     l = l + [inp]



# PROGRAM PORTION
# LOGIC :  Go through each point in the matrix, and see if either their bases are both 1 or if the element itself is 1
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

warshall(l)

