import re


parts = []
instructions = []
with open("input.txt", "r") as file:
    for line in file:
        line_parts = line.split(" ")
        parts.append(line_parts[0])
        instructions.append(list(map(int, re.findall("\\d+", line_parts[1]))))


def process_hash(current_parts, instructions, streak, cache):
    next_char = current_parts[1] if len(current_parts) > 1 else "."
    if streak + 1 == instructions[0]:
        if next_char == "#":
            return 0
        else:
            return process_parts_rec(current_parts[min(len(current_parts), 2):], instructions[1:], 0, cache)

    next_dot_pos = current_parts.find(".")
    section_length = next_dot_pos if next_dot_pos > -1 else len(current_parts)
    if section_length + streak < instructions[0]:
        return 0
    if section_length + streak == instructions[0]:
        return process_parts_rec(current_parts[min(len(current_parts), section_length + 1):], instructions[1:], 0, cache)
    return process_parts_rec(current_parts[1:], instructions, streak + 1, cache)

def process_dot(current_parts, instructions, streak, cache):
    if streak == instructions[0]:
        return process_parts_rec(current_parts[1:], instructions[1:], 0, cache)
    if streak == 0:
        return process_parts_rec(current_parts[1:], instructions, 0, cache)
    else:
        return 0


def process_parts_rec(current_parts, instructions, streak, cache):
    if len(instructions) == 0:
        if current_parts.find("#") > -1:
            return 0
        return 1
    if len(current_parts) == 0:
        return 0

    if streak + len(current_parts) < sum(instructions) + len(instructions) - 1:
        return 0

    subtree = cache.get(str(streak) + current_parts)
    if subtree:
        cached_value = subtree.get(len(instructions))
        if cached_value:
            return cached_value

    sub_total = 0
    if current_parts[0] == "#":
        sub_total = process_hash(current_parts, instructions, streak, cache)
    elif current_parts[0] == ".":
        sub_total = process_dot(current_parts, instructions, streak, cache)
    elif current_parts[0] == "?":
        sub_total = process_hash(current_parts, instructions, streak, cache) + process_dot(current_parts, instructions, streak, cache)

    if not subtree:
        cache[str(streak) + current_parts] = { len(instructions): sub_total }
    else:
        subtree[len(instructions)] = sub_total
    return sub_total

result = 0
for parts_index, current_parts in enumerate(parts):
    result += process_parts_rec(current_parts, instructions[parts_index], 0, {})
print(result)


result2 = 0
for parts_index, current_parts in enumerate(parts):
    result2 += process_parts_rec("?".join([current_parts] * 5), instructions[parts_index] * 5, 0, {})
print(result2)
