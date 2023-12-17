from enum import Enum
from collections import deque


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


mirror_map = []
with open("input.txt", "r") as file:
    for line in file:
        mirror_map.append(line.strip())


def add_to_map(map_to_update, key, value):
    if key in map_to_update:
        map_to_update[key].add(value)
    else:
        map_to_update[key] = {value}


def add_to_cache(cache, x, y, direction):
    if y in cache[direction]:
        if x in cache[direction][y]:
            return False
        cache[direction][y].add(x)
    else:
        cache[direction][y] = {x}
    return True


def get_new_directions(previous_direction, symbol):
    if symbol == ".":
        return [previous_direction]
    if symbol == "/":
        if previous_direction == Direction.RIGHT:
            return [Direction.UP]
        if previous_direction == Direction.LEFT:
            return [Direction.DOWN]
        if previous_direction == Direction.DOWN:
            return [Direction.LEFT]
        return [Direction.RIGHT]
    if symbol == "\\":
        if previous_direction == Direction.RIGHT:
            return [Direction.DOWN]
        if previous_direction == Direction.LEFT:
            return [Direction.UP]
        if previous_direction == Direction.DOWN:
            return [Direction.RIGHT]
        return [Direction.LEFT]
    if symbol == "|":
        if previous_direction == Direction.DOWN or previous_direction == Direction.UP:
            return [previous_direction]
        return [Direction.UP, Direction.DOWN]
    if symbol == "-":
        if previous_direction == Direction.RIGHT or previous_direction == Direction.LEFT:
            return [previous_direction]
        return [Direction.LEFT, Direction.RIGHT]


def get_new_coordinates(x, y, symbol, previous_direction):
    new_directions = get_new_directions(previous_direction, symbol)
    new_coordinates = []
    for new_direction in new_directions:
        if new_direction == Direction.RIGHT:
            new_coordinates.append((x + 1, y, new_direction))
        elif new_direction == Direction.UP:
            new_coordinates.append((x, y - 1, new_direction))
        elif new_direction == Direction.LEFT:
            new_coordinates.append((x - 1, y, new_direction))
        else:
            new_coordinates.append((x, y + 1, new_direction))
    return new_coordinates


def move_beam(x, y, direction, visited_map, cache):
    new_coordinates_list = deque([(x, y, direction)])
    while len(new_coordinates_list) > 0:
        current_x, current_y, current_dir = new_coordinates_list.popleft()
        if not (0 <= current_x < len(mirror_map[0]) and 0 <= current_y < len(mirror_map)):
            continue
        if not add_to_cache(cache, current_x, current_y, current_dir):
            continue
        add_to_map(visited_map, current_x, current_y)
        current_symbol = mirror_map[current_y][current_x]
        new_coordinates_list.extend(get_new_coordinates(current_x, current_y, current_symbol, current_dir))
    return visited_map


def get_result(start_x, start_y, direction):
    cache = {Direction.RIGHT: {}, Direction.LEFT: {}, Direction.DOWN: {}, Direction.UP: {}}
    visited_nodes = move_beam(start_x, start_y, direction, {}, cache)
    result = 0
    for visited_node in visited_nodes.values():
        result += len(visited_node)
    return result


def set_max(current_max, new_value):
    return new_value if new_value > current_max else current_max


print(get_result(0, 0, Direction.RIGHT))

max_result = 0
for start_y in range(len(mirror_map)):
    # 💡 Refactoring idea: use previous calculation's values stored in cache -- x, y, direction, possible steps left
    max_result = set_max(max_result, get_result(0, start_y, Direction.RIGHT))
    max_result = set_max(max_result, get_result(len(mirror_map[0]) - 1, start_y, Direction.LEFT))
for start_x in range(len(mirror_map[0])):
    max_result = set_max(max_result, get_result(start_x, 0, Direction.DOWN))
    max_result = set_max(max_result, get_result(start_x, len(mirror_map) - 1, Direction.UP))
print(max_result)
