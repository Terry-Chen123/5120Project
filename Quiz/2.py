def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [i for i in nums if i < pivot]
    middle = [i for i in nums if i == pivot]
    right = [i for i in nums if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)

#print(quick_sort([2,3,5,1,0]))


import sys

# 读取第一行的n,m
first_line = sys.stdin.readline().strip()
n, m = int(first_line[0]), int(first_line[2])
ans = []
for i in range(n):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    ans += values

max_price = max(ans)
min_price = min(ans)
gap = m - (max_price - min_price)
if max_price - min_price > 2 * m:
    print(-1)
elif m < max_price - min_price <= 2 * m:
    print(max_price - m, min_price + m)
elif max_price - min_price <= m:
    print(min_price - gap, max_price + gap)


