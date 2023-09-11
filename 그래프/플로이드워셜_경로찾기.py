# https://www.acmicpc.net/problem/11403

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드 워셜 알고리즘
for k in range(n):  # k: 거쳐가는 노드
    for i in range(n):  # i: 출발 노드
        for j in range(n):  # j: 도착 노드
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])
