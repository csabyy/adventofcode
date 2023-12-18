import sys
from collections import deque


class Vertex:
    def __init__(self, x, y, weight):
        self.vertical_distance = sys.maxsize
        self.horizontal_distance = sys.maxsize
        self.weight = weight
        self.x = x
        self.y = y


def get_vertical_neighbours(heat_map, vertex, min_steps, max_steps):
    neighbours = []
    down_weight = vertex.horizontal_distance
    up_weight = vertex.horizontal_distance
    for offset in range(1, max_steps + 1):
        if vertex.y + offset < len(heat_map):
            current_vertex = heat_map[vertex.y + offset][vertex.x]
            down_weight += current_vertex.weight
            if min_steps <= offset and current_vertex.vertical_distance > down_weight:
                current_vertex.vertical_distance = down_weight
                neighbours.append((False, current_vertex))
        if vertex.y - offset > -1:
            current_vertex = heat_map[vertex.y - offset][vertex.x]
            up_weight += current_vertex.weight
            if min_steps <= offset and current_vertex.vertical_distance > up_weight:
                current_vertex.vertical_distance = up_weight
                neighbours.append((False, current_vertex))
    return neighbours


def get_horizontal_neighbours(heat_map, vertex, min_steps, max_steps):
    neighbours = []
    right_weight = vertex.vertical_distance
    left_weight = vertex.vertical_distance
    for offset in range(1, max_steps + 1):
        if vertex.x + offset < len(heat_map[0]):
            current_vertex = heat_map[vertex.y][vertex.x + offset]
            right_weight += current_vertex.weight
            if min_steps <= offset and current_vertex.horizontal_distance > right_weight:
                current_vertex.horizontal_distance = right_weight
                neighbours.append((True, current_vertex))
        if vertex.x - offset > -1:
            current_vertex = heat_map[vertex.y][vertex.x - offset]
            left_weight += current_vertex.weight
            if min_steps <= offset and current_vertex.horizontal_distance > left_weight:
                current_vertex.horizontal_distance = left_weight
                neighbours.append((True, current_vertex))
    return neighbours


def traverse_map(heat_map, initial_directions, min_steps, max_steps):
    while len(initial_directions) != 0:
        queue_item = initial_directions.popleft()
        current_is_horizontal = queue_item[0]
        current_vertex = queue_item[1]

        if current_is_horizontal:
            for v_neighbours in get_vertical_neighbours(heat_map, current_vertex, min_steps, max_steps):
                initial_directions.append(v_neighbours)
        else:
            for h_neighbours in get_horizontal_neighbours(heat_map, current_vertex, min_steps, max_steps):
                initial_directions.append(h_neighbours)


def initialise_heat_map():
    heat_map = []
    with open("input.txt", "r") as file:
        for line_index, line in enumerate(file):
            heat_map_line = []
            for line_char_index, line_char in enumerate(line.strip()):
                heat_map_line.append(Vertex(line_char_index, line_index, int(line_char)))
            heat_map.append(heat_map_line)
    return heat_map


def start_traversal(min_steps, max_steps):
    heat_map = initialise_heat_map()
    initial_items = deque()
    initial_node = heat_map[0][0]
    initial_node.horizontal_distance = 0
    initial_node.vertical_distance = 0
    for horizontal_neighbours in get_horizontal_neighbours(heat_map, initial_node, min_steps, max_steps):
        initial_items.append(horizontal_neighbours)
    for vertical_neighbours in get_vertical_neighbours(heat_map, initial_node, min_steps, max_steps):
        initial_items.append(vertical_neighbours)
    traverse_map(heat_map, initial_items, min_steps, max_steps)

    last_item = heat_map[len(heat_map) - 1][len(heat_map[0]) - 1]
    return min(last_item.horizontal_distance, last_item.vertical_distance)


print("Task 1", start_traversal(1, 3))
print("Task 2", start_traversal(4, 10))
