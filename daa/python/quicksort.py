# algorithm to sort n numbers using quicksort
list = [7,6,1,5,4,3]

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

quicksort(list, 0, 5)