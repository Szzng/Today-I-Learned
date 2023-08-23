# https://www.acmicpc.net/problem/1016

"""
제곱 ㄴㄴ 수 : 어떤 수 x가 1보다 큰 제곱 수로 나누어 떨어지지 않는 수
"""

a, b = map(int, input().split())
checks = [False] * (b - a + 1)  # 범위를 0부터 b까지 잡으면 메모리 초과 발생

for i in range(2, int(b ** 0.5) + 1):
    num = i * i

    # checks 범위를 지정해 놓아서, index 0을 a라고 가정해야 함
    # start_idx 구하는 것 여러 번 틀렸음
    if a % num:
        start_idx = num - a % num
    else:
        start_idx = 0

    for j in range(start_idx, len(checks), num):
        checks[j] = True

count = 0

for i in range(len(checks)):
    if not checks[i]:
        count += 1

print(count)