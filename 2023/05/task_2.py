import re
import sys


def map_input(input_val, map_items):
    closest_interval = None
    for destination, source, offset in map_items:
        source = int(source)
        offset = int(offset)
        if input_val < source:
            closest_candidate = source - input_val
            if not closest_interval or closest_candidate < closest_interval:
                closest_interval = closest_candidate
        elif source <= input_val < source + offset:
            diff = input_val - source
            return int(destination) + diff, offset - diff
    return input_val, closest_interval


def process_maps(input_val, skip_count, maps):
    if not maps:
        return input_val, skip_count
    transformed_input, skip = map_input(input_val, maps[0])
    return process_maps(transformed_input, min(skip_count if skip is None else skip, skip_count), maps[1:])


seeds = []
map_list = []
map_item = None
with open("input.txt", "r") as file:
    for line_count, line in enumerate(file, start=1):
        if line_count == 1:
            seeds = re.findall("\\d+", line)
            continue
        if not line.strip():
            if map_item:
                map_list.append(map_item)
            map_item = []
            continue

        map_elements = re.findall("\\d+", line)
        if len(map_elements) == 3:
            map_item.append(map_elements)
    if map_item is not None:
        map_list.append(map_item)

seed_index = 0
result = sys.maxsize
i = 0
while seed_index + 2 < len(seeds):
    current_seed_id = int(seeds[seed_index])
    current_seed_max = current_seed_id + int(seeds[seed_index + 1])
    while current_seed_id < current_seed_max:
        transformed_input, skip = process_maps(int(current_seed_id), sys.maxsize, map_list)
        current_seed_id += skip
        i += 1
        print(i)
        if transformed_input < result:
            result = transformed_input
    seed_index += 2

print(result)

