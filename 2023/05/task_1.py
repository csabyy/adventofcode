import re
import sys


def map_input(input_val, map_items):
    for destination, source, offset in map_items:
        source = int(source)
        offset = int(offset)
        if source <= input_val < source + offset:
            diff = input_val - source
            return int(destination) + diff
    return input_val


def process_maps(input_val, maps):
    if not maps:
        return input_val
    return process_maps(map_input(input_val, maps[0]), maps[1:])


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

minimum_location = sys.maxsize
for seed in seeds:
    local_minimum = process_maps(int(seed), map_list)
    if local_minimum < minimum_location:
        minimum_location = local_minimum

print(minimum_location)
