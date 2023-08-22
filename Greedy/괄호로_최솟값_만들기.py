# https://www.acmicpc.net/problem/1541

formula = input().split('-')
total = 0

for i in range(0, len(formula)):
    if i==0:
        total += sum(map(int, formula[i].split('+')))
    else:
        total -= sum(map(int, formula[i].split('+')))

print(total)
