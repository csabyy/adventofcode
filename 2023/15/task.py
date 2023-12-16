import re


def calculate_hash(item):
    current_value = 0
    for current_char in item:
        current_value = ((current_value + ord(current_char)) * 17) % 256
    return current_value


def add_item(boxes, box_number, item_key, item_value):
    if box_number in boxes.keys():
        for lens in boxes[box_number]:
            if lens[0] == item_key:
                lens[1] = item_value
                return
        boxes[box_number].append([item_key, item_value])
    else:
        boxes[box_number] = [[item_key, item_value]]


def remove_item(boxes, box_number, item_key):
    if box_number in boxes.keys():
        lens_index_to_remove = None
        for lens_index, lens in enumerate(boxes[box_number]):
            if lens[0] == item_key:
                lens_index_to_remove = lens
                break
        if lens_index_to_remove:
            boxes[box_number].remove(lens_index_to_remove)


def arrange_lenses(instructions):
    boxes = {}
    for instruction in instructions:
        instruction_parts = re.findall("\\w+", instruction)
        is_addition = instruction.find("=") > -1
        box_number = calculate_hash(instruction_parts[0])
        if is_addition:
            add_item(boxes, box_number, instruction_parts[0], int(instruction_parts[1]))
        else:
            remove_item(boxes, box_number, instruction_parts[0])
    return boxes


def calculate_result(arranged_boxes):
    result = 0
    for box_id, lenses in arranged_boxes.items():
        for lens_index, lens in enumerate(lenses):
            result += (box_id + 1) * (lens_index + 1) * (lens[1])
    return result


with open("input.txt", "r") as file:
    instructions = file.readline().strip().split(",")

print(sum(map(calculate_hash, instructions)))
print(calculate_result(arrange_lenses(instructions)))
