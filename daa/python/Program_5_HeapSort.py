
# Q:5
# Algorithm to Sort an array using heapsort using either maxheap or minheap.
# Time complexity : O(N), where N is number of nodes, and we have to traverse through all the nodes. 
# Space complexity : O(n) ,where worst case is we have to store all the nodes in the order 
# note that here we used dictionaries/hashmaps but one can use adjacency matrix aswell


# INPUT PORTION:
# comment below if you want to enter the array on your own
array = [6,2,4,3,6,333,5,6,2,44,66,33,44,22]

# comment below if you want to use the preconfigured input
# print("Enter the array as space seperated digits")
# array = [int(i) for i in input().split(sep=" ")]

# PROGRAM PORTION

# logic behind maxheap sorting : in maxheaps the root will contain the largest element. we swap this with the
# last element in the array representation of the heap and fix its position. we do this n / 2 times with recursion.
# as a result we get the array in ascending order
def max_heap(arr,n,parent):
        largest = parent
        left =  2 * parent + 1 # Left = 2*i... here we did taking into consideration array starts at 0
        right = 2 * parent + 2 # Right = 2 * i + 1

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right 
        if largest != parent:
            arr[largest],arr[parent] = arr[parent],arr[largest]
            max_heap(arr,n,largest)

# logic behind maxheap sorting : in minheaps the root will contain the smallest element. we swap this with the
# last element in the array representation of the heap and fix its position. we do this n / 2 times with recursion.
def min_heap(arr,n,parent):
        smallest = parent
        left = 2 * parent + 1 # Left = 2*i... here we did taking into consideration array starts at 0
        right = 2 * parent + 2 # Right = 2 * i + 1
        if right < n and arr[right] < arr[smallest]:    
            smallest = right
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if smallest != parent:
            arr[smallest] , arr[parent] = arr[parent],arr[smallest]
            min_heap(arr,n,smallest)

def heapsortWithMinHeap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            min_heap(arr,n, i)
        for i in range(n - 1, 0, -1):
            arr[i],arr[0] = arr[0],arr[i]
            min_heap(arr, i, 0)
        # prints the descending order array
        print(arr)

def heapsortWithMaxHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
            max_heap(arr,n, i)
    for i in range(n - 1, 0, -1):
            arr[i],arr[0] = arr[0],arr[i]
            max_heap(arr, i, 0)
    # prints the ascending order array
    print(arr)

print("With maxHeap : ",end="")
heapsortWithMaxHeap(array)
print("With minHeap: " ,end = "")
heapsortWithMinHeap(array)