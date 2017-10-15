# arr = [1,2,3,4,5] after rotating by 2 [3,4,5,1,2]

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
