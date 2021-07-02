import copy

# this is not the solution. but please understand this since it is the naive way of solving knapsack problem
def knapsackBruteForce(items,sack):
    #this has a complexity of 2^n since the function makes a subset for each possible combination
    #items : [[items]] where [items]  = [weight,value]
    ret = [[]]
    for i in items:
        for j in range(0,len(ret)):
            a = [] + ret[j]
            a.append(i)
            ret.append(a)
    # print(ret)
    maxval = 0
    soln = []
    for i in ret:
        if not i : continue
        totweight = totval = 0
        for (weight,value) in i :
            totweight += weight
            totval += value
        if totweight <= sack and totval > maxval:
            soln = [i + [[totweight,totval]]]
            maxval = totval
    print(soln)

def printm(matrix):
    for arr in matrix:
        print(arr)  
# this is the solution we must follow. knapsack part  
def knapsackBottomUp(items, sack):
    w =[0] +  [wt for (wt,_) in items]
    v =[0] +  [val for (_,val) in items]
    mat = [[0] * (sack + 1) for _ in  range(0,len(items) + 1)]
    for i in range(0,len(items) + 1):
        for c in range(0,sack + 1):
            #ie let us add this to the sack, sack size will now become c - wi
            take = 0
            nottake = 0
            if c - w[i] >= 0:
                take = v[i] + mat[i - 1][c - w[i]] 
            #ie let us disregard this item and just consider the set of elements with no item i 
            #and a sack of size c
            nottake = mat[i - 1][c]
            mat[i][c] = max(take, nottake)

def knapsackTopDown(items, sack):
    n = len(items)
    w =[wt for (wt,_) in items]
    v =[val for (_,val) in items]
    mat = [[-1] * (sack + 1) for _ in  range(0,len(items) + 1)]
    def dp(i,c):
         if c < 0 : return -999
         if i == n : return 0
         if mat[i][c] != -1:
             return mat[i][c]
         take = dp(i + 1, c - w[i]) + v[i]
         nottake = dp(i+1 ,c)
         mat[i][c] =  max(take, nottake)
         return mat[i][c]
    x =  dp(0,sack)
    print(x)




    



knapsackTopDown([[2,12],[1,10],[3,20],[2,15]],5)
