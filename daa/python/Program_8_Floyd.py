# # Q:8
# Algorithm to Find the shortest paths for pairs in graph using Floyd's algorithm 
#  Time compexity: O(n^3) since it goes through 3 for loops
# Space complexity: O(1) if we change the original matrix or O(n^2) if we create a new matrix each time
import pprint
import  numpy as np

# INPUT PORTION:
# uncomment below for preconfigured input
mat = [[0, 999, 3, 999], [2, 0, 5, 999], [999, 7, 0, 1], [6, 999, 9, 0]]

# uncomment below for manual input
# mat = []
# print("Enter the Number of nodes, followed by space seperated row values. i for infinity")
# for i in range(0,int(input())):
#     # break
#     m = []
#     for j in input().split(sep=' '):
#         if j.__contains__('i'):
#             m.append(999)
#         else:
#             m.append(int(j))
#     mat = mat + [m]

# LOGIC : we compare the distances between the two  paths above, ie direct path (i,j) and indirect path through k. We assign the 
# shortest path's value to the node(i,j).

def floyd(mat):
    for k in range(0,len(mat)):
        new = mat # new is going to be matrix k
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                    new[i][j] = min(new[i][j],mat[i][k] + mat[k][j])
        mat = new
    print(np.matrix(mat))


print(np.matrix(mat))
floyd(mat)





