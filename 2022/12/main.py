import math
from collections import deque


class Node:
    def __init__(self, value, row, col):
        self.distance = math.inf
        self.value = value
        self.row_index = row
        self.col_index = col


def get_neighbours(map_matrix, current_node):
    neighbours = []
    if current_node.row_index > 0:
        neighbours.append(map_matrix[current_node.row_index - 1][current_node.col_index])
    if current_node.col_index > 0:
        neighbours.append(map_matrix[current_node.row_index][current_node.col_index - 1])
    if current_node.row_index < len(map_matrix) - 1:
        neighbours.append(map_matrix[current_node.row_index + 1][current_node.col_index])
    if current_node.col_index < len(map_matrix[0]) - 1:
        neighbours.append(map_matrix[current_node.row_index][current_node.col_index + 1])
    return neighbours


def update_neighbours(map_matrix, current_node, can_step_fn):
    neighbours = get_neighbours(map_matrix, current_node)
    next_neighbours = []
    for neighbour in neighbours:
        if can_step_fn(current_node, neighbour) and neighbour.distance > (current_node.distance + 1):
            neighbour.distance = current_node.distance + 1
            next_neighbours.append(neighbour)
    return next_neighbours


def get_shortest_path(map_matrix, first_node, is_end_node_fn, can_step_fn):
    first_node.distance = 0
    nodes = deque()
    nodes.append(first_node)
    while len(nodes) > 0:
        current_node = nodes.popleft()
        if is_end_node_fn(current_node):
            return current_node.distance
        for neighbour in update_neighbours(map_matrix, current_node, can_step_fn):
            nodes.append(neighbour)


matrix = []
start_node = None
end_node = None

for row_index, data in enumerate(open("input.txt", "r")):
    line = data.strip()
    matrix_line = []
    matrix.append(matrix_line)
    for col_index, character in enumerate(line):
        node = Node(character, row_index, col_index)
        matrix_line.append(node)
        if character == 'S':
            node.value = 'a'
            start_node = node
        elif character == 'E':
            node.value = 'z'
            end_node = node


# print(get_shortest_path(matrix, start_node, lambda x: x == end_node, lambda c, n: ord(c.value) + 1 >= ord(n.value)))
print(get_shortest_path(matrix, end_node, lambda x: x.value == 'a', lambda c, n: ord(c.value) - 1 <= ord(n.value)))
