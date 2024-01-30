# https://www.acmicpc.net/problem/14425

"""
# 트라이
- 문자열 집합을 표현하는 트리
- 트라이는 단어들을 사전의 형태로 생성한 후 트리의 부모 자식 관계를 이용해 문자열을 표현 및 검색하는 트리
- 루트 노트는 항상 빈 문자열을 뜻하는 공백 상태를 유지
- N진 트리 형태 (ex. 영어 알파벳의 경우 N = 26)
- 문자열의 길이가 M이라면, 시간복잡도는 O(M)
- 문자열의 길이가 길어지면 메모리를 많이 차지하게 됨

# 문제
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서
집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.
다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다.
집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

# 출력
첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

# 시간제한: 2초
# 시간복잡도:
"""

import sys


class Node:
    def __init__(self, is_end=False):
        self.is_end = is_end
        self.children = {}


class Trie:
    def __init__(self):
        # 루트 노드는 항상 빈 문자열을 뜻하는 공백 상태를 유지
        self.root = Node()

    def insert(self, word):
        curr_node = self.root

        for char in word:
            # 자식 노드에 없으면 새로 자식 노드 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node()

            # 자식 노드로 이동
            curr_node = curr_node.children[char]

        curr_node.is_end = True  # 마지막 노드에는 is_end = True

    def search(self, word):
        curr_node = self.root

        for char in word:
            # 자식 노드에 없으면 False
            if char not in curr_node.children:
                return False

            # 자식 노드로 이동
            curr_node = curr_node.children[char]

        # 마지막 노드의 is_end 반환
        return curr_node.is_end


read = sys.stdin.readline

N, M = map(int, read().split())

trie = Trie()
for _ in range(N):
    trie.insert(read())

cnt = 0
for _ in range(M):
    if trie.search(read()):
        cnt += 1

print(cnt)
