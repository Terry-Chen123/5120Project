def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [i for i in nums if i < pivot]
    middle = [i for i in nums if i == pivot]
    right = [i for i in nums if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)

#print(quick_sort([2,3,5,1,0]))

l = [1,2,3]
l[0] = 2
print(l)

