import numpy as np

input_list = []
while True:
    line = input()
    if line:
        k = line.split()
        input_list.append(k)
    else:
        break

target = int(input_list[0][1])
weight = []
value = []
num = []
for i in range(1, int(input_list[0][0]) + 1):
    num.append(int(input_list[i][0]))
    weight.append(int(input_list[i][1]))
    value.append(int(input_list[i][2]))

F = [0 for i in range(0, target + 1)]
n = int(input_list[0][0])

#背包问题
def solution(max_weight, weight, value, num):
    dp = np.zeros((n + 1, max_weight + 1), dtype=int)

    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if weight[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                count = min(num[-1], j // weight[i - 1])
                dp[i][j] = dp[i - 1][j]
                for k in range(1, count + 1):
                    temp = dp[i - 1][j - k * weight[i - 1]] + k * value[i - 1]
                    if temp > dp[i][j]:
                        dp[i][j] = temp
    print(dp[n][-1])


solution(target, weight, value, num)











