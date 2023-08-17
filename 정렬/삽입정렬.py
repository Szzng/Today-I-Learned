# https://www.acmicpc.net/problem/11399

"""
삽입정렬
- 이미 정렬된 데이터 범위에 정렬되지 않은 데이터를 적절한 위치로 삽입시켜 정렬
- 시간복잡도 O(N^2)
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):  # 1부터 시작하는 이유는 0번째는 이미 정렬되어있다고 가정하기 때문
        for j in range(i, 0, -1):  # i부터 1까지 감소하며 반복
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr


import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

nums = insertion_sort(nums)

sums = [0] * n

for i in range(n):
    sums[i] = sums[i - 1] + nums[i] if i > 0 else nums[i]

print(sum(sums))
