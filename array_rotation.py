# arr = [1,2,3,4,5] after rotating by 2 [3,4,5,1,2]
# on single rotation [2,3,4,5,1]

def rotate(arr,d,n):
    temp = []
    temp = arr[:d]
    arr[:n-d] = arr[d:n]
    arr[-d:] = temp
    print "Result by method 1",arr

rotate([1,2,3,4,5],2,5)

#################### Method 2 rotating one by one ###################
def rotate_new(arr,d,n):
    temp = arr[0]
    for i in range(d):
        temp = arr[0]
        for i in range(len(arr)-1):

            arr[i] = arr[i+1]
        arr[len(arr)-1] = temp
    print "result by method 2",arr
rotate_new([1,2,3,4,5],2,5)

################### Method 3 Reversal Algorithm ####################
# Python program for reversal algorithm of array rotation

# Function to reverse arr[] from index start to end
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d-1)
    rverseArray(arr, d, n-1)
    rverseArray(arr, 0, n-1)

# Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print arr[i],

# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2) # Rotate array by 2
printArray(arr)
