def sum_numbers(numbers):
    array_sum = 0
    for number in numbers:
        array_sum += number
    return array_sum


def add_to_dict(dictionary, key, value):
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value


def process_map(beam_map, start_index):
    beam_locations_dict = {start_index: 1}
    counter = 0
    for beam_row in beam_map:
        for beam_column in beam_row:
            if beam_column in beam_locations_dict:
                counter += 1
                combinations = beam_locations_dict.pop(beam_column)
                add_to_dict(beam_locations_dict, beam_column - 1, combinations)
                add_to_dict(beam_locations_dict, beam_column + 1, combinations)
    return counter, sum_numbers(beam_locations_dict.values())


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def process_input():
    with open("input.txt", "r") as file:
        start_index = file.readline().find("S")
        row_map = []
        for line in file:
            found_splitters = find(line, "^")
            if len(found_splitters) > 0:
                row_map.append(find(line, "^"))
        return row_map, start_index


(beam_map, start_index) = process_input()
print(process_map(beam_map, start_index))
