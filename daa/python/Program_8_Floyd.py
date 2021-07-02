import pprint
import  numpy as np
def floyd(mat):
    for k in range(0,len(mat)):
        new = mat # new is going to be matrix k
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                    new[i][j] = min(new[i][j],mat[i][k] + mat[k][j])
        mat = new
    print(np.matrix(mat))

mat = []
# mat = [[0, 999, 3, 999], [2, 0, 5, 999], [999, 7, 0, 1], [6, 999, 9, 0]]
for i in range(0,int(input())):
    # break
    m = []
    for j in input().split(sep=' '):
        if j.__contains__('i'):
            m.append(999)
        else:
            m.append(int(j))
    mat = mat + [m]
print(np.matrix(mat))
floyd(mat)





