# https://www.acmicpc.net/problem/1940

"""
두 재료의 합, 즉 크기를 비교하므로 값을 정렬하면 문제를 더 쉽게 풀 수 있음.
일반적으로 정렬 알고리즘의 시간 복잡도는 O(nlogn)
"""

import sys

read = sys.stdin.readline

n = int(read())
target = int(read())
materials = sorted(list(map(int, read().split())))
cnt = 0
left, right = 0, n - 1

while left < right:
    if materials[left] + materials[right] == target:
        cnt += 1
        left += 1
        right -= 1
    elif materials[left] + materials[right] < target:
        left += 1
    else:
        right -= 1

print(cnt)
