import math
import re

instructions = None
direction_map = {}
with open("input.txt", "r") as file:
    instructions = file.readline().strip()
    for line in file:
        if line.strip():
            direction = line.split("=")
            source = direction[0].strip()
            if not direction_map.items():
                start_location = source
            direction_map[source] = re.findall("\\w+", direction[1])


def traverse_map(initial_direction):
    cycle_detection = {initial_direction: {0: 0}}
    current_node = direction_map.get(initial_direction)
    destination_steps = []
    steps = 0
    while 1:
        for instructions_x, instruction in enumerate(instructions):
            instructions_index = instructions_x + 1
            steps += 1
            index = 0 if instruction == "L" else 1
            if current_node[index].endswith("Z"):
                destination_steps.append(steps)
            if current_node[index] in cycle_detection:
                if instructions_index in cycle_detection[current_node[index]]:
                    return destination_steps, steps - cycle_detection[current_node[index]][instructions_index]
                else:
                    cycle_detection[current_node[index]][instructions_index] = steps
            else:
                cycle_detection[current_node[index]] = {instructions_index: steps}
            current_node = direction_map.get(current_node[index])


def merge_cycles(cycle_a, cycle_b):
    # TODO: iterate over every item
    offset_a = cycle_a[0][0]
    offset_b = cycle_b[0][0]
    round_a = cycle_a[1]
    round_b = cycle_b[1]
    counter = 0
    fraction = (round_b * counter + (offset_b - offset_a)) / round_a
    while not fraction.is_integer():
        fraction = (round_b * counter + (offset_b - offset_a)) / round_a
        counter += 1
    new_offset = offset_b + round_b * counter
    new_round = math.lcm(round_a, round_b)
    return [new_offset], new_round

cycles = []
for direction in direction_map:
    if direction.endswith("A"):
        current_cycles = traverse_map(direction)
        cycles.append(current_cycles)

merged = cycles[0]
counter = 0
while counter < len(cycles) - 1:
    merged = merge_cycles(cycles[counter + 1], merged)
    counter += 1

print(merged[0][0])
