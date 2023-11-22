# https://www.acmicpc.net/problem/17298


"""
- 오큰수: 오른쪽에 있으면서 자신보다 큰 수 중에서 가장 왼쪽에 있는 수 (= 오른쪽에 있으면서 자신보다 큰 수 중에서 가장 가까운 수)
- 다시 보고 연습 강력추천!!!

- 스택의 기본 개념을 이해하고 적용하는 문제!
- 스택의 후입선출이라는 독특한 성질이 종종 시간 복잡도를 줄이거나 특정한 문제의 조건을 손쉽게 해결하는 실마리가 될 때가 있습니다.
- 문제에 접근할 때 혹시 스택을 이용하면 손쉽게 풀리지 않는지 한 번쯤 고민해 보세요.
"""

from sys import stdin

read = stdin.readline

n = int(read())
nums = list(map(int, read().split()))
stack = []
result = [-1] * n

for idx, num in enumerate(nums):
    # 이렇게 하면 스택에는 num을 기준으로 왼쪽에 있는 수 중에서 num보다 큰 수들만 남게 됨.
    # 결국 스택에는 num보다 큰 수들이 큰 수부터 작은 수 순서로 내림차순 정렬되어 있음.
    while stack and stack[-1][1] < num:
        result[stack.pop()[0]] = num

    stack.append((idx, num))

print(*result)
