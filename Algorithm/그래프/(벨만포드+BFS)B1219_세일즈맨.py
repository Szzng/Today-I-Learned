# https://www.acmicpc.net/problem/1219

"""
# 문제
오민식은 세일즈맨이다. 오민식의 회사 사장님은 오민식에게 물건을 최대한 많이 팔아서 최대 이윤을 남기라고 했다.
어떻게 하면 최대 이윤을 낼 수 있을까?

이 나라에는 N개의 도시가 있다.
도시는 0번부터 N-1번까지 번호 매겨져 있다.
오민식의 여행은 A도시에서 시작해서 B도시에서 끝난다.

오민식이 이용할 수 있는 교통수단은 여러 가지가 있다.
오민식은 모든 교통수단의 출발 도시와 도착 도시를 알고 있고, 비용도 알고 있다.
게다가, 오민식은 각각의 도시를 방문할 때마다 벌 수 있는 돈을 알고있다.
이 값은 도시마다 다르며, 액수는 고정되어있다.
또, 도시를 방문할 때마다 그 돈을 벌게 된다.

오민식은 도착 도시에 도착할 때, 가지고 있는 돈의 액수를 최대로 하려고 한다.
이 최댓값을 구하는 프로그램을 작성하시오.

오민식이 버는 돈보다 쓰는 돈이 많다면, 도착 도시에 도착할 때 가지고 있는 돈의 액수가 음수가 될 수도 있다.
또, 같은 도시를 여러 번 방문할 수 있으며, 그 도시를 방문할 때마다 돈을 벌게 된다.
모든 교통 수단은 입력으로 주어진 방향으로만 이용할 수 있으며, 여러 번 이용할 수도 있다.

# 입력
첫째 줄에 도시의 수 N과 시작 도시, 도착 도시 그리고 교통 수단의 개수 M이 주어진다.

둘째 줄부터 M개의 줄에는 교통 수단의 정보가 주어진다.
교통 수단의 정보는 “시작 끝 가격”과 같은 형식이다.

마지막 줄에는 오민식이 각 도시에서 벌 수 있는 돈의 최댓값이 0번 도시부터 차례대로 주어진다.

N과 M은 50보다 작거나 같고, 돈의 최댓값과 교통 수단의 가격은 1,000,000보다 작거나 같은 음이 아닌 정수이다.

# 출력
첫째 줄에 도착 도시에 도착할 때, 가지고 있는 돈의 액수의 최댓값을 출력한다.
만약 오민식이 도착 도시에 도착하는 것이 불가능할 때는 "gg"를 출력한다.
그리고, 오민식이 도착 도시에 도착했을 때 돈을 무한히 많이 가지고 있을 수 있다면 "Gee"를 출력한다.

# 시간제한: 2초
# 시간복잡도:

# 풀이
- 기존 벨만-포드는 최단 거리를 구하는 알고리즘이지만, 이 문제는 최단 거리를 구하는 것이 아니라 최대 이익을 구하는 것이므로 업데이트 방식을 반대로 변경해야 한다.
- 또한 돈을 무한히 벌 수 있다는 조건이 있으므로 음수 사이클이 아닌 양수 사이클을 찾도록 변경해야 한다.
"""
import sys
from collections import deque


def relax_edges(num_nodes, edges, distance):
    for _ in range(num_nodes - 1):  # 최대 num_nodes-1번만큼 반복
        for start, end, price in edges:
            if distance[start] != -sys.maxsize and distance[end] < distance[start] - price + city_money[end]:
                distance[end] = distance[start] - price + city_money[end]


def detect_positive_cycle_to_end_city(edges, distance):
    for start, end, price in edges:
        if distance[start] != -sys.maxsize and distance[end] < distance[start] - price + city_money[end]:
            if is_connected_to_end_city(end):  # 양수 사이클이 존재하고, 도착 도시와 연결되어 있다면
                return True
    return False


def is_connected_to_end_city(city):
    q = deque([city])
    visited = [False] * num_nodes
    visited[city] = True

    while q:
        curr_node = q.popleft()

        if curr_node == end_city:
            return True

        for start, end, _ in edges:
            if start == curr_node and not visited[end]:
                q.append(end)
                visited[end] = True

    return False


num_nodes, start_city, end_city, num_edges = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(num_edges)]
city_money = list(map(int, sys.stdin.readline().split()))
distance = [-sys.maxsize] * num_nodes
distance[start_city] = city_money[start_city]  # 출발 도시의 돈의 최댓값으로 초기화

relax_edges(num_nodes, edges, distance)

if detect_positive_cycle_to_end_city(edges, distance):
    print("Gee")
else:
    print(distance[end_city] if distance[end_city] != -sys.maxsize else "gg")
