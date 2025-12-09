def consolidate_ranges(accumulator, ranges_to_check):
    if len(ranges_to_check) == 0:
        return accumulator

    range = ranges_to_check[0]
    new_range_to_check = ranges_to_check[1:]
    new_accumulator = []
    is_overlapping = False
    for existing_range in accumulator:
        min_start_value = existing_range[0]
        max_end_value = existing_range[1]
        if range[0] < min_start_value <= range[1]:
            min_start_value = range[0]
            is_overlapping = True
        if range[0] <= max_end_value < range[1]:
            max_end_value = range[1]
            is_overlapping = True
        if min_start_value <= range[0] <= max_end_value and min_start_value <= range[1] <= max_end_value:
            is_overlapping = True
        if min_start_value != existing_range[0] or max_end_value != existing_range[1]:
            new_range_to_check.append([min_start_value, max_end_value])
        else:
            new_accumulator.append(existing_range)
    if not is_overlapping:
        new_accumulator.append([range[0], range[1]])

    return consolidate_ranges(new_accumulator, new_range_to_check)

def count_set(ranges):
    count = 0
    for range in ranges:
        count += range[1] - range[0] + 1
    return count

def count_ingredients(ingredients, ranges):
    result = 0
    for ingredient in ingredients:
        for range in ranges:
            if range[0] <= ingredient <= range[1]:
                result += 1
                break
    return result


def process_input():
    ranges = []
    ingredients = []
    with open("input.txt", "r") as file:
        is_range_instruction = True
        for line in file:
            trimmed_line = line.strip()
            if len(trimmed_line) == 0:
                is_range_instruction = False
                continue
            if is_range_instruction:
                split_line = line.split("-")
                ranges.append([int(split_line[0]), int(split_line[1])])
            else:
                ingredients.append(int(trimmed_line))
    return (ranges, ingredients)

(ranges, ingredients) = process_input()
print(count_ingredients(ranges, ingredients))
print(count_set(consolidate_ranges([], ranges)))
