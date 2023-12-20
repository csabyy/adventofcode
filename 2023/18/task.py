def get_direction(direction_number):
    if direction_number == "0":
        return "R"
    if direction_number == "1":
        return "D"
    if direction_number == "2":
        return "L"
    return "U"


def get_steps(hex_string):
    return int(hex_string, 16)


instructions_task1 = []
instructions_task2 = []
with open("input.txt", "r") as file:
    for line in file:
        instruction_parts = line.strip().split(" ")
        instructions_task1.append([instruction_parts[0], int(instruction_parts[1])])
        colour_code = instruction_parts[2]
        instructions_task2.append([get_direction(colour_code[-2:-1]), get_steps(colour_code[2:-2])])


def add_to_dictionary(dictionary, key, value):
    if key in dictionary:
        dictionary[key].add(value)
    else:
        dictionary[key] = {value}


def get_visited_items(instructions):
    turns = {}
    current_y = 0
    current_x = 0
    for instruction in instructions:
        direction = instruction[0]
        steps = instruction[1]
        if direction == "R" or direction == "L":
            current_x += steps if direction == "R" else -steps
        else:
            current_y += steps if direction == "D" else -steps
        add_to_dictionary(turns, current_y, current_x)
    return turns


def merge_corner_rows(previous, current):
    if len(previous) == 0:
        return get_section_value(current), current
    if len(current) == 0:
        return get_section_value(previous), previous
    pointer_previous = 0
    pointer_current = 0
    sorted_list = []
    current_sections = []
    previous_junction_type = None # J F 7 L
    current_junction_type = None # J F 7 L
    is_inside = False

    while pointer_previous < len(previous) and pointer_current < len(current):
        if current[pointer_current] < previous[pointer_previous]:
            current_junction_type = "F" if pointer_current % 2 == 0 else "7"
            if current_junction_type == "F" and not is_inside:
                current_sections.append(current[pointer_current])
            elif current_junction_type == "7":
                if previous_junction_type == "F" and not is_inside:
                    current_sections.append(current[pointer_current])
                elif previous_junction_type == "L":
                    if is_inside:
                        current_sections.append(current[pointer_current])
                    is_inside = not is_inside
            sorted_list.append(current[pointer_current])
            pointer_current += 1
        elif current[pointer_current] > previous[pointer_previous]:
            sorted_list.append(previous[pointer_previous])
            current_sections.append(previous[pointer_previous])
            is_inside = not is_inside
            pointer_previous += 1
        else:
            current_junction_type = "L" if pointer_current % 2 == 0 else "J"
            if current_junction_type == "L" and not is_inside:
                current_sections.append(current[pointer_current])
            elif current_junction_type == "J":
                if previous_junction_type == "L" and not is_inside:
                    current_sections.append(current[pointer_current])
                elif previous_junction_type == "F":
                    if is_inside:
                        current_sections.append(current[pointer_current])
                    is_inside = not is_inside
            pointer_previous += 1
            pointer_current += 1
        previous_junction_type = current_junction_type

    while pointer_current < len(current):
        sorted_list.append(current[pointer_current])
        current_sections.append(current[pointer_current])
        pointer_current += 1
    while pointer_previous < len(previous):
        sorted_list.append(previous[pointer_previous])
        current_sections.append(previous[pointer_previous])
        pointer_previous += 1
    return get_section_value(current_sections), sorted_list


def get_section_value(sorted_corner_row):
    counter = 0
    section_value = 0

    while counter + 1 < len(sorted_corner_row):
        section_value += sorted_corner_row[counter + 1] - sorted_corner_row[counter] + 1
        counter += 2

    return section_value


def calculate_area(corners):
    sorted_corner_rows = sorted(corners.keys())
    previous_row_corners = []
    previous_y = 0
    result = 0
    for current_row_ix in sorted_corner_rows:
        sorted_x = sorted(corners[current_row_ix])
        if len(previous_row_corners) != 0:
            height = current_row_ix - previous_y - 1
            weight = get_section_value(previous_row_corners)
            result += height * weight
        current_value, previous_row_corners = merge_corner_rows(previous_row_corners, sorted_x)
        result += current_value
        previous_y = current_row_ix
    return result


print(calculate_area(get_visited_items(instructions_task1)))
print(calculate_area(get_visited_items(instructions_task2)))
