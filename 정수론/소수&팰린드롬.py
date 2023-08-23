# https://www.acmicpc.net/problem/1747


def is_palindrome(num):
    num = list(str(num))
    s = 0
    e = len(num) - 1

    while s < e:
        if num[s] != num[e]:
            return False
        s += 1
        e -= 1
    return True


n = int(input())
max_end = 1000000 * 10  # 1000000보다 큰 소수 중 가장 작은 팰린드롬 수는 1003001
checks = [False, False] + [True] * (max_end - 1)

for i in range(2, int(max_end ** 0.5) + 1):
    if checks[i]:
        for j in range(i * 2, max_end + 1, i):
            checks[j] = False

for i in range(n, max_end + 1):
    if checks[i] and is_palindrome(i):
        print(i)
        break
