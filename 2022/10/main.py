instruction_cycle = 0
register_value = 1
relevant_amount_sum = 0
pixels_line = []
pixels = []


def process_instruction_cycle(increment=None):
    global pixels, pixels_line, instruction_cycle, relevant_amount_sum, register_value
    instruction_cycle += 1
    if (instruction_cycle - 20) % 40 == 0:
        relevant_amount_sum += instruction_cycle * register_value
    if len(pixels_line) % 40 == 0:
        pixels_line = []
        pixels.append(pixels_line)
    if register_value - 1 <= len(pixels_line) <= register_value + 1:
        pixels_line.append('#')
    else:
        pixels_line.append('.')
    if increment is not None:
        register_value += increment


for data in open("input.txt", "r"):
    instruction = data.strip().split(' ')
    operation = instruction[0]
    process_instruction_cycle()
    if len(instruction) > 1:
        process_instruction_cycle(int(instruction[1]))

print(relevant_amount_sum)

index = 0
for line in pixels:
    print(''.join(line))
