import time

def init_garden_map():
    start_pos = None
    garden_map = []
    with open("input.txt", "r") as file:
        for line_index, line in enumerate(file):
            rock_map_line = []
            for line_char_index, line_char in enumerate(line.strip()):
                if line_char == "S":
                    start_pos = line_index, line_char_index
                rock_map_line.append(line_char)
            garden_map.append(rock_map_line)
    return garden_map, start_pos


def init_visited_tiles(garden_matrix):
    visited_matrix = []
    for garden_matrix_line_ix in range(len(garden_matrix)):
        visited_matrix_line = []
        for garden_matrix_item_ix in range(len(garden_matrix[0])):
            visited_matrix_line.append(False)
        visited_matrix.append(visited_matrix_line)
    return visited_matrix


def get_possible_tiles(current_position, garden_matrix, visited_tiles):
    current_y, current_x = current_position
    possible_tiles = []
    if current_y - 1 >= 0 and garden_matrix[current_y - 1][current_x] != "#" and not visited_tiles[current_y - 1][current_x]:
        possible_tiles.append((current_y - 1, current_x))
    if current_y + 1 < len(garden_matrix) and garden_matrix[current_y + 1][current_x] != "#" and not \
    visited_tiles[current_y + 1][current_x]:
        possible_tiles.append((current_y + 1, current_x))
    if current_x - 1 >= 0 and garden_matrix[current_y][current_x - 1] != "#" and not visited_tiles[current_y][current_x - 1]:
        possible_tiles.append((current_y, current_x - 1))
    if current_x + 1 < len(garden_matrix[0]) and garden_matrix[current_y][current_x + 1] != "#" and not \
    visited_tiles[current_y][current_x + 1]:
        possible_tiles.append((current_y, current_x + 1))
    return possible_tiles


def visualise_visited_tiles(visited_tiles):
    for visited_tile_line in visited_tiles:
        buffer = ""
        for visited_tile_char in visited_tile_line:
            buffer += "." if not visited_tile_char else "O"
        print(buffer)


def traverse_garden(start_position, garden_matrix, max_steps):
    result_counter = 0
    visited_tiles = init_visited_tiles(garden_matrix)
    visited_tiles[start_position[0]][start_position[1]] = True
    current_steps = 0
    tiles = [start_position]

    while len(tiles) > 0 and current_steps < max_steps:
        if current_steps % 2 == max_steps % 2:
            result_counter += len(tiles)
        tiles_next = []
        for tile in tiles:
            next_tiles = get_possible_tiles(tile, garden_matrix, visited_tiles)
            for next_tile in next_tiles:
                visited_tiles[next_tile[0]][next_tile[1]] = True
                tiles_next.append(next_tile)
        tiles = tiles_next
        current_steps += 1
    if len(tiles) > 0 and current_steps % 2 == max_steps % 2:
        result_counter += len(tiles)
    # visualise_visited_tiles(visited_tiles)
    return result_counter



garden_map, start_pos = init_garden_map()
start = time.time()
for i in range(0, 11):
    print("First task:",  traverse_garden(start_pos, garden_map, 10 + i * 11))
end = time.time()
print(f"Time taken to run the code was {end-start} seconds")
