def init_rock_map():
    rock_map = []
    with open("input.txt", "r") as file:
        for line in file:
            rock_map_line = []
            for line_char in line.strip():
                rock_map_line.append(line_char)
            rock_map.append(rock_map_line)
    return rock_map


def find_sections(line):
    current_start = 0
    sections = []
    while current_start < len(line):
        counter = current_start
        section_end_offset = -1
        while counter < len(line):
            if line[counter] == "#":
                section_end_offset = counter
                break
            counter += 1
        section_end = len(line) if section_end_offset == -1 else section_end_offset
        sections.append((current_start, section_end))
        current_start = section_end + 1
    return sections


def move_north():
    for rock_map_column_index in range(len(rock_map[0])):
        current_line = get_vertical_line(rock_map_column_index)
        for section in vertical_sections[rock_map_column_index]:
            pointer_free = section[0]
            pointer_counter = section[0]
            while pointer_counter < section[1]:
                if current_line[pointer_counter] == "O":
                    rock_map[pointer_free][rock_map_column_index] = "O"
                    if pointer_counter != pointer_free:
                        rock_map[pointer_counter][rock_map_column_index] = "."
                    pointer_free += 1
                pointer_counter += 1


def move_south():
    for rock_map_column_index in range(len(rock_map[0])):
        current_line = get_vertical_line(rock_map_column_index)
        for section in vertical_sections[rock_map_column_index]:
            pointer_free = section[1] - 1
            pointer_counter = section[1] - 1
            while pointer_counter >= section[0]:
                if current_line[pointer_counter] == "O":
                    rock_map[pointer_free][rock_map_column_index] = "O"
                    if pointer_counter != pointer_free:
                        rock_map[pointer_counter][rock_map_column_index] = "."
                    pointer_free -= 1
                pointer_counter -= 1


def move_west():
    for rock_map_row_index, current_line in enumerate(rock_map):
        for section in horizontal_sections[rock_map_row_index]:
            pointer_free = section[0]
            pointer_counter = section[0]
            while pointer_counter < section[1]:
                if current_line[pointer_counter] == "O":
                    rock_map[rock_map_row_index][pointer_free] = "O"
                    if pointer_counter != pointer_free:
                        rock_map[rock_map_row_index][pointer_counter] = "."
                    pointer_free += 1
                pointer_counter += 1


def move_east():
    for rock_map_row_index, current_line in enumerate(rock_map):
        for section in horizontal_sections[rock_map_row_index]:
            pointer_free = section[1] - 1
            pointer_counter = section[1] - 1
            while pointer_counter >= section[0]:
                if current_line[pointer_counter] == "O":
                    rock_map[rock_map_row_index][pointer_free] = "O"
                    if pointer_counter != pointer_free:
                        rock_map[rock_map_row_index][pointer_counter] = "."
                    pointer_free -= 1
                pointer_counter -= 1


def get_weight(rock_map):
    result = 0
    for rock_map_line_index, rock_map_line in enumerate(rock_map):
        result += rock_map_line.count("O") * (len(rock_map) - rock_map_line_index)
    return result


def get_vertical_line(column_index):
    ln = []
    for rock_map_line in rock_map:
        ln.append(rock_map_line[column_index])
    return ln


def get_vertical_sections():
    vertical_sections = {}
    for rock_map_column_index in range(len(rock_map[0])):
        vertical_sections[rock_map_column_index] = find_sections(get_vertical_line(rock_map_column_index))
    return vertical_sections


def get_horizontal_sections():
    horizontal_sections = {}
    for rock_map_line_index, rock_map_line in enumerate(rock_map):
        horizontal_sections[rock_map_line_index] = find_sections(rock_map_line)
    return horizontal_sections


def construct_history():
    history_item = ""
    for rock_map_line_index, rock_map_line in enumerate(rock_map):
        for rock_map_char_index, rock_map_char in enumerate(rock_map_line):
            if rock_map_char == "O":
                history_item += str(rock_map_line_index) + "-" + str(rock_map_char_index) + "."
    return history_item.__hash__()


def move_cycles(max_cycles):
    cntr = 0
    history = {}
    weights = []
    while cntr < max_cycles:
        move_north()
        move_west()
        move_south()
        move_east()
        current_history = construct_history()
        if current_history in history:
            history_item_index = history.get(current_history)
            return history_item_index, cntr - history_item_index, weights
        history[current_history] = cntr
        weights.append(get_weight(rock_map))
        cntr += 1
    return -1, cntr, weights


rock_map = init_rock_map()
vertical_sections = get_vertical_sections()
horizontal_sections = get_horizontal_sections()
move_north()
print("Task 1", get_weight(rock_map))
match_index, diff, weight_history = move_cycles(1_000_000_000)
print("Task 2", weight_history[match_index + (999_999_999 - match_index) % diff])
