import re

rock_map = []
with open("input.txt", "r") as file:
    for line in file:
        rock_map.append(line.strip())


def find_sections(line):
    current_start = 0
    sections = []
    while current_start < len(line):
        section_end_offset = line[current_start:].find("#")
        section_end = len(line) if section_end_offset == -1 else current_start + section_end_offset
        sections.append((current_start, section_end))
        current_start = section_end + 1
    return sections

def get_section_weight(line, section_start, section_end):
    result = 0
    rocks = re.findall("O", line[section_start:section_end])
    for x in range(len(rocks)):
        result += len(line) - section_start - x
    return result


total = 0
vertical_line = None
for rock_map_column_index in range(len(rock_map[0])):
    if not vertical_line:
        vertical_line = []
    for rock_map_line in rock_map:
        vertical_line.append(rock_map_line[rock_map_column_index])
    current_line = "".join(vertical_line)
    vertical_line = None
    sections = find_sections(current_line)
    for section in sections:
        total += get_section_weight(current_line, section[0], section[1])

print(total)