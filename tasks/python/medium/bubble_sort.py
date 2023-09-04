# Python - Medium

def bubble_sort(arr):
    # TODO: Implement the bubble sort algorithm
    n=len(arr)
    swap=False
    for i in range(0,n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                swap=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
            if not swap:
                return

#! Test cases (Don't edit):
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)
