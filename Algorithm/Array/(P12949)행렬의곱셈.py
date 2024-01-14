# https://school.programmers.co.kr/learn/courses/30/lessons/12949?language=python3

def solution1(arr1, arr2):
    row1, col1, row2, col2 = len(arr1), len(arr1[0]), len(arr2), len(arr2[0])

    answer = [[0] * col2 for _ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


def solution2(arr1, arr2):
    return [[sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*arr2)] for row1 in arr1]


def solution3(arr1, arr2):
    import numpy as np
    return np.dot(arr1, arr2).tolist()


test_cases = [
    ([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]], [[15, 15], [15, 15], [15, 15]]),
    ([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]], [[22, 22, 11], [36, 28, 18], [29, 20, 14]])
]

solutions = [solution1, solution2, solution3]

for arr1, arr2, expected in test_cases:
    for solution in solutions:
        assert solution(arr1, arr2) == expected
        print(f"{solution.__name__} with arr1: {arr1} and arr2: {arr2} passed!")

print("All tests passed!")
