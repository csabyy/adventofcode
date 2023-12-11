def move(current_position, instruction, previous_position):
    vertical_index = current_position[0]
    horizontal_index = current_position[1]
    previous_vertical_index = previous_position[0]
    previous_horizontal_index = previous_position[1]
    if instruction == "|":
        vertical_index += 1 if previous_vertical_index < vertical_index else -1
    elif instruction == "-":
        horizontal_index += 1 if previous_horizontal_index < horizontal_index else -1
    else:
        if previous_horizontal_index != horizontal_index:
            if instruction == "L" or instruction == "J":
                vertical_index -= 1
            if instruction == "7" or instruction == "F":
                vertical_index += 1
        else:
            if instruction == "L" or instruction == "F":
                horizontal_index += 1
            if instruction == "J" or instruction == "7":
                horizontal_index -= 1
    return vertical_index, horizontal_index


def get_possible_moves(matrix, start_position):
    current_vertical = start_position[0]
    current_horizontal = start_position[1]
    possible_coordinates = []
    if current_vertical - 1 > -1:
        instruction = matrix[current_vertical - 1][current_horizontal]
        if instruction == "|" or instruction == "F" or instruction == "7":
            possible_coordinates.append((current_vertical - 1, current_horizontal))
    if current_vertical + 1 < len(matrix):
        instruction = matrix[current_vertical + 1][current_horizontal]
        if instruction == "|" or instruction == "L" or instruction == "J":
            possible_coordinates.append((current_vertical + 1, current_horizontal))
    if current_horizontal + 1 < len(matrix[0]):
        instruction = matrix[current_vertical][current_horizontal + 1]
        if instruction == "-" or instruction == "J" or instruction == "7":
            possible_coordinates.append((current_vertical, current_horizontal + 1))
    if current_horizontal - 1 > -1:
        instruction = matrix[current_vertical][current_horizontal - 1]
        if instruction == "-" or instruction == "F" or instruction == "L":
            possible_coordinates.append((current_vertical, current_horizontal - 1))
    return possible_coordinates


def map_starting_pos(start, possible_a, possible_b):
    start_vertical = start[0]
    start_horizontal = start[1]
    possible_a_vertical = possible_a[0]
    possible_a_horizontal = possible_a[1]
    possible_b_vertical = possible_b[0]
    possible_b_horizontal = possible_b[1]
    if possible_a_vertical == possible_b_vertical:
        return "-"
    if possible_a_horizontal == possible_b_horizontal:
        return "|"
    if possible_a_vertical < start_vertical:
        if possible_b_horizontal < start_horizontal:
            return "J"
        return "L"
    else:
        if possible_b_horizontal < start_horizontal:
            return "7"
        return "F"


def update_visited_nodes(coordinates, visited_nodes):
    if coordinates[0] in visited_nodes:
        visited_nodes[coordinates[0]].add(coordinates[1])
    else:
        visited_nodes[coordinates[0]] = {coordinates[1]}


def traverse_nodes(first_node, visited_nodes):
    previous_node = staring_position
    current_node = first_node
    update_visited_nodes(current_node, visited_nodes)
    while current_node[0] != staring_position[0] or current_node[1] != staring_position[1]:
        temp = current_node
        current_node = move(current_node, map_lines[current_node[0]][current_node[1]], previous_node)
        previous_node = temp
        update_visited_nodes(current_node, visited_nodes)


map_lines = []
staring_position = 0, 0
with open("input.txt", "r") as file:
    for line_index, line in enumerate(file):
        start_index = line.find("S")
        if start_index > -1:
            staring_position = line_index, start_index
        map_lines.append(line.strip())

perimeter_nodes = {}
possible_moves = get_possible_moves(map_lines, staring_position)
update_visited_nodes(staring_position, perimeter_nodes)
traverse_nodes(possible_moves[0], perimeter_nodes)
total_steps = 0
for perimeter_node in perimeter_nodes.values():
    total_steps += len(perimeter_node)
print("First task: " + str(total_steps / 2))

result_counter = 0
for map_line_index, map_line in enumerate(map_lines):
    if map_line_index not in perimeter_nodes:
        continue
    visited_nodes_in_line = perimeter_nodes[map_line_index]
    is_inside = False
    special_char = ""
    for map_item_index, map_item in enumerate(map_line):
        if map_item_index in visited_nodes_in_line:
            if map_item == "S":
                map_item = map_starting_pos(staring_position, possible_moves[0], possible_moves[1])
            if map_item == "|" or special_char == "L" and map_item == "7" or special_char == "F" and map_item == "J":
                is_inside = not is_inside
            elif map_item == "L" or map_item == "F":
                special_char = map_item
        else:
            if is_inside:
                result_counter += 1

print("Second task" + str(result_counter))
