# https://www.acmicpc.net/problem/2178

"""
- 지나야 하는 칸 수의 최솟값을 구하는 문제
- 완전 탐색을 진행하며 몇 번째 깊이에서 원하는 값을 찾을 수 있는지를 구하는 문제
- BFS를 사용해 최초로 도달했을 때의 깊이를 출력

# BFS를 사용해야 하는 이유
- BFS는 시작 노드에서 가장 가까운 노드부터 방문하며 점차 멀어지는 순서로 탐색하므로, 최단 거리를 구하는 알고리즘

# DFS를 사용할 수 없는 이유 (DFS는 최단 거리를 보장하지 않고 경로의 존재 여부만 판단)
- 반면 DFS는 가능한 한 깊이 들어가면서 탐색 진행 = 미로의 한 방향으로 계속해서 진행하다가 막히면 다시 돌아와서 다른 방향으로 탐색 진행
- DFS는 항상 최단 경로를 보장X: DFS는 처음 발견된 경로를 따라 깊이 탐색하기 때문에, 더 짧은 경로가 있더라도 이를 놓칠 수 있음.
- DFS는 탐색 과정에서 막다른 길에 도달할 경우, 이전 분기점까지 되돌아가야 함 = 복잡한 미로에서 많은 백트래킹을 필요로 하며, 탐색에 필요한 시간과 메모리 사용량이 증가.
"""

from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 상하좌우
DELTA = [(0, 1), (0, -1), (-1, 0), (1, 0)]
CAN_GO = 1

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == CAN_GO and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

                maze[nx][ny] = maze[x][y] + 1

bfs()
print(maze[n - 1][m - 1])
