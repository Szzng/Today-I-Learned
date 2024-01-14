# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    scores = [0] * 3

    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if pattern[i % len(pattern)] == answer:
                scores[j] += 1

    max_score = max(scores)
    result = []

    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)

    return result


print(solution([1, 2, 3, 4, 5]) == [1])
print(solution([1, 3, 2, 4, 2]) == [1, 2, 3])
