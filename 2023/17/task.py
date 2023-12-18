import sys
from collections import deque


class Vertex:
    def __init__(self, x, y, weight):
        self.vertical_distance = sys.maxsize
        self.horizontal_distance = sys.maxsize
        self.weight = weight
        self.x = x
        self.y = y


class Visit:
    def __init__(self, is_horizontal, vertex):
        self.is_horizontal = is_horizontal
        self.vertex = vertex


def get_vertical_neighbours(vertex):
    neighbours = []
    down_weight = vertex.horizontal_distance
    up_weight = vertex.horizontal_distance
    for offset in range(1, 4):
        if vertex.y + offset < len(heat_map):
            current_vertex = heat_map[vertex.y + offset][vertex.x]
            down_weight += current_vertex.weight
            if current_vertex.vertical_distance > down_weight:
                current_vertex.vertical_distance = down_weight
                neighbours.append(Visit(False, current_vertex))
        if vertex.y - offset > -1:
            current_vertex = heat_map[vertex.y - offset][vertex.x]
            up_weight += current_vertex.weight
            if current_vertex.vertical_distance > up_weight:
                current_vertex.vertical_distance = up_weight
                neighbours.append(Visit(False, current_vertex))
    return neighbours

def get_horizontal_neighbours(vertex):
    neighbours = []
    right_weight = vertex.vertical_distance
    left_weight = vertex.vertical_distance
    for offset in range(1, 4):
        if vertex.x + offset < len(heat_map[0]):
            current_vertex = heat_map[vertex.y][vertex.x + offset]
            right_weight += current_vertex.weight
            if current_vertex.horizontal_distance > right_weight:
                current_vertex.horizontal_distance = right_weight
                neighbours.append(Visit(True, current_vertex))
        if vertex.x - offset > -1:
            current_vertex = heat_map[vertex.y][vertex.x - offset]
            left_weight += current_vertex.weight
            if current_vertex.horizontal_distance > left_weight:
                current_vertex.horizontal_distance = left_weight
                neighbours.append(Visit(True, current_vertex))
    return neighbours

def traverse_map(initial_directions):
    while len(initial_directions) != 0:
        queue_item = initial_directions.popleft()
        current_vertex = queue_item.vertex

        if queue_item.is_horizontal:
            for v_neighbours in get_vertical_neighbours(current_vertex):
                initial_directions.append(v_neighbours)
        else:
            for h_neighbours in get_horizontal_neighbours(current_vertex):
                initial_directions.append(h_neighbours)

heat_map = []
with open("input.txt", "r") as file:
    for line_index, line in enumerate(file):
        heat_map_line = []
        for line_char_index, line_char in enumerate(line.strip()):
            heat_map_line.append(Vertex(line_char_index, line_index, int(line_char)))
        heat_map.append(heat_map_line)
initial_items = deque()
initial_node = heat_map[0][0]
initial_node.horizontal_distance = 0
initial_node.vertical_distance = 0
for horizontal_neighbours in get_horizontal_neighbours(initial_node):
    initial_items.append(horizontal_neighbours)
for vertical_neighbours in get_vertical_neighbours(initial_node):
    initial_items.append(vertical_neighbours)
traverse_map(initial_items)

last_item = heat_map[len(heat_map) - 1][len(heat_map[0]) - 1]
print("Result: " + str(min(last_item.horizontal_distance, last_item.vertical_distance)))
# for heat_map_line in heat_map:
#     buffer = ''
#     for vertex in heat_map_line:
#         buffer += str(min(vertex.horizontal_distance, vertex.vertical_distance)) + "\t\t"
#     print(buffer)