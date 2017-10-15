# arr = [1,2,3,4,5] after rotating by 2 [3,4,5,1,2]
def rotate(arr,d,n):
    temp = []
    temp = arr[:d]
    arr[:n-d] = arr[d:n]
    arr[-d:] = temp
    print arr
    print temp
rotate([1,2,3,4,5],2,5)
