# https://www.acmicpc.net/problem/2251

"""
- 그래프를 그리는 방식으로 접근하는 문제
- a, b, c의 특정 무게 상태를 1개의 노드로 가정하고, 조건에 따라 이 상태에서 변경할 수 있는 이후 무게 상태가 에지로 이어진 인접한 노드가 됨
- sender, receiver 리스트를 이용하여 6가지 이동 케이스를 정의하고, 이를 이용하여 그래프를 그림
"""

from collections import deque

# 두 리스트를 이용하여 6가지 이동 케이스 정의 가능 (0: a, 1: b, 2: c를 나타냄)
# a -> b, a -> c, b -> a, b -> c, c -> a, c -> b
# index = 0 : sender[0] -> receiver[0] (a -> b)
sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]

now = list(map(int, input().split()))
max_num = 201
visited = [[False] * max_num for _ in range(max_num)]
answer = []


def bfs():
    q = deque()
    q.append((0, 0))  # a, b의 무게가 0인 상태이므로 (0,0) 노드에서 시작
    visited[0][0] = True
    answer.append(now[2])  # a의 무게가 0인 상태에서 시작하므로 c의 무게를 answer에 추가

    while q:
        now_node = q.popleft()
        a = now_node[0]
        b = now_node[1]
        c = now[2] - a - b  # a, b의 무게가 정해져 있으면 c의 무게도 정해짐

        for i in range(6):  # a->b, a->c, b->a, b->c, c->a, c->b
            next_node = [a, b, c]
            next_node[receiver[i]] += next_node[sender[i]]  # sender에서 receiver로 무게 이동
            next_node[sender[i]] = 0  # sender의 무게는 0이 됨

            if next_node[receiver[i]] >= now[receiver[i]]:  # receiver의 무게가 최대 무게보다 크거나 같으면
                next_node[sender[i]] = next_node[receiver[i]] - now[receiver[i]]  # sender의 무게를 그 차로 채움
                next_node[receiver[i]] = now[receiver[i]]  # receiver의 무게는 최대 무게가 됨

            if not visited[next_node[0]][next_node[1]]:  # a, b 무게를 기준으로 방문 여부 체크
                visited[next_node[0]][next_node[1]] = True
                q.append((next_node[0], next_node[1]))

                if next_node[0] == 0:  # a의 무게가 0이면 c의 무게를 answer에 추가
                    answer.append(next_node[2])


bfs()

print(*sorted(answer))
