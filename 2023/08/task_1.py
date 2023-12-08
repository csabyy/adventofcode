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

def traverse_map():
    current_node = direction_map.get("AAA")
    steps = 0
    while 1:
        for instruction in instructions:
            steps += 1
            index = 0 if instruction == "L" else 1
            if current_node[index] == "ZZZ":
                return steps
            current_node = direction_map.get(current_node[index])


print(traverse_map())