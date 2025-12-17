from heapq import heapify_max, heappush_max, heappop_max


class Coordinate:
    def __init__(self, x, y, corner_type):
        self.x = x
        self.y = y
        self.corner_type = corner_type  # F, J, L, 7

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Coordinate({self.x}, {self.y}, {self.corner_type})"


class Rectangle:
    def __init__(self, diagonal_1, diagonal_2):
        self.diagonal_1 = diagonal_1
        self.diagonal_2 = diagonal_2
        self.area = calculate_area(diagonal_1, diagonal_2)

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Rectangle({self.diagonal_1}, {self.diagonal_2}, {self.area})"


def calculate_area(coord1, coord2):
    return (abs(coord1.x - coord2.x) + 1) * (abs(coord1.y - coord2.y) + 1)


def load_coordinates(filename):
    coordinates = []
    with open(filename, "r") as file:
        for line in file:
            x, y = line.strip().split(",")
            coordinates.append(Coordinate(int(x), int(y), None))
    return coordinates


def get_sorted_rectangles(coordinates):
    heap = []
    heapify_max(heap)
    for index_from, from_coordinate in enumerate(coordinates):
        for to_coordinate in coordinates[index_from + 1:]:
            heappush_max(heap, Rectangle(from_coordinate, to_coordinate))
    return heap


def organise_coordinates(coordinates):
    x_sorted_coordinates = {}
    y_sorted_coordinates = {}

    for coordinate in coordinates:
        if coordinate.x in x_sorted_coordinates:
            x_sorted_coordinates[coordinate.x].append(coordinate)
        else:
            x_sorted_coordinates[coordinate.x] = [coordinate]

        if coordinate.y in y_sorted_coordinates:
            y_sorted_coordinates[coordinate.y].append(coordinate)
        else:
            y_sorted_coordinates[coordinate.y] = [coordinate]

    for y_coordinates in x_sorted_coordinates.values():
        y_coordinates.sort(key=lambda c: c.y)

    for x_coordinates in y_sorted_coordinates.values():
        x_coordinates.sort(key=lambda c: c.x)

    return x_sorted_coordinates, y_sorted_coordinates


def largest_index_less_than(coords, predicate):
    for i, coord in enumerate(coords):
        if predicate(coord):
            return i
    return -1


def get_next_coordinate(x_sorted_coordinates, y_sorted_coordinates, current_coordinate, previous_direction):
    is_horizontal = previous_direction == "UP" or previous_direction == "DOWN"

    coordinates = []

    if is_horizontal:
        x_index = largest_index_less_than(y_sorted_coordinates[current_coordinate.y],
                                          lambda c: c.x == current_coordinate.x)
        horizontal_direction = "RIGHT" if x_index % 2 == 0 else "LEFT"
        next_coordinate = y_sorted_coordinates[current_coordinate.y][
            x_index + 1 if horizontal_direction == "RIGHT" else x_index - 1]

        vertical_direction = previous_direction
        next_direction = horizontal_direction
        if vertical_direction == "UP":
            if horizontal_direction == "RIGHT":
                coordinate_direction = "F"
            else:
                coordinate_direction = "7"
        else:
            if horizontal_direction == "RIGHT":
                coordinate_direction = "L"
            else:
                coordinate_direction = "J"
        counter = current_coordinate.x
        while abs(next_coordinate.x - counter) > 1:
            counter += 1 if horizontal_direction == "RIGHT" else -1
            coordinates.append(Coordinate(counter, current_coordinate.y, "-"))
    else:
        y_index = largest_index_less_than(x_sorted_coordinates[current_coordinate.x],
                                          lambda c: c.y == current_coordinate.y)
        vertical_direction = "DOWN" if y_index % 2 == 0 else "UP"
        next_coordinate = x_sorted_coordinates[current_coordinate.x][
            y_index + 1 if vertical_direction == "DOWN" else y_index - 1]
        horizontal_direction = previous_direction
        next_direction = vertical_direction
        if vertical_direction == "UP":
            if horizontal_direction == "RIGHT":
                coordinate_direction = "J"
            else:
                coordinate_direction = "L"
        else:
            if horizontal_direction == "RIGHT":
                coordinate_direction = "7"
            else:
                coordinate_direction = "F"

    current_coordinate.corner_type = coordinate_direction
    coordinates.append(next_coordinate)
    return coordinates, next_direction


def get_border_coordinates(x_sorted_coordinates, y_sorted_coordinates):
    sorted_y = sorted(y_sorted_coordinates.keys())
    current_coordinate = first_coordinate = y_sorted_coordinates[sorted_y[0]][0]
    first_coordinate.corner_type = "F"
    current_direction = "UP"

    border_coordinates = [current_coordinate]

    while True:
        current_coordinates, current_direction = get_next_coordinate(x_sorted_coordinates, y_sorted_coordinates,
                                                                     current_coordinate, current_direction)
        for current_coordinate in current_coordinates:
            if current_coordinate.x == first_coordinate.x and current_coordinate.y == first_coordinate.y:
                return border_coordinates
            border_coordinates.append(current_coordinate)


def is_coordinate_inside(y, border_coordinates_array):
    counter = 0
    last_direction = None

    for border_coordinate in border_coordinates_array:
        if y == border_coordinate.y:
            return True

        if border_coordinate.y > y:
            break

        if border_coordinate.corner_type == "-":
            counter += 1
        elif last_direction is None:
            last_direction = border_coordinate.corner_type
        elif (last_direction == "F" and border_coordinate.corner_type == "J"
              or last_direction == "7" and border_coordinate.corner_type == "L"):
            counter += 1
            last_direction = None
        elif (last_direction == "F" and border_coordinate.corner_type == "L"
              or last_direction == "7" and border_coordinate.corner_type == "J"):
            last_direction = None

    return counter % 2 == 1 or last_direction == "F" or last_direction == "7"


def check_rectangle(rectangle, border_coordinates_x):
    start_coordinate = rectangle.diagonal_1
    end_coordinate = rectangle.diagonal_2
    # vertical checks first
    counter = abs(start_coordinate.y - end_coordinate.y)
    while counter > 0:
        multiplier = 1 if end_coordinate.y > start_coordinate.y else -1
        if not is_coordinate_inside(start_coordinate.y + counter * multiplier,
                                    border_coordinates_x[start_coordinate.x]):
            return False
        if not is_coordinate_inside(end_coordinate.y - counter * multiplier, border_coordinates_x[end_coordinate.x]):
            return False
        counter -= 1

    # horizontal next
    counter = abs(start_coordinate.x - end_coordinate.x)
    while counter > 0:
        multiplier = 1 if end_coordinate.x > start_coordinate.x else -1
        if not is_coordinate_inside(start_coordinate.y,
                                    border_coordinates_x[start_coordinate.x + counter * multiplier]):
            return False
        if not is_coordinate_inside(end_coordinate.y, border_coordinates_x[end_coordinate.x - counter * multiplier]):
            return False
        counter -= 1
    return True


def main():
    nodes = load_coordinates("input.txt")
    x_sorted, y_sorted = organise_coordinates(nodes)
    border_coordinates_x, _ = organise_coordinates(get_border_coordinates(x_sorted, y_sorted))

    sorted_rectangles = get_sorted_rectangles(nodes)
    counter = 0
    while len(sorted_rectangles) > 0:
        max_rectangle = heappop_max(sorted_rectangles)
        if counter == 0:
            print(max_rectangle.area)

        if check_rectangle(max_rectangle, border_coordinates_x):
            print(max_rectangle)
            return
        counter += 1


if __name__ == "__main__":
    main()
