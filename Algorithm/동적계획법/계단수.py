# https://www.acmicpc.net/problem/10844

n = int(input())  # 1 <= n <= 100, 자리수
mod = 1000000000  # 1000000000으로 나눈 나머지 출력


def solution1():
    # 초기화
    d = [[0] * 10 for _ in range(n + 1)]  # d[i][j] : i자리 계단수 중 j로 끝나는 계단수의 개수
    d[1] = [0] + [1] * 9

    for i in range(2, n + 1):
        d[i][0] = d[i - 1][1]
        d[i][9] = d[i - 1][8]
        for j in range(1, 9):
            d[i][j] = (d[i - 1][j - 1] + d[i - 1][j + 1]) % mod

    print(sum(d[n]) % mod)


def solution2():
    before = [0] + [1] * 9  # 이전 계단수의 개수, n=1일 때 초기화
    after = [0] * 10  # 현재 계단수의 개수

    for _ in range(2, n + 1):
        after[0] = before[1] % mod
        after[9] = before[8] % mod

        for i in range(1, 9):
            after[i] = (before[i - 1] + before[i + 1]) % mod

        before = after[:]

    print(sum(before) % mod)  # before 대신 after를 하면 n=1일 때를 처리하지 못한다.
