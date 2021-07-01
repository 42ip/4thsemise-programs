import itertools as it
# this is the brute force algorithm for the n queens problem. basically checking if two queens fall on the same lines
def soln(perm):
    for (i1, i2) in it.combinations(range(len(perm)),2):
        if (abs(i1 - i2) == abs(perm[i1] - perm[i2])):
            return False
    return True

def checker(perm):
    i = len(perm) - 1
    for j in range(i):
        # this sees if the 2 points are 45deg to each other or not
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True        
# backtracking method
def generate(perm, n): 
    if (n == len(perm)):
        print((list(map(lambda x : x + 1,perm))))
        return

    for k in range(n):
     if k not in perm:
        perm.append(k)
        if(checker(perm)):
            generate(perm,n)
        perm.pop()
 
generate([],9)