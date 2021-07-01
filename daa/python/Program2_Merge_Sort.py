

# Q:2
# Algorithm to sort an array using Merge sort
# Time complexity : O(nlogn), where n is length of array. 
# Space complexity : O(n) ,where we divide the problem into n subproblems

# INPUT PORTION
# comment below if you want to use input
arr = [6,4,3,6,3,5,7,32,4,7,4,3,23]

# comment below if you want to use the preconfigured array
# print("Enter the length of the array")
# n = int(input())
# print("Enter the array as a space seperated integer list")
# arr = [int(i) for i  in input().split(" ")]

# PROGRAM PORTION
# mergesort is a divide and conquer algorithm. we merge the sub arrays to sort the array
def merge(b,c,a):
    i = j = k = 0
    p = len(b) 
    q = len(c)
    while(i < p and j < q):
        if b[i] <= c[j]:
            a[k] = b[i] ; i += 1
        else:
            a[k] = c[j] ; j += 1
        k += 1
    if i == p:
            a[k : p + q ] = c[j : q]
    else:
            a[k : p + q] = b[i : p]
    return a

def mergesort(a):
    n = len(a)
    if(n > 1):
        b =  a[0 :(n//2)]
        c = a[(n//2) : n]
        mergesort(b)
        mergesort(c)
        merge(b,c,a)
    return a

print(mergesort(arr))
 