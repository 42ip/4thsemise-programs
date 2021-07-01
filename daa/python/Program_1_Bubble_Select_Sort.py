
# Q:1A
# Algorithm to sort an array using bubble sort
# Time complexity : O(N^2), where N is length of array. 
# Space complexity : O(1) ,where we swap with a temp variable



# INPUT PORTION
# comment below if you want to use input
arr = [6,4,3,6,3,5,7,32,4,7,4,3,23]

# comment below if you want to use the preconfigured array
# print("Enter the length of the array")
# n = int(input())
# print("Enter the array as a space seperated integer list")
# arr = [int(i) for i  in input().split(" ")]

# PROGRAM PORTION
def bubbleSort():
    n = len(arr)
    # Idea behind a bubble sort is that it slowly brings to the ends the smaller and larger elements, like a bubble
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j],arr[j + 1]
    print(arr)


# Q:1B
# Algorithm to sort an array using select sort
# Time complexity : O(N^2), where N is length of array. 
# Space complexity : O(1) where we use a variable to swap elements

def selectionSort():
    n = len(arr)
    # Idea behind a select sort is that it finds the smallest or largest and sticks it to a side
    for i in range(n):
        small = i
        for j in range(i + 1,n):
            if arr[j] < arr[small]:
                small = j
        arr[small],arr[i] = arr[i],arr[small]
    print(arr)

print("sorted with bubble sort")
bubbleSort()

print("sorted with selection sort")
selectionSort()