# https://www.acmicpc.net/problem/11399

"""
# 삽입정렬
- 이미 정렬된 부분과 그렇지 않은 부분으로 나누어, 정렬되지 않은 부분의 원소를 적절한 위치에 삽입하는 방식
- 시간복잡도 O(N^2)

# insertion_sort1 vs insertion_sort2
- insertion_sort1(Insert version) -> 더 비효율적 (원소 이동을 위해 추가적인 k 반복문 사용)
    - 삽입할 위치를 찾는 과정과 원소를 이동시키는 과정이 분리되어 있음
    - 원소를 뒤로 이동시키기 위해 "추가적인 반복문"을 사용. 이는 원소가 많을수록 더 많은 연산을 필요로 하게 됨.

- insertion_sort2 (Swap version) -> 더 효율적
    - 삽입할 위치를 찾는 과정과 원소를 교환하는 과정이 동시에 이루어짐
    - 원소를 교환하는 방식을 사용하며, 적절한 위치를 찾으면 즉시 다음 원소로 넘어감.
    - 이 방식은 필요한 경우에만 원소를 교환하므로, 특히 부분적으로 정렬된 배열에서 더 효율적일 수 있음.
"""


# Insert version
def insertion_sort1(arr):
    for i in range(1, len(arr)):  # 1부터 시작하는 이유는 0번째는 이미 정렬되어있다고 가정하기 때문
        insert_idx = i
        insert_value = arr[i]

        for j in range(i - 1, -1, -1):  # 이미 정렬된 데이터 범위(0 ~ i - 1)에서 적절한 위치를 찾아 삽입
            if arr[j] < arr[i]:
                insert_idx = j + 1
                break

            if j == 0:  # 삽입할 위치가 없어서 j가 0이 되었을 때
                insert_idx = 0

        # 삽입할 위치에 삽입 arr.insert(insert_idx, arr.pop(i))
        for k in range(i, insert_idx, -1):
            arr[k] = arr[k - 1]  # 삽입할 위치까지 데이터를 한 칸씩 뒤로 이동
        arr[insert_idx] = insert_value  # 삽입할 위치에 삽입

    return arr


# Swap version
def insertion_sort2(arr):
    for i in range(1, len(arr)):  # 1부터 시작하는 이유는 0번째는 이미 정렬되어있다고 가정하기 때문
        for j in range(i, 0, -1):  # i부터 1까지 감소하며 반복 - 이미 정렬된 데이터 범위(0 ~ i - 1)에서 적절한 위치를 찾아 삽입
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:  # 크기 순으로 정렬되어있기 때문에 삽입할 위치를 찾았다면 더 이상 반복할 필요가 없음
                break

    return arr


import sys

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

nums = insertion_sort1(nums)

sums = [0] * n

for i in range(n):
    sums[i] = sums[i - 1] + nums[i] if i > 0 else nums[i]

print(sum(sums))
