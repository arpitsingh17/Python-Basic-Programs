import pytest
def arrange_even_odd(nums):
    start = 0
    last = 1
    if len(nums)>0 and len(nums)%2 == 0:
        while start != len(nums) and last != len(nums)-1:


            if (nums[start] + start)%2 == 0:
                start += 2

            if (nums[last] + last)%2 == 0:
                last -= 2

            if (nums[start] + start)%2 != 0 and (nums[last] + last) %2 != 0:

                    nums[start],nums[last] = nums[last],nums[start]
                    start+=2
                    last+=2


        return nums
    else:
        return False


print arrange_even_odd([1,3,2,5,4,6,9,0])
