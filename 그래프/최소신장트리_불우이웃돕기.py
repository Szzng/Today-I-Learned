# https://www.acmicpc.net/problem/1414

from queue import PriorityQueue

n = int(input())

edges = PriorityQueue()
total_length = 0


for i in range(n):
    strings = list(input())

    for j, string in enumerate(strings):
        if string.islower():
            length = ord(string) - ord('a') + 1  # 알파벳 순서를 숫자로 변환
        elif string.isupper():
            length = ord(string) - ord('A') + 27  # 알파벳 순서를 숫자로 변환
        else:
            length = 0

        total_length += length  # 총 랜선 길이에 더함

        if i != j and length != 0:  # 자기 자신이 아니고, 연결 랜선이 있다면
            edges.put((length, i, j))  # 랜선 길이를 기준으로 정렬하기 위해 랜선 길이를 맨 앞에 둠 (랜선 길이, 정점1, 정점2)

parent = [i for i in range(n)]  # 사이클 생성 여부를 판단하기 위한 유니온 파인드용 부모 리스트


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x


use_edges = 0  # 사용한 에지의 수
total_cost = 0  # 총 가중치

while not edges.empty(): # 모든 에지를 사용할 때까지 반복
    cost, a, b = edges.get()  # 가중치가 가장 작은 에지를 꺼냄

    if find(a) != find(b):  # 두 정점의 부모가 같지 않다면 (사이클이 생성되지 않는다면)
        union(a, b)  # 두 정점을 연결
        total_cost += cost  # 가중치를 더함
        use_edges += 1  # 사용한 에지의 수를 더함

if use_edges == n - 1:  # 모든 정점을 연결했다면 (최소신장트리는 정점의 수 - 1개의 에지로 구성됨)
    print(total_length - total_cost)  # 총 랜선 길이에서 총 가중치를 뺌
else: # 모든 정점을 연결하지 못했다면
    print(-1)
