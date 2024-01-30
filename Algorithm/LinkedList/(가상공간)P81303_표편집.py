# https://school.programmers.co.kr/learn/courses/30/lessons/81303?language=python3

"""
# 경계 조건(맨 위, 맨 아래)을 처리 간소화를 위해 가상공간 추가 (조건문 없이도 처리 가능)
# 실제 데이터의 0번째 데이터는 prev가 없고, n-1번째 데이터는 next가 없는데 이런 경계값 처리를 조건문으로 따로 고려하지 않기 위해서 가상공간(일종의 더미 데이터)을 추가한다고 이해했음.

1. 가상공간을 사용하기 위해 실제 데이터의 인덱스에 모두 +1 : 0~n-1 -> 1~n
2. 가상공간을 사용하기 위해 실제 데이터의 시작점 이전과 끝점 다음에 가상의 요소를 추가

## up 리스트 (길이: n+2):
    - up[0]: 가상의 시작 요소. 이 요소는 실제 데이터의 시작점 이전을 나타냄. 링크드 리스트의 첫 번째 요소를 삭제할 때, 첫 번째 요소가 되도록 해주는 역할.
    - up[1]부터 up[n]: 실제 데이터 요소들. 각각의 요소는 이전 요소를 가리키는 인덱스를 저장합니다.
    - up[n+1]: 가상의 끝 요소. 이 요소는 실제 데이터의 마지막 요소 다음을 나타냅니다. 이것은 리스트의 마지막 요소를 삭제하면 up[n+1]을 참조하여 리스트의 끝을 처리할 수 있도록 해줌.

## down 리스트 (길이: n+1):
    - down[0]: 가상의 시작 요소. 이 요소는 실제 데이터의 시작점 이전을 나타냅니다.
    - down[1]부터 down[n]: 실제 데이터 요소들. 각각의 요소는 다음 요소를 가리키는 인덱스를 저장합니다.
"""


def solution(n, k, cmd):
    deleted = []

    # 링크드 리스트에서 각 행 위아래의 행의 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n + 2)]  # up[n + 1]은 가상의 끝 요소
    down = [i + 1 for i in range(n + 1)]  # down[0]은 가상의 시작 요소

    # 현재 위치를 나타내는 인덱스: 가상공간 때문에 +1
    k += 1

    for c in cmd:
        if c.startswith("C"):
            deleted.append(k)

            up[down[k]] = up[k]
            down[up[k]] = down[k]

            k = up[k] if n < down[k] else down[k]

        elif c.startswith("Z"):
            restore = deleted.pop()

            down[up[restore]] = restore
            up[down[restore]] = restore

        else:
            action, num = c.split()
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]

    result = ["O"] * n
    for i in deleted:
        result[i - 1] = "X"
    return "".join(result)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
