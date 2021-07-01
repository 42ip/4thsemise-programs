






# INPUT PORTION
# comment below if you want to use input
arr = [6,4,3,6,3,5,7,32,4,7,4,3,23]

# comment below if you want to use the preconfigured array
# print("Enter the length of the array")
# n = int(input())
# print("Enter the array as a space seperated integer list")
# arr = [int(i) for i  in input().split(" ")]

# PROGRAM PORTION

# The idea with quicksort is that a pivot point exists, where we split the array into 2.
# the pivot point is the final position for the element at the point.
def partition(a,l,r):
    #takes a subarray and returns the partition position
    pivot = a[l]
    i = l 
    for k in range(l, r + 1):
        if a[k] <= pivot:
            print(a)
            a[i], a[k] = a[k] , a[i]
            i += 1
    a[i - 1], a[l] = a[l], a[i - 1]
    return i - 1

def quicksort(a,l,r):
    if(l < r):
        s =  partition(a,l,r)
        quicksort(a,l,s - 1)
        print(a)
        quicksort(a,s + 1, r)
        print(a)

quicksort(arr, 0, len(arr) - 1)