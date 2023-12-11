points = []
points_x = set()
points_y = set()


def count_empty_space(coord_comp_a, coord_comp_b, point_set, expansion):
    empty_space = 0
    i = min(coord_comp_a, coord_comp_b)
    while i < max(coord_comp_a, coord_comp_b):
        if i not in point_set:
            empty_space += expansion - 1
        i += 1
    return empty_space


def get_distance(coordinate_a, coordinate_b, expansion):
    a_x = coordinate_a[0]
    a_y = coordinate_a[1]
    b_x = coordinate_b[0]
    b_y = coordinate_b[1]

    empty_space = count_empty_space(a_x, b_x, points_x, expansion)
    empty_space += count_empty_space(a_y, b_y, points_y, expansion)

    return abs(a_x - b_x) + abs(a_y - b_y) + empty_space


with open("input.txt", "r") as file:
    for line_index, line in enumerate(file):
        has_point = False
        for char_index, character in enumerate(line):
            if character == "#":
                points.append((char_index, line_index))
                points_x.add(char_index)
                points_y.add(line_index)


def get_all_distance(expansion):
    counter = 0
    distance = 0
    while counter < len(points):
        current_coordinate = points[counter]
        counter2 = counter + 1
        while counter2 < len(points):
            other_coordinate = points[counter2]
            distance += get_distance(current_coordinate, other_coordinate, expansion)
            counter2 += 1
        counter += 1
    return distance


print(get_all_distance(2))
print(get_all_distance(1_000_000))
