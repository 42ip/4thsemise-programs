
# Q:11
# Algorithm to find the shortest path between 2 points in a connected weighted graph using djikstra's algorithm
# Time complexity : O(N^2), where N is number of nodes. 
# Space complexity : O(N) ,where we store visited nodes in an array with their costs
inf = float('inf')

# INPUT PORTION

# COMMENT BELOW IF YOU WANT TO INPUT A GRAPH
adjmat = [    
[inf,7,2,inf,inf,inf,inf,3,inf,inf,inf,inf,inf],
[7,inf,3,4,inf,inf,inf,inf,inf,inf,inf,inf,inf],
[2,3,inf,4,inf,1,inf,inf,inf,inf,inf,inf,inf],
[inf,4,4,inf,5,inf,inf,inf,inf,inf,inf,inf,inf],
[inf,inf,inf,5,inf,3,inf,inf,inf,inf,inf,inf,inf],
[inf,inf,1,inf,3,inf,2,inf,inf,inf,inf,inf,inf],
[inf,inf,inf,inf,inf,2,inf,inf,inf,inf,inf,inf,2],
[3,inf,inf,inf,inf,inf,inf,inf,2,inf,inf,inf,inf],
[inf,inf,inf,inf,inf,inf,inf,2,inf,4,4,inf,inf],
[inf,inf,inf,inf,inf,inf,inf,inf,4,inf,6,4,inf],
[inf,inf,inf,inf,inf,inf,inf,inf,4,6,inf,4,inf],
[inf,inf,inf,inf,inf,inf,inf,inf,inf,4,4,inf,5],
[inf,inf,inf,inf,inf,inf,2,inf,inf,inf,inf,5,inf],
]
# uncommment below if you want 2nd example
# adjmat = [
#  [inf, 3.0, 5.0, 7.0, inf, inf, inf, inf, inf],
#  [3.0, inf, inf,   1.0, 7.0, inf, inf, inf, inf], 
#  [5.0, inf, inf, 3.0, inf, 2.0, inf, inf, inf],
#  [7.0, 1.0, 3.0, inf, 2.0, 3.0, 1.0, inf, inf],
#  [inf, 7.0, inf, 2.0, inf, inf, 2.0, 1.0, inf], 
#  [inf, inf, 2.0, 3.0, inf, inf, 3.0, inf, 4.0], 
#  [inf, inf, inf, 1.0, 2.0, 3.0, inf, 3.0, 2.0], 
#  [inf, inf, inf, inf, 1.0, inf, 3.0, inf, 5.0], 
#  [inf, inf, inf, inf, inf, 4.0, 2.0, 5.0, inf]
#  ]
s = 'a'
e = 'e'

# COMMENT BELOW IF YOU WANT TO USE THE PROVIDED GRAPH

# print("Enter the number of nodes:",end = " ")
# n = int(input())
# adjmat = []
# print("Enter the adjacency matrix as space seperated values")
# for _ in range(n):
#     inparr = input().split(sep=" ")
#     for i in range(len(inparr)):
#         if inparr[i] == "0":
#             inparr[i] = 'inf'
#     inparr = list(map(float,inparr))
#     adjmat.append(inparr)


n = len(adjmat)
print("Enter the start and end nodes seperated by space (should be between {} and {})".format(chr(97),chr(96 + n)))
inparr = input().split(sep = " ")
s = inparr[0]
e = inparr[1]


n = len(adjmat)
prevvisit = [n + 1] * len(adjmat) # where you were before
minvalues = [inf] * len(adjmat) # cost of getting there

start = (ord(s) - 97) if int(ord(s)) else 0 
end = (ord(e) - 97) if int(ord(e)) else n - 1 

minvalues[start] = 0
prevvisit[start] = 0
visited = [False] * len(adjmat)
def findmin() -> int:
    index = end
    for i in range(n):
            if minvalues[i] < minvalues[index] and not visited[i]:
                index = i            
    return index

def djikstra():
    for _ in range(n):
        index = findmin()
        for i in range(len(adjmat[index])):
            cost = adjmat[index][i]
            if minvalues[i] > cost + minvalues[index] and not visited[i]:
                minvalues[i] = cost + minvalues[index]
                prevvisit[i] = index
                adjmat[i][index] = inf
                adjmat[index][i] = inf
        visited[index] = True
             
djikstra()

print("The cost of going from {} to {} is {} and the path is :".format(s,e,minvalues[end]))
print("{}<-".format(e),end="")
while end != start:
    print("{}".format(chr(97 + prevvisit[end]) + ("<-" if prevvisit[end] != start else " ")),end= "")
    end = prevvisit[end]
print()
# for i in range(len(visited)):
#     print((chr(97 + i), minvalues[i]))
