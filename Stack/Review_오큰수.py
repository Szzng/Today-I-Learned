# https://www.acmicpc.net/problem/17298


"""
- 오큰수: 오른쪽에 있으면서 자신보다 큰 수 중에서 가장 왼쪽에 있는 수
- 스택의 기본 개념을 이해하고 적용하는 문제!
- 다시 보고 연습 강력추천!!!
"""

from sys import stdin

read = stdin.readline

n = int(read())
nums = list(map(int, read().split()))
stack = []
result = [-1] * n

for idx, num in enumerate(nums):
    while stack and stack[-1][1] < num:
        result[stack.pop()[0]] = num

    stack.append((idx, num))

print(*result)
