# https://www.acmicpc.net/problem/1068

"""
# 문제
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.
트리가 주어졌을 때, 노드 하나를 지울 것이다.
그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오.
노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

# 입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다.
만약 부모가 없다면 (루트) -1이 주어진다.
셋째 줄에는 지울 노드의 번호가 주어진다.

# 출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

# 시간제한: 2초
# 시간복잡도: O(N)
"""
import sys

sys.setrecursionlimit(10 ** 6)


def read_tree(num_nodes):
    parents = list(map(int, sys.stdin.readline().split()))
    tree = [[] for _ in range(num_nodes)]
    root = None

    for idx, parent in enumerate(parents):
        if parent == -1:
            root = idx
        else:
            tree[parent].append(idx)

    return tree, root


def count_leaf_nodes1(tree, delete_node, curr_node):
    # curr_node가 삭제될 노드인 경우
    if curr_node == delete_node:
        return 0

    # curr_node가 리프노드인 경우
    if not tree[curr_node] or all(child == delete_node for child in tree[curr_node]):
        return 1

    # curr_node가 리프노드가 아닌 경우
    return sum(count_leaf_nodes1(tree, delete_node, child) for child in tree[curr_node])


def count_leaf_nodes2(tree, delete_node, curr_node):
    # curr_node가 삭제될 노드인 경우
    if curr_node == delete_node:
        return 0

    leaf_cnt = 0
    for child in tree[curr_node]:
        if child != delete_node:
            leaf_cnt += count_leaf_nodes2(tree, delete_node, child)

    return leaf_cnt if leaf_cnt else 1


nums_nodes = int(input())
tree, root = read_tree(nums_nodes)
delete_node = int(input())

print(count_leaf_nodes1(tree, delete_node, root))
print(count_leaf_nodes2(tree, delete_node, root))
