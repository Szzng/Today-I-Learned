# https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3

def solution(nums):
    n = len(nums)
    answer = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            answer.add(nums[i] + nums[j])

    return sorted(list(answer))


print(solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7])
print(solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12])
