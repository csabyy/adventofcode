import re


def get_last_int(control_row):
    return int(re.findall("\\d+", control_row).pop())


def get_all_int(instruction):
    result = re.findall("\\d+", instruction)
    return list(map(int, result))


def parse_instruction(instruction_row, stck):
    instructions = get_all_int(instruction_row)
    source_stack = stck[instructions[1] - 1]
    destination_stack = stck[instructions[2] - 1]
    return source_stack, destination_stack, instructions[0]


def initialise_stack(size):
    x = []
    for i in range(0, size):
        x.append([])
    return x


def convert_to_stack(input_stack_rows):
    control_row = input_stack_rows[len(input_stack_rows) - 1]
    stck = initialise_stack(get_last_int(control_row))
    index = len(input_stack_rows) - 2
    while index >= 0:
        current_line = input_stack_rows[index]
        line_index = 1
        stack_index = 0
        while line_index < len(current_line):
            crate = current_line[line_index]
            if crate.strip():
                stck[stack_index].append(crate)
            stack_index += 1
            line_index += 4
        index -= 1
    return stck


def move_creates(instruction_row, stck):
    source_stack, destination_stack, items_to_move = parse_instruction(instruction_row, stck)
    while items_to_move > 0:
        crate = source_stack.pop()
        destination_stack.append(crate)
        items_to_move -= 1


def move_n_creates(instruction_row, stck):
    source_stack, destination_stack, items_to_move = parse_instruction(instruction_row, stck)
    crates = source_stack[len(source_stack) - items_to_move:]
    for crate in crates:
        destination_stack.append(crate)
    del source_stack[len(source_stack) - items_to_move:]


def get_last_chars(stck):
    result = ""
    for stack_item in stck:
        result += stack_item[-1]
    return result


stack_rows = []
stack = []
stack2 = []
for data in open("input.txt", "r"):
    row = data.rstrip()
    if not row:
        stack = convert_to_stack(stack_rows)
        stack2 = convert_to_stack(stack_rows)
    elif not stack:
        stack_rows.append(row)
    else:
        move_creates(row, stack)
        move_n_creates(row, stack2)

print(get_last_chars(stack))
print(get_last_chars(stack2))
