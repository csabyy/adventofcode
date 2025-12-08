def read_input():
    map_matrix = []
    with open("input.txt", "r") as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(1 if char == "@" else 0)
            map_matrix.append(row)
    return map_matrix


def get_horizontal_neighbours(map_vector, column_index, is_middle):
    neighbours = 0 if is_middle else map_vector[column_index]
    if column_index == 0:
        neighbours += map_vector[column_index + 1]
    elif column_index == len(map_vector) - 1:
        neighbours += map_vector[column_index - 1]
    else:
        neighbours += map_vector[column_index - 1] + map_vector[column_index + 1]
    return neighbours


def process_matrix(map_matrix, only_once):
    result = 0
    new_map_matrix = []
    item_removed = False
    for row_index, row in enumerate(map_matrix):
        new_row = []
        for column_index, column in enumerate(row):
            if map_matrix[row_index][column_index] == 0:
                new_row.append(0)
                continue
            neighbours = 0
            if row_index > 0:
                neighbours += get_horizontal_neighbours(map_matrix[row_index - 1], column_index, False)
            neighbours += get_horizontal_neighbours(map_matrix[row_index], column_index, True)
            if row_index < len(map_matrix[0]) - 1:
                neighbours += get_horizontal_neighbours(map_matrix[row_index + 1], column_index, False)
            if neighbours < 4:
                new_row.append(0)
                result += 1
                item_removed = True
            else:
                new_row.append(1)
        new_map_matrix.append(new_row)
    if item_removed and not only_once:
        result += process_matrix(new_map_matrix, only_once)
    return result


print(process_matrix(read_input(), True))
print(process_matrix(read_input(), False))
