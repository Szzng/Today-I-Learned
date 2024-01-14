# https://school.programmers.co.kr/learn/courses/30/lessons/49994?language=python3


def solution(dirs):
    x, y = 0, 0
    answers = set()  # 중복 방지 -> set 사용

    for direction in dirs:
        nx, ny = move(x, y, direction)

        if not is_valid_move(nx, ny):
            continue

        # (x, y) -> (nx, ny)로 이동하는 경로와 (nx, ny) -> (x, y)로 이동하는 경로는 같으므로 둘 다 추가
        answers.add((x, y, nx, ny))
        answers.add((nx, ny, x, y))

        x, y = nx, ny

    return len(answers) // 2


def move(x, y, direction):
    if direction == 'U':
        nx, ny = x, y + 1
    elif direction == 'D':
        nx, ny = x, y - 1
    elif direction == 'R':
        nx, ny = x + 1, y
    else:
        nx, ny = x - 1, y

    return nx, ny


def is_valid_move(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5
