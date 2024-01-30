"""
# 문제
정수 배열 nums와 정수 target이 주어지면, nums에 있는 두 개의 숫자를 더해서 target을 만들 수 있는지 찾으시오.
- n은 2 이상 10^4 이하의 자연수
- nums에는 중복된 숫자가 없다.
- numsdml dnjsthsms 1 이상 10,000 이하의 자연수
- target은 1 이상 20,000 이하의 자연수

# 풀이
1. O(n) : 각 원소에 대해 target에서 자신을 뺀 나머지 원소가 존재하는지 확인 -> 계수 정렬 알고리즘을 이용, 해시 테이블에 저장
2. O(n^2) : 각 원소에 대해 자신을 제외한 나머지 원소를 전부 더하며 target과 비교
"""


def count_sort(nums, k):
    hashtable = [0] * (k + 1)

    for num in nums:
        if num > k:
            continue

        hashtable[num] += 1

    return hashtable


def solution(nums, target):
    hashtable = count_sort(nums, target)

    for num in nums:
        if num > target:
            continue

        diff = target - num

        if diff != num and hashtable[diff] > 0:
            return True

    return False


print(solution([1, 2, 3, 4, 8], 6) == True)
print(solution([2, 3, 5, 9], 10) == False)
