# https://www.acmicpc.net/problem/14425

"""
트라이
- 문자열 집합을 표현하는 트리
- 트라이는 단어들을 사전의 형태로 생성한 후 트리의 부모 자식 관계를 이용해 문자열을 표현 및 검색하는 트리
- 루트 노트는 항상 빈 문자열을 뜻하는 공백 상태를 유지
- 문자열의 길이가 M이라면, 시간복잡도는 O(M)
- 문자열의 길이가 길어지면 메모리를 많이 차지하게 됨
"""

"""
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
"""


def trie_solution():
    class Node:
        def __init__(self, is_end=False):
            self.is_end = is_end
            self.children = {}

    class Trie:
        def __init__(self):
            self.root = Node()

        def insert(self, word):
            now_node = self.root

            for char in word:
                if char not in now_node.children:  # 자식 노드에 없으면 새로 자식 노드 생성
                    now_node.children[char] = Node()

                now_node = now_node.children[char]  # 자식 노드로 이동

            now_node.is_end = True  # 마지막 노드에는 is_end = True

        def search(self, word):
            now_node = self.root

            for char in word:
                if char not in now_node.children:  # 자식 노드에 없으면 False
                    return False

                now_node = now_node.children[char]  # 자식 노드로 이동

            return now_node.is_end  # 마지막 노드의 is_end 반환

    import sys

    read = sys.stdin.readline

    n, m = map(int, read().split())
    trie = Trie()

    for _ in range(n):
        trie.insert(read().strip())

    cnt = 0

    for _ in range(m):
        if trie.search(read().strip()):
            cnt += 1

    print(cnt)


def set_solution():
    import sys

    read = sys.stdin.readline

    n, m = map(int, read().split())
    s = set([read().strip() for _ in range(n)])

    cnt = 0

    for _ in range(m):
        if read().strip() in s:
            cnt += 1

    print(cnt)
