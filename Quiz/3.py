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
#print(find('abcdamnolk'))


input_list = []
while True:
    try:
        line = input()
        input_list.append(line.split())
    except:
        break
x,y,z = int(input_list[0][0]),int(input_list[0][1]),int(input_list[0][2])
n,m = int(input_list[1][0]),int(input_list[1][1])
q = int(input_list[2][0])
rest = input_list[3:3+q]
def shun(x,y,m):
    return y, m-x
def fan(x,y,m):
    return x, m-y
def ni(x,y,m):
    return m-y, x
result = []
for pair in rest:
    i = j = k =0
    pair_x,pair_y = int(pair[0]),int(pair[1])
    while i < x:
        pair_x, pair_y = shun(pair_x, pair_y, m)
        i +=1
    while j < y:
        pair_x, pair_y = fan(pair_x, pair_y, m)
        j +=1
    while k < z:
        pair_x, pair_y = ni(pair_x, pair_y, m)
        k += 1
    result.append([pair_x,pair_y])
for each in result:
    print (each[0],each[1])

a = [1,2,3]
b = a
b.append(1)
print(a)


























