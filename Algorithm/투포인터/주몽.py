# https://www.acmicpc.net/problem/1940

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
