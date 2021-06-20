#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void printArray(int A[], int size)
{
int i;
for (i=0; i < size; i++)
printf("%d ", A[i]);
printf("\n");
}
void swap(int arr[],int a ,int b)
{
    int temp;
    temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}

 void bubbleSort(int arr[],int n)
{
    int i,j;
     for(i = 0; i<n - 1;i++)
    {
         for (j = 0; j < n - i - 1; j++) {
            if (arr[j + 1] < arr[j])
            {
                swap(arr,j,j+1);
                printArray(arr,n);
            }
             
        }
 
      }
}

int main()
{
    int arr[10],size;
    scanf("%d",&size);
    for(int i = 0; i < size;i++)
        scanf("%d",&arr[i]);
printf("Given array is \n");
printArray(arr, size);
    bubbleSort(arr,size);
printf("\n Sorted array is \n");
printArray(arr, size);
return 0;
}
