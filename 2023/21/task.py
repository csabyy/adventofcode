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


def dedupe_tiles(tiles):
    tile_map = {}
    for tile in tiles:
        if tile[0] in tile_map:
            tile_map[tile[0]].add(tile[1])
        else:
            tile_map[tile[0]] = {tile[1]}
    deduped = []
    for key, value in tile_map.items():
        for set_item in value:
            deduped.append((key, set_item))
    return deduped

def traverse_garden(current_position, garden_matrix, max_steps):
    visited_tiles = init_visited_tiles(garden_matrix)
    tiles = current_position
    current_steps = 0
    new_tiles_per_step = [1]
    while len(tiles) > 0 and current_steps < max_steps:
        tiles_next = []
        for tile in tiles:
            if visited_tiles[tile[0]][tile[1]]:
                continue
            visited_tiles[tile[0]][tile[1]] = True
            next_tiles = get_possible_tiles(tile, garden_matrix, visited_tiles)
            for next_tile in next_tiles:
                tiles_next.append(next_tile)
        tiles = tiles_next
        new_tiles_per_step.append(len(tiles))
        current_steps += 1
    # visualise_visited_tiles(visited_tiles)
    return new_tiles_per_step


def get_possible_location_count(new_tiles_per_step):
    counter = len(new_tiles_per_step) - 1
    result = 0
    while counter > -1:
        result += new_tiles_per_step[counter]
        counter -= 2
    return result



garden_map, start_pos = init_garden_map()
start = time.time()
new_locations = traverse_garden([start_pos], garden_map, 7000)
print("First task:", get_possible_location_count(new_locations))
end = time.time()

print(f"Time taken to run the code was {end-start} seconds")
