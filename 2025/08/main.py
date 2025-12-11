import math
from heapq import heappop, heappush, heapify, heapreplace


class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))



class Connection:
    def __init__(self, from_coordinate, to_coordinate, distance):
        self.from_coordinate = from_coordinate
        self.to_coordinate = to_coordinate
        self.distance = distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self):
        return str(self.distance) + " (" + str(self.from_coordinate) + ") (" + str(self.to_coordinate) + ")"


def get_distance_matrix(coordinates):
    matrix = []
    heap = []
    heapify(heap)

    for (index_from, from_coordinate) in enumerate(coordinates):
        counter = 0
        row = []
        while counter < index_from:
            row.append(0)
            counter += 1
        for (index_to, to_coordinate) in enumerate(coordinates[index_from + 1:]):
            distance = math.sqrt(
                (from_coordinate.x - to_coordinate.x) ** 2 + (from_coordinate.y - to_coordinate.y) ** 2 + (
                        from_coordinate.z - to_coordinate.z) ** 2)
            heappush(heap, Connection(from_coordinate, to_coordinate, distance))
            row.append(distance)
        matrix.append(row)
    return matrix, heap


def process_input():
    with open("input.txt", "r") as file:
        coordinates = []
        for line in file:
            xyz = line.strip().split(",")
            coordinates.append(Coordinate(int(xyz[0]), int(xyz[1]), int(xyz[2])))
        return coordinates

def add_to_circuits(circuits, connection):
    for existing_circuit in circuits:
        # TODO: merge multiple circuits
        if connection.from_coordinate in existing_circuit and connection.to_coordinate in existing_circuit:
            return 0
        if connection.from_coordinate in existing_circuit:
            existing_circuit.add(connection.to_coordinate)
            return 1
        if connection.to_coordinate in existing_circuit:
            existing_circuit.add(connection.from_coordinate)
            return 1
    circuits.append({connection.from_coordinate, connection.to_coordinate})
    return 1


(distance_matrix, heap) = get_distance_matrix(process_input())
counter = 0
circuits = []

while counter < min(10, len(heap)):
    smallest_distance_connection = heappop(heap)
    counter += add_to_circuits(circuits, smallest_distance_connection)

heap2 = []
heapify(heap2)
for circuit in circuits:
    if len(heap2) < 3:
        heappush(heap2, len(circuit))
    elif len(circuit) > heap2[0]:
        heapreplace(heap2, len(circuit))

    for coord in circuit:
        print(coord)
    print("------")


print(heap2)
result = 1
while len(heap2) > 0:
    result *= heappop(heap2)
print(result)