
# Q:4A
# Algorithm to print all the nodes reachable from a single node using breadth first search
# Time complexity : O(N), where N is number of nodes, and we have to traverse through all the nodes. 
# Space complexity : O(n) ,where worst case is we have to store all the nodes in the order 
# note that here we used dictionaries/hashmaps but one can use adjacency matrix aswell

# INPUT PORTION
# comment below if you want to create your own diagraph
nodes = {0 : [4,3,2], 1 : [4,5], 2 : [0,3,5], 3: [0,2], 4: [0,1,5], 5 : [2,4,1]}

# comment below if you want to input diagraph
# print("enter number of vertices")
# nodes = dict()
# print(nodes)
# for i in range(int(input())):
#     print("Enter the nodes connected to node {} seperated by space:".format(i),end="")
#     a = [int(i) for i in input().split()]
#     nodes[i] = a
# print(nodes)





# [0, 4, 3, 2, 1, 5, 6]


# PROGRAM PORTION
order = []
visited = set()
for i in range(len(nodes.keys())):
    if i not in visited:
        queue = [i]
        if i in nodes.keys():
            queue = queue + nodes[i]
            print(queue)
            while len(queue) != 0:
                if queue[0] not in visited:
                    visited.add(queue[0])
                    order.append(queue[0])
                    for j in nodes[queue[0]]:
                        if j not in visited:
                            queue.append(j)
                            visited.add(j)
                            order.append(j)
                del queue[0]
        order = order + queue
print(order)
        
