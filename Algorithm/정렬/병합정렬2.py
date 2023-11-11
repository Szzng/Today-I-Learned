# https://www.acmicpc.net/problem/1517

"""
- 문제 이름은 버블소트지만, 시간복잡도 때문에 병합정렬로 풀어야 한다.
- 버블 정렬에서 Swap이 일어나는 횟수를 구하는 문제이다.
- 병합정렬을 구현하면서, Swap이 일어나는 횟수를 구하면 된다.
- swap: right arr는 left보다 오른쪽에 있기 때문에, right arr 값이 더 작아서 선택되면 left arr의 남은 값들의 개수만큼 Swap이 일어났다는 뜻이다!
"""


def merge_sort_counting_swap(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_swap = merge_sort_counting_swap(arr[:mid])
    right, right_swap = merge_sort_counting_swap(arr[mid:])

    swap = left_swap + right_swap
    merged = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if right[right_idx] < left[left_idx]:
            merged.append(right[right_idx])
            right_idx += 1
            swap += len(left) - left_idx
        else:
            merged.append(left[left_idx])
            left_idx += 1

    if left_idx < len(left):
        merged += left[left_idx:]
    elif right_idx < len(right):
        merged += right[right_idx:]

    return merged, swap


import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

sorted_nums, swap = merge_sort_counting_swap(nums)

print(swap)
