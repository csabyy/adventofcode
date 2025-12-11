import math
from heapq import heappop, heappush, heapify, heapreplace


class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

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


def load_coordinates(filename):
    coordinates = []
    with open(filename, "r") as file:
        for line in file:
            x, y, z = line.strip().split(",")
            coordinates.append(Coordinate(int(x), int(y), int(z)))
    return coordinates


def calculate_distance(coord1, coord2):
    return math.sqrt((coord1.x - coord2.x) ** 2 + (coord1.y - coord2.y) ** 2 + (coord1.z - coord2.z) ** 2)


def build_distance_heap(coordinates):
    heap = []
    heapify(heap)

    for index_from, from_coord in enumerate(coordinates):
        for to_coord in coordinates[index_from + 1:]:
            heappush(heap, Connection(from_coord, to_coord, calculate_distance(from_coord, to_coord)))

    return heap


def merge_or_add_connection(circuits, connection, nodes_connected, total_nodes):
    from_circuit = None
    to_circuit = None

    for circuit in circuits:
        if connection.from_coordinate in circuit and connection.to_coordinate in circuit:
            return 0, None
        if connection.from_coordinate in circuit:
            from_circuit = circuit
        elif connection.to_coordinate in circuit:
            to_circuit = circuit

    newly_connected_nodes = 0
    if from_circuit is not None and to_circuit is not None:
        circuits.remove(to_circuit)
        from_circuit.update(to_circuit)
    elif from_circuit is not None:
        from_circuit.add(connection.to_coordinate)
        newly_connected_nodes = 1
    elif to_circuit is not None:
        to_circuit.add(connection.from_coordinate)
        newly_connected_nodes = 1
    else:
        circuits.append({connection.from_coordinate, connection.to_coordinate})
        newly_connected_nodes = 2

    result2 = None
    if len(circuits) == 1 and nodes_connected + newly_connected_nodes == total_nodes:
        result2 = connection.from_coordinate.x * connection.to_coordinate.x

    return newly_connected_nodes, result2


def calculate_top3_product(circuits):
    heap = []
    heapify(heap)

    for circuit in circuits:
        if len(heap) < 3:
            heappush(heap, len(circuit))
        elif len(circuit) > heap[0]:
            heapreplace(heap, len(circuit))

    product = 1
    while len(heap) > 0:
        product *= heappop(heap)
    return product


MAX_CONNECTIONS = 1000


def main():
    nodes = load_coordinates("input.txt")
    distance_heap = build_distance_heap(nodes)
    circuits = []
    nodes_connected = 0
    counter = 0
    while counter < len(distance_heap):
        connection = heappop(distance_heap)
        newly_connected, result2 = merge_or_add_connection(circuits, connection, nodes_connected, len(nodes))
        nodes_connected += newly_connected
        if counter == MAX_CONNECTIONS:
            print("Result 1", calculate_top3_product(circuits))
        if result2 is not None:
            print("Result 2", result2)
            break
        counter += 1


if __name__ == "__main__":
    main()
