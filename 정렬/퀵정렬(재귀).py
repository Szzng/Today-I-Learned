"""
퀵정렬
- 기준 데이터(Pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 병합정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 시간복잡도 O(NlogN) / 최악의 경우 O(N^2)
"""


def quick_sort1(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort1(arr, start, right - 1)
    quick_sort1(arr, right + 1, end)


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left, right = [], []

    for x in tail:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort2(left) + [pivot] + quick_sort2(right)