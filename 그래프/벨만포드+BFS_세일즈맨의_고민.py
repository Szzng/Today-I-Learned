# https://www.acmicpc.net/problem/1219

"""
- 기존 벨만-포드는 최단 거리를 구하는 알고리즘이지만, 이 문제는 최단 거리를 구하는 것이 아니라 최대 이익을 구하는 것이므로 업데이트 방식을 반대로 변경해야 한다.
- 또한 돈을 무한히 벌 수 있다는 조건이 있으므로 음수 사이클이 아닌 양수 사이클을 찾도록 변경해야 한다.
"""
import sys

n, start_city, end_city, m = map(int, input().split())
edges = []
dist = [-sys.maxsize] * n

for _ in range(m):
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

city_money = list(map(int, input().split()))  # 각 도시에 있는 돈의 최댓값

dist[start_city] = city_money[start_city]  # 출발 도시의 돈의 최댓값으로 초기화

for _ in range(n - 1):
    for start, end, price in edges:
        if dist[start] != -sys.maxsize and dist[end] < dist[start] - price + city_money[end]:
            dist[end] = dist[start] - price + city_money[end]

def is_connected(s, e):
    q = [s]
    visited = [False] * n
    visited[s] = True

    while q:
        now = q.pop(0)

        if now == e:
            return True

        for u, v, w in edges:
            if u == now and not visited[v]: # now -> v로 가는 간선이 존재하고, v를 방문한 적이 없다면
                q.append(v)
                visited[v] = True


# 양수 사이클이 존재하는지 확인
for start, end, price in edges:
    if dist[start] != -sys.maxsize and dist[end] < dist[start] - price + city_money[end]:
        if is_connected(end, end_city):
            print("Gee")
            exit()

print(dist[end_city] if dist[end_city] != -sys.maxsize else "gg")
