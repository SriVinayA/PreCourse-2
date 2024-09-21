# Python program for implementation of MergeSort

# Function to merge two halves
def merge(arr, left, mid, right):
    # Sizes of the two sub-arrays to be merged
    n1 = mid - left + 1
    n2 = right - mid

    # Temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    i = 0     # Initial index of the first sub-array
    j = 0     # Initial index of the second sub-array
    k = left  # Initial index of the merged sub-array

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Function to sort an array using merge sort
def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Recursively sort the first and second halves
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)

# Code to print the list 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver code to test the above code 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array is: ", end="\n")
    printList(arr)
