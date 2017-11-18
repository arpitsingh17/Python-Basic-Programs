# s1 = "string"
# s2 = "strong"
#
# sets1 = set(s1)
# sets2 = set(s2)
#
# print sets1 & sets2

arr = [10, 3, 5, 6, 20]

# max = 0
# def max_triplet_product(arr):
#     if len(arr) < 3:
#         return False
#     elif len(arr) == 3:
#         return (arr[0]*arr[1]*arr[2])
#     else:
#         max = arr[0]*arr[1]*arr[2]
#         for i in range(len(arr)-2):
#             if max < arr[i] * arr[i+1] * arr[i+2]:
#                 max = arr[i] * arr[i+1] * arr[i+2]
#     return max
#
# print max_triplet_product(arr)

def max_triplet(arr):
    min1 = min2 = max1 = max2 = max3 = 0
    for num in arr:
        if min1 >= num:
            min2 = min1
            min1 = num
        elif min2 > num:
            min2 = num

        if max1<num:
            max3 = max2
            max2 = max1
            max1 = num

        elif max2 < num:
            max3 = max2
            max2 = num

        elif max3 < num:
            max3 = num

    return max(min1*min2*max1,max1*max2*max3)

print max_triplet(arr)


