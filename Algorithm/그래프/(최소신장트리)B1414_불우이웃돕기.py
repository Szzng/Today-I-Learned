# https://www.acmicpc.net/problem/1414


"""
# 문제
다솜이는 불우이웃 돕기 활동을 하기 위해 무엇을 할지 생각했다.
마침 집에 엄청나게 많은 랜선이 있다는 것을 깨달았다.
마침 랜선이 이렇게 많이 필요 없다고 느낀 다솜이는 랜선을 지역사회에 봉사하기로 했다.

다솜이의 집에는 N개의 방이 있다.
각각의 방에는 모두 한 개의 컴퓨터가 있다.
각각의 컴퓨터는 랜선으로 연결되어 있다.
어떤 컴퓨터 A와 컴퓨터 B가 있을 때, A와 B가 서로 랜선으로 연결되어 있거나, 또 다른 컴퓨터를 통해서 연결이 되어있으면 서로 통신을 할 수 있다.

다솜이는 집 안에 있는 N개의 컴퓨터를 모두 서로 연결되게 하고 싶다.

N개의 컴퓨터가 서로 연결되어 있는 랜선의 길이가 주어질 때,
다솜이가 기부할 수 있는 랜선의 길이의 최댓값을 출력하는 프로그램을 작성하시오.

# 입력
첫째 줄에 컴퓨터의 개수 N이 주어진다.
둘째 줄부터 랜선의 길이가 주어진다.
i번째 줄의 j번째 문자가 0인 경우는 컴퓨터 i와 컴퓨터 j를 연결하는 랜선이 없음을 의미한다.
그 외의 경우는 랜선의 길이를 의미한다.
랜선의 길이는 a부터 z는 1부터 26을 나타내고,
A부터 Z는 27부터 52를 나타낸다.

N은 50보다 작거나 같은 자연수이다.

# 출력
첫째 줄에 다솜이가 기부할 수 있는 랜선의 길이의 최댓값을 출력한다. 만약, 모든 컴퓨터가 연결되어 있지 않으면 -1을 출력한다.

# 시간제한: 초
# 시간복잡도:
"""
import sys


class UnionFind:
    def __init__(self, num_nodes):
        self.parent = [i for i in range(num_nodes)]

    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_y] = root_x


num_nodes = int(sys.stdin.readline())
edges = []
lan_length = 0

for i in range(num_nodes):
    strings = sys.stdin.readline()

    for j, char in enumerate(strings):
        # 알파벳 순서를 숫자로 변환
        if char.islower():
            length = ord(char) - ord('a') + 1
        elif char.isupper():
            length = ord(char) - ord('A') + 27
        else:
            length = 0

        lan_length += length

        if i != j and length != 0:  # 자기 자신이 아니고, 연결 랜선이 있다면
            edges.append((i, j, length))

edges.sort(key=lambda x: x[2])

used_edges = 0
used_lan_length = 0
UF = UnionFind(num_nodes)

for node1, node2, length in edges:
    if used_edges == num_nodes - 1:
        break

    if UF.find(node1) != UF.find(node2):
        UF.union(node1, node2)
        used_lan_length += length
        used_edges += 1

if used_edges == num_nodes - 1:  # 모든 정점을 연결했다면 (최소신장트리는 정점의 수 - 1개의 에지로 구성됨)
    print(lan_length - used_lan_length)  # 총 랜선 길이에서 총 가중치를 뺌
else:  # 모든 정점을 연결하지 못했다면
    print(-1)
