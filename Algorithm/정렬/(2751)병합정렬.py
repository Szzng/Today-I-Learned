# https://www.acmicpc.net/problem/2751

"""
병합정렬
- 분할 정복 알고리즘의 하나
- 데이터를 최소 단위까지 나누어 정렬한 후, 다시 합치면서 정렬하는 방식
- 재귀함수를 이용하여 구현
- 시간복잡도 O(nlogn)
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid]) # 왼쪽 부분 정렬
    right = merge_sort(arr[mid:]) # 오른쪽 부분 정렬

    merged = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        merged += left[left_idx:]
    elif right_idx < len(right):
        merged += right[right_idx:]

    return merged


import sys

read = sys.stdin.readline
write = sys.stdout.write

n = int(read())
nums = [int(read()) for _ in range(n)]

merged_nums = merge_sort(nums)

write('\n'.join(map(str, merged_nums)))
