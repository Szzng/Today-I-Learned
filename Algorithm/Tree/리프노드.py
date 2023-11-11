# https://www.acmicpc.net/problem/1068

"""
- dfs로 리프노드 개수 구하기
- 단, 제거 대상 노드를 만났을 때는 그 아래 자식 노드와 관련된 탐색은 하지 않음. (child == remove)
"""
import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n)]
parents = list(map(int, input().split()))

for i, parent in enumerate(parents):
    if parent == -1:
        root = i
    else:
        graph[parent].append(i)

remove = int(input())
leaf_cnt = 0


def dfs(num):
    global leaf_cnt

    ischild = False

    for child in graph[num]:
        if child != remove:
            dfs(child)
            ischild = True

    if not ischild: # 자식이 없는 경우 -> 리프노드
        leaf_cnt += 1


if remove == root:
    print(0)
else:
    dfs(root)
    print(leaf_cnt)
