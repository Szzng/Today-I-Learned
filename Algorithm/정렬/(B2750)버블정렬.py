# https://www.acmicpc.net/problem/2750

"""
# 버블정렬
- 인접한 두 수를 비교하여 큰 수를 뒤로 보내는 정렬 알고리즘
- 시간복잡도: O(n^2)

- 시간복잡도: N(1 ≤ N ≤ 1,000), 1초 -> O(N^2) 정렬 알고리즘 사용 가능
"""

n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(n - 1):  # j+1을 사용하므로 n-1까지만 반복
    for j in range(n - 1 - i):  # 반복을 할 때마다 맨 뒤부터 i개는 이미 정렬된 영역을 나타내므로, 반복할 필요가 없음.
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(*nums, sep='\n')
