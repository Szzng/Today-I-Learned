"""
# 문제
N명의 사람이 원 형태로 앉아있고, K번째 사람을 제거한다.
이를 반복하다가 마지막 사람이 남을 때까지 계속한다.

원에서 사람들이 제거되는 순서를 (N,K)-요세푸스 순열이라고 한다.
예를 들어 (7,3)-요세푸스 순열은 <3,6,2,7,5,1,4>이다.
N과 K가 주어지면 (N,K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""

from collections import deque


def solution(N, K):
    answer = []
    q = deque(range(1, N + 1))

    while q:
        for i in range(K - 1):
            q.append(q.popleft())

        answer.append(q.popleft())

    return answer[-1]


print(solution(7, 3) == 4)
