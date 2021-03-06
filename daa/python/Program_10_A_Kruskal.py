# # Q:10
# Algorithm to find the minimum cost span tree using kruskal algorithm
#  Time complexity: O(vE) = O(n^2) but O(n^3) in our case due to adjacency matrix
# Space complexity: O(n) 


# Aim of kruskal : we keep selecting the smallest cost as long as both nodes are not in the visited matrix
import numpy
mat = [[0.0,3,0,0,6,5],[3,0,1,0,0,4],[0,1,0,6,0,4],[0,0,6,0,8,5],[6,0,0,8,0,2],[5,4,4,5,2,0]] # adjacency matrix
visited = set()
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] == 0:
            mat[i][j] = float('inf')

def kruskal():
    global mat
    n = len(mat)
    parent = [n for _ in range(n + 1)]
    # n means no parent
    totalCost = 0
    edges = 0
    while (edges < n - 1):
        min = inf = float("inf")
        u = v = a = b = 0
        for i in range(n):
            for j in range(n):
                if mat[i][j] < min:
                    min = mat[i][j]
                    a = u = i
                    b = v = j 
        # print((u,v,parent),end=" ")
        while parent[u] != n:
            u = parent[u]
        while parent[v] != n:
            v = parent[v]
        # print((u,v))
        if (u != v): #Means they are acyclic beacause they don't originate from the same parent
            print("Edge {}: node {} to node {},cost: {}".format(edges,chr(97 + a),chr(97 + b),min))
            edges += 1
            totalCost += min
            parent[v] = u
        mat[a][b] = inf
        mat[b][a] = inf
    print((totalCost))

kruskal()
 