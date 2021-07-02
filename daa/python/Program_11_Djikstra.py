inf = float('inf')
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
n = len(adjmat)
prevvisit = [n + 1] * len(adjmat) # where you were before
minvalues = [inf] * len(adjmat) # cost of getting there
s = 'a'
e = 'm'
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
