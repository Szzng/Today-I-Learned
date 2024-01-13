# https://www.acmicpc.net/problem/1427

"""
선택정렬
- 가장 작은 수를 찾아 맨 앞으로 보내는 정렬 알고리즘
- 버블정렬과 마찬가지로 인접한 두 수를 비교하는 것이 아니라, 가장 작은 수를 찾아 맨 앞으로 보내는 것이 차이점
- 시간복잡도: O(n^2)
"""

# solution1
nums = list(input())

for i in range(len(nums)):
    max_idx = i
    for j in range(i + 1, len(nums)): # 앞쪽 i만큼은 이미 정렬된 영역을 나타냄
        if nums[j] > nums[max_idx]:
            max_idx = j

    if nums[i] < nums[max_idx]:
        nums[i], nums[max_idx] = nums[max_idx], nums[i]

print(''.join(nums))

# solution2
print(''.join(sorted(input(), reverse=True)))
