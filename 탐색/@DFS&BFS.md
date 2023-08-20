# 깊이 우선 탐색 (Depth First Search)
- 그래프 완전 탐색 기법 중 하나
- 그래프의 시작 노드에서 출발하여 탐색할 한 쪽 분기를 정하여 최대 깊이까지 탐색을 마친 후 다른 분기를 탐색하는 방법
- 재귀 함수로 구현
- 스택 자료구조를 이용하여 구현
- 시간 복잡도: O(V+E) (V: 노드의 수, E: 간선의 수)

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

# 너비 우선 탐색 (Breadth First Search)
- 그래프 완전 탐색 기법 중 하나
- 그래프의 시작 노드에서 출발하여 시작 노드를 기준으로 가까운 노드부터 탐색하는 방법
- !! 탐색 시작 노드와 가까운 노드를 우선하여 탐색하므로 목표 노드에 도착하는 경로가 여러 개일 때 최단 경로를 보장
- 큐 자료구조를 이용하여 구현 (FIFO)
- 시간 복잡도: O(V+E) (V: 노드의 수, E: 간선의 수)

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
``` 
