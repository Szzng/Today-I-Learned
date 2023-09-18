# https://www.acmicpc.net/problem/2775


def dp_solution():
    max_num = 14
    d = [[0] * (max_num + 1) for _ in range(max_num + 1)]
    d[0] = [i for i in range(max_num + 1)]  # 0층의 i호에는 i명이 산다.

    for a in range(1, max_num + 1):  # 1층부터
        for b in range(1, max_num + 1):  # 1호부터
            d[a][b] = d[a][b - 1] + d[a - 1][b]  # a층의 b호에는 a층의 b-1호 + a-1층의 b호만큼 사람이 산다.

    t = int(input())

    for _ in range(t):
        k = int(input())  # 층
        n = int(input())  # 호
        print(d[k][n])


def sum_solution():
    for _ in range(int(input())):
        k = int(input())  # 층
        n = int(input())  # 호

        d = [[1] for _ in range(k)]  # 0층부터 k층까지, 1호는 무조건 1명이 산다.
        d[0] = list(range(1, n + 1))  # 0층의 i호에는 i명이 산다.

        for a in range(1, k):  # 1층부터 -> 0층은 이미 구해놨으니까
            for b in range(1, n):  # 2호(1)부터 -> 1호는 이미 구해놨으니까
                d[a].append(sum(d[a - 1][:b + 1]))
        print(sum(d[k - 1]))
