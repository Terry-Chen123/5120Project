def checkArithmeticSubarrays(nums, l, r):
    result = []
    m = len(l)
    for i in range(m):
        lm = l[i]
        rm = r[i]
        cut = nums[lm:rm + 1]
        cut.sort()
        isAri = True
        gap = cut[1] - cut[0]
        for j in range(len(cut)):
            if j>0 and cut[j] - cut[j - 1] != gap:
                isAri = False
        result.append(isAri)
    return result


print(checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5]))

def find(a):
    start = end = 0
    max = 0
    result = ''
    while end < len(a)-1 and start <= end:
        if a[end+1] not in a[start:end+1]:
            end += 1
        else:
            if end - start + 1 > max:
                max = end - start + 1
                result = a[start:end+1]
            start += 1
            end = start
    if end - start + 1 > max:
        result = a[start:end + 1]
    return result
print(find('abcdamnolk'))
















