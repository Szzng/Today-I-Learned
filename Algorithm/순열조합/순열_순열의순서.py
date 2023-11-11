# https://www.acmicpc.net/problem/1722

n = int(input())
query = list(map(int, input().split()))

factorial = 1
for i in range(1, n):
    factorial *= i

cases = [0] * (n - 1)
for i in range(n - 1):
    cases[i] = factorial
    factorial //= (n - 1 - i)

left_nums = [i for i in range(1, n + 1)]

if query.pop(0) == 1:
    k = query[0]

    result = []

    for i in range(n - 1):
        if k <= cases[i]:
            result.append(left_nums.pop(0))
        else:
            cnt = 0
            while k > cases[i]:
                k -= cases[i]
                cnt += 1
            result.append(left_nums.pop(cnt))

    print(*(result + left_nums))

else:
    k = 1

    for i, num in enumerate(query):
        idx = left_nums.index(num)
        left_nums.pop(idx)

        if idx != 0:
            k += cases[i] * idx

    print(k)
