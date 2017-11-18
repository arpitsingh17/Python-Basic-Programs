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
arr = [10, 3, 5, 6, 20]
print max_triplet(arr)
