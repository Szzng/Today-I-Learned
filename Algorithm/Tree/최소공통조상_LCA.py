# https://www.acmicpc.net/problem/11437

from collections import deque
import sys

read = sys.stdin.readline

n = int(read())
tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0] * (n + 1)
depth = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, read().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs(root):
    q = deque([root])
    visited[root] = True

    while q:
        node = q.popleft()

        for child in tree[node]:
            if not visited[child]:
                q.append(child)
                visited[child] = True
                parent[child] = node
                depth[child] = depth[node] + 1


bfs(1)


def lca(x, y):
    if depth[x] < depth[y]:
        x, y = y, x  # x가 더 깊은 노드가 되도록

    while depth[x] != depth[y]:  # 두 노드의 깊이가 같아질 때까지
        x = parent[x]  # 더 깊은 노드를 위로 올림

    while x != y:  # 두 노드가 같아질 때까지 (두 노드가 같아지는 순간이 LCA)
        x = parent[x]  # 두 노드를 동시에 위로 올림
        y = parent[y]

    return x


m = int(read())
dic = {}  # 같은 질문일 경우 재계산을 하지 않기 위해 딕셔너리 자료형 사용 -> 시간초과 해결 방법
for _ in range(m):
    a, b = map(int, read().split())

    if (a, b) not in dic or (b, a) not in dic:
        dic[(a, b)] = dic[(b, a)] = lca(a, b)  # 두 노드의 LCA를 딕셔너리에 저장

    print(dic[(a, b)])
