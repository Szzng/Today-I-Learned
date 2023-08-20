# https://www.acmicpc.net/problem/1920


import sys

read = sys.stdin.readline

n = int(read())
nums = sorted(list(map(int, read().split())))  # 이진 탐색은 정렬된 상태에서만 가능

m = int(read())
targets = list(map(int, read().split()))

for target in targets:
    start = 0
    end = n - 1
    flag = 0

    while start <= end:
        mid = (start + end) // 2

        if target == nums[mid]:
            flag = 1
            break
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    print(flag)
