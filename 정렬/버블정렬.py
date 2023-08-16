# https://www.acmicpc.net/problem/2750

"""
버블정렬
- 인접한 두 수를 비교하여 큰 수를 뒤로 보내는 정렬 알고리즘
- 시간복잡도: O(n^2)
"""

n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(n - 1): # j+1을 사용하므로 n-1까지만 반복
    for j in range(n - 1 - i): # 뒤쪽 i만큼은 이미 정렬된 영역을 나타냄
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(*nums, sep='\n')