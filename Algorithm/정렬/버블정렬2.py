# https://www.acmicpc.net/problem/1377

"""
버블정렬
- 버블정렬의 swap이 한 번도 일어나지 않은 루프가 언제인지 = 이미 모든 데이터가 정렬 완료된 때를 찾는 문제
- 그러나 n의 최대범위가 500,000이므로 버블정렬의 O(n^2)은 시간초과

- 안쪽 루프는 1에서 n-j까지, 즉 왼쪽에서 오른쪽으로 이동하면서 swap을 한다.
- 이는 특정 데이터가 안쪽 루프에서 swap의 왼쪽으로 이동할 수 있는 최대거리가 1이라는 뜻이다.
- 따라서 데이터 정렬 전 index와 정렬 후 index를 비교해 왼쪽으로 가장 많이 이동한 값을 찾으면 된다.
"""

import sys
read = sys.stdin.readline

n = int(read())
nums = [(int(read()), i) for i in range(n)]
sorted_nums = sorted(nums)

max_move = 0
for i in range(n):
    move = sorted_nums[i][1] - i  # 정렬 전 index - 정렬 후 index(=i)
    if move > max_move:
        max_move = move

print(max_move + 1)  # swap이 한 번도 일어나지 않은 루프가 마지막에 1번 있으므로 +1
