# https://www.acmicpc.net/problem/1931

"""
리스트 2중 조건 정렬 방법 -> 튜플
리스트.sort(key=lamda x: (x[1], x[0]))
"""

import sys
read = sys.stdin.readline

n = int(read())
nums = [list(map(int, read().split())) for _ in range(n)]

# 종료 시각으로 1차 정렬, 시작 시각으로 2차 정렬
nums.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for num in nums:
    if num[0] >= end_time:
        end_time = num[1]
        count+=1

print(count)
