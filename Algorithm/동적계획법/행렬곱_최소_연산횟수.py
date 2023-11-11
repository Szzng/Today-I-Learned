# https://www.acmicpc.net/problem/11049

import sys

n = int(input())
matrices = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]  # dp[i][j] : i번째 행렬부터 j번째 행렬까지 곱했을 때 최소값


def bottom_up():
    for cnt in range(1, n):  # 행렬의 개수
        for start in range(n - cnt):
            end = start + cnt

            dp[start][end] = sys.maxsize

            for mid in range(start, end):
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][mid] + dp[mid + 1][end] + matrices[start][0] * matrices[mid][1] * matrices[end][1]
                )

    print(dp[0][n - 1])


def top_down():
    def recur(start, end):
        if dp[start][end] != 0:  # 이미 계산한 경우
            return dp[start][end]

        # 행렬 1개를 곱하는 경우
        if start == end:
            return 0

        # 행렬 2개를 곱하는 경우
        elif start + 1 == end:
            dp[start][end] = matrices[start][0] * matrices[start][1] * matrices[end][1]

        # 행렬 3개 이상을 곱하는 경우 -> 재귀 호출
        else:
            dp[start][end] = sys.maxsize

            for mid in range(start, end):
                dp[start][end] = min(
                    dp[start][end],
                    recur(start, mid) + recur(mid + 1, end) + matrices[start][0] * matrices[mid][1] * matrices[end][1]
                )

        return dp[start][end]

    print(recur(0, n - 1))


bottom_up()
top_down()
