# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3


from collections import deque


# bridge 기준
def solution1(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    weight_on_bridge = 0

    while bridge:
        time += 1
        weight_on_bridge -= bridge.popleft()

        if not truck_weights:
            continue

        if weight_on_bridge + truck_weights[0] <= weight and len(bridge) < bridge_length:
            truck = truck_weights.popleft()
            bridge.append(truck)
            weight_on_bridge += truck
        else:
            bridge.append(0)

    return time


# truck_weights 기준 : 마지막 트럭이 다리를 건너는 시간인 bridge_length를 더해주는 아이디어
def solution2(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    weight_on_bridge = 0

    while truck_weights:
        time += 1
        weight_on_bridge -= bridge.popleft()

        if weight_on_bridge + truck_weights[0] <= weight and len(bridge) < bridge_length:
            truck = truck_weights.popleft()
            bridge.append(truck)
            weight_on_bridge += truck
        else:
            bridge.append(0)

    time += bridge_length  # 마지막 트럭이 다리를 건너는 시간

    return time


print(solution1(2, 10, [7, 4, 5, 6]) == 8)
print(solution2(100, 100, [10]) == 101)
print(solution1(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110)
