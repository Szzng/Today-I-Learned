# https://www.acmicpc.net/problem/2342

import sys

points = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        if i == 0:
            points[i][j] = 2
        elif i == j:
            points[i][j] = 1
        elif abs(i - j) == 2:
            points[i][j] = 4
        else:
            points[i][j] = 3

nums = [0] + list(map(int, sys.stdin.readline().split()))
nums.pop()

dp = [[[-1] * 5 for _ in range(5)] for _ in range(len(nums))]  # dp[i][j][k] : i번째 수를 왼발로 j, 오른발로 k를 밟았을 때 최소값
dp[0][0][0] = 0

for i in range(1, len(nums)):
    for j in range(5):
        for k in range(5):
            if dp[i - 1][j][k] == -1:  # 이전에 밟은 적이 없으면(밟을 수 없는 경우)
                continue

            # 왼발로 밟았을 때 (오른발은 k로 고정)
            # dp[i][nums[i]][k] == -1 : 이전에 밟은 적이 없는 경우
            value = dp[i - 1][j][k] + points[j][nums[i]]
            dp[i][nums[i]][k] = value if dp[i][nums[i]][k] == -1 else min(value, dp[i][nums[i]][k])

            # 오른발로 밟았을 때 (왼발은 j로 고정)
            # dp[i][j][nums[i]] == -1 : 이전에 밟은 적이 없는 경우
            value = dp[i - 1][j][k] + points[k][nums[i]]
            dp[i][j][nums[i]] = value if dp[i][j][nums[i]] == -1 else min(value, dp[i][j][nums[i]])

result = sys.maxsize
for i in range(5):
    for j in range(5):
        if dp[-1][i][j] == -1:  # 마지막에 밟은 적이 없는 경우
            continue
        result = min(result, dp[-1][i][j])

print(result)
