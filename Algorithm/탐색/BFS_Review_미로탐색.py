# https://www.acmicpc.net/problem/2178

"""
- 지나야 하는 칸 수의 최솟값을 구하는 문제
- 완전 탐색을 진행하며 몇 번째 깊이에서 원하는 값을 찾을 수 있는지를 구하는 문제
- BFS를 사용해 최초로 도달했을 때의 깊이를 출력 (BFS는 최단 거리를 구하는 알고리즘)
"""
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 상하좌우
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        now = q.popleft()

        for dx, dy in move:
            x, y = now[0] + dx, now[1] + dy
            if 0 <= x < n and 0 <= y < m:
                if maze[x][y] == 1 and not visited[x][y]:
                    q.append((x, y))
                    visited[x][y] = True
                    maze[x][y] += maze[now[0]][now[1]]


bfs(0, 0)
print(maze[n - 1][m - 1])
