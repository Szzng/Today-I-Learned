# https://www.acmicpc.net/problem/13251


color_num = int(input())
colors = list(map(int, input().split()))
total = sum(colors)
pick = int(input())

prob = 0

for color in colors:
    if color < pick:
        continue

    # color 중 pick개를 뽑을 확률
    temp = 1
    for i in range(pick):
        temp *= (color - i) / (total - i)
    prob += temp

print(prob)
