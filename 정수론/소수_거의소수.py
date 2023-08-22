# https://www.acmicpc.net/problem/1456

a, b = map(int, input().split())
end = int(b ** 0.5)
checks = [False, False] + [True] * (end - 1)

for i in range(2, end + 1): # int(b ** 0.5)까지만 돌려도 됨 -> 어차피 제곱했을 때 b를 넘을 수 없기 때문
    if checks[i]:
        for j in range(i * 2, end + 1, i): # int(b ** 0.5)까지만 돌려도 됨 -> 어차피 제곱했을 때 b를 넘을 수 없기 때문
            checks[j] = False

count = 0

for i in range(2, end + 1):
    if checks[i]:
        target = i ** 2
        while target <= b:
            if target >= a:
                count += 1
            target *= i

print(count)
