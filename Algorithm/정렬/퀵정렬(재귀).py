"""
# 퀵정렬
- 기준 데이터(Pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 병합정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 퀵정렬은 추가적인 메모리가 거의 또는 전혀 필요하지 않은 '제자리 정렬(in-place sorting)' 방법
- 시간복잡도 O(NlogN), 최악의 경우 O(N^2)


- 분할 정복(divide and conquer)' 전략
1. 분할(Divide): 피벗을 기준으로 피벗보다 작은 모든 요소는 배열의 왼쪽으로, 큰 모든 요소는 오른쪽으로 이동
2. 정복(Conquer): 피벗을 기준으로 나눠진 두 개의 부분 배열에 대해 재귀적으로 다시 퀵정렬을 적용. 각 부분 배열에서도 피벗을 선택하여 반복.
분할된 부분 배열들이 충분히 작아질 때까지 반복. 배열의 크기가 충분히 작아지면 자연히 정렬 상태가 됨. 부분 배열들을 합치는 단계가 필요 없음.

# 퀵정렬(Quick Sort)에서 최악의 시간 복잡도(O(N^2))가 나오는 경우
1. 피벗 선택이 불균형적일 때
- 퀵정렬의 성능은 피벗(pivot)의 선택에 크게 의존
- 만약 피벗이 매번 가장 크거나 가장 작은 요소로 선택된다면, 분할(divide) 과정이 매우 불균형적으로 이루어짐
- 이 경우, 한 쪽은 거의 비어 있고, 다른 한 쪽에는 거의 모든 요소가 몰리게 되어 효율적인 분할이 이루어지지 않음
2. 이미 정렬된 배열 또는 거의 정렬된 배열
- 만약 배열이 이미 정렬되어 있거나 거의 정렬된 상태라면, 피벗이 최소값이나 최대값으로 선택될 가능성이 높아짐.
- 이 경우, 매 분할마다 한 쪽 부분 배열은 비어 있게 되고, 다른 쪽 부분 배열에는 n−1 개의 요소가 남게 됨.

- 이러한 최악의 시나리오를 피하기 위해 다양한 피벗 선택 전략 사용: 중간값, 랜덤 선택 등
- 이러한 전략은 분할이 보다 균등하게 이루어지도록 도와, 대체로 O(nlogn)의 평균 시간 복잡도를 달성하게 함.
"""


def quick_sort1(arr, start, end):
    # 배열의 크기가 0이나 1인 경우 더이상 정렬할 필요 없음
    if start >= end:
        return

    pivot = start
    left = start + 1  # left 포인터는 피벗보다 큰 값을 찾기 위해 오른쪽으로 이동
    right = end  # right 포인터는 피벗보다 작은 값을 찾기 위해 왼쪽으로 이동

    while left <= right:  # 엇갈릴 때까지 반복
        # 피벗보다 큰 데이터를 찾을 때까지 left 포인터를 오른쪽으로 이동
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 right 포인터를 왼쪽으로 이동
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # 포인터 교차 여부 확인 및 교체
        # 엇갈렸다면? right 포인터의 위치까지가 피벗보다 작은 값들의 영역 -> right 포함 왼쪽은 모두 피벗보다 작은 값, 오른쪽은 피벗보다 큰 값
        # 엇갈리지 않았다면? 피벗보다 큰 값과 작은 값의 위치를 서로 교환
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]  # 작은 데이터와 피벗을 교체

        else:  # 엇갈리지 않았다면: 피벗보다
            arr[left], arr[right] = arr[right], arr[left]  # 작은 데이터와 큰 데이터를 교체

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