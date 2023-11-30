# https://www.acmicpc.net/problem/1517

"""
- 시간복잡도: 1<=N<=500,000, 1초이므로 O(NlogN)인 정렬 알고리즘을 사용해야 한다.
- 문제 이름은 버블소트지만, 시간복잡도 때문에 병합정렬로 풀어야 한다.
- 버블 정렬에서 Swap이 일어나는 횟수를 구하는 문제이다.
- 병합정렬을 구현하면서, Swap이 일어나는 횟수를 구하면 된다.
- Swap: right arr는 left보다 오른쪽에 있기 때문에, right arr 값이 더 작아서 선택되면 left arr의 남은 값들의 개수만큼 Swap이 일어났다는 뜻이다!
"""


def merge_sort_counting_swap(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_swap = merge_sort_counting_swap(arr[:mid])
    right, right_swap = merge_sort_counting_swap(arr[mid:])

    merged = []
    left_idx = right_idx = 0
    swap_cnt = left_swap + right_swap

    while left_idx < len(left) and right_idx < len(right):
        if right[right_idx] < left[left_idx]:  # swap이 일어난 경우(오른쪽 배열의 값이 더 작은 경우)
            merged.append(right[right_idx])
            right_idx += 1
            swap_cnt += len(left) - left_idx  # left 배열의 남은 값들의 개수만큼 swap이 일어남
        else:
            merged.append(left[left_idx])
            left_idx += 1

    if left_idx < len(left):
        merged += left[left_idx:]
    elif right_idx < len(right):
        merged += right[right_idx:]

    return merged, swap_cnt


import sys

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

sorted_nums, swap = merge_sort_counting_swap(nums)

print(swap)
