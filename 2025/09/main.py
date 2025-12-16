class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordinate({self.x}, {self.y})"

def calculate_area(coord1, coord2):
    return abs(coord1.x - coord2.x + 1) * abs(coord1.y - coord2.y + 1)


def load_coordinates(filename):
    coordinates = []
    with open(filename, "r") as file:
        for line in file:
            x, y = line.strip().split(",")
            coordinates.append(Coordinate(int(x), int(y)))
    return coordinates

def get_max_coordinates(coordinates):
    max_area = 0
    for index_from, from_coordinate in enumerate(coordinates):
        for to_coordinate in coordinates[index_from+1:]:
            area = calculate_area(from_coordinate, to_coordinate)
            if area > max_area:
                max_area = area
    return max_area



def orgnise_coordinates(coordinates):
    x_sorted_coordinates = {}
    y_sorted_coordinates = {}

    for coordinate in coordinates:
        if coordinate.x in x_sorted_coordinates:
            x_sorted_coordinates[coordinate.x].append(coordinate.y)
        else:
            x_sorted_coordinates[coordinate.x] = [coordinate.y]

        if coordinate.y in y_sorted_coordinates:
            y_sorted_coordinates[coordinate.y].append(coordinate.x)
        else:
            y_sorted_coordinates[coordinate.y] = [coordinate.x]

    for y_coordinates in x_sorted_coordinates.values():
        y_coordinates.sort()

    for x_coordinates in y_sorted_coordinates.values():
        x_coordinates.sort()

    print("---X------")
    for x, y_coordinates in x_sorted_coordinates.items():
        print(x, y_coordinates)

    print("---Y------")
    for y, x_coordinates in y_sorted_coordinates.items():
        print(y, x_coordinates)

    return x_sorted_coordinates, y_sorted_coordinates


def main():
    nodes = load_coordinates("input.txt")
    # x_sorted, y_sorted = orgnise_coordinates(nodes)

    max_coordinate = get_max_coordinates(nodes)
    print(max_coordinate)

if __name__ == "__main__":
    main()
