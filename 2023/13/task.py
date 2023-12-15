patterns = []
patterns_transpose = []


def check_pattern_rec(current_pattern, streak, has_previous):
    if len(current_pattern) == 1:
        return 0

    if len(current_pattern) == 0:
        return streak

    if current_pattern[0] == current_pattern[len(current_pattern) - 1]:
        candidate = check_pattern_rec(current_pattern[1:len(current_pattern) - 1], streak + 1, True)
        if candidate > 0:
            return candidate
    if has_previous:
        return 0
    return check_pattern_rec(current_pattern[:len(current_pattern) - 1], 0, has_previous)


def check_pattern(current_pattern, old_start_index, old_streak):
    i = 0
    while i < len(current_pattern):
        streak = check_pattern_rec(current_pattern[i:], 0, i != 0)
        if streak > 0 and (old_start_index != i or old_streak != streak):
            return i, streak
        i += 1
    return -1, -1


def replacement_candidates(pattern):
    replacement_candidate_list = {}
    for current_pattern_index, current_pattern in enumerate(pattern):
        counter = current_pattern_index + 1
        while counter < len(pattern):
            other_line = pattern[counter]
            diff_counter = 0
            for line_char_index, line_char in enumerate(current_pattern):
                if line_char != other_line[line_char_index]:
                    diff_counter += 1
                if diff_counter > 1:
                    break
            if diff_counter == 1:
                if replacement_candidate_list.get(current_pattern_index):
                    replacement_candidate_list[current_pattern_index].add(other_line)
                else:
                    replacement_candidate_list[current_pattern_index] = {other_line}
                if replacement_candidate_list.get(counter):
                    replacement_candidate_list[counter].add(current_pattern)
                else:
                    replacement_candidate_list[counter] = { current_pattern}
            counter += 1
    return replacement_candidate_list


def get_replacement_value(pattern, replacement_candidates):
    original_start, original_streak = check_pattern(pattern, -1, -1)

    for key, replacements in replacement_candidates.items():
        for replacement in replacements:
            new_pattern = pattern[:key] + [replacement] + pattern[key + 1:]
            new_start, new_streak = check_pattern(new_pattern, original_start, original_streak)
            if new_start > -1 and (original_start != new_start or original_streak != new_streak):
                return new_start, new_streak
    return -1, -1


with open("input.txt", "r") as file:
    pattern = []
    pattern_transpose = None

    for line_number, line in enumerate(line.strip() for line in file):
        if len(line) == 0:
            patterns.append(pattern)
            patterns_transpose.append(pattern_transpose)
            pattern = []
            pattern_transpose = None
        else:
            if not pattern_transpose:
                pattern_transpose = []
                for i in range(len(line)):
                    pattern_transpose.append("")
            pattern.append(line)
            for char_number, char_in_line in enumerate(line):
                pattern_transpose[char_number] += char_in_line
    patterns.append(pattern)
    patterns_transpose.append(pattern_transpose)

result = 0
for pattern_x, pattern in enumerate(patterns):
    h_start, h_streak = check_pattern(pattern, -1, -1)
    if h_start > -1:
        result += (h_start + h_streak) * 100
    else:
        v_start, v_streak = check_pattern(patterns_transpose[pattern_x], -1, -1)
        result += v_start + v_streak

print(result)

result2 = 0
for pattern_x, pattern in enumerate(patterns):
    replacement_candidates_horizontal = replacement_candidates(pattern)
    replacement_candidates_vertical = replacement_candidates(patterns_transpose[pattern_x])
    new_h_start, new_h_streak = get_replacement_value(pattern, replacement_candidates_horizontal)
    if new_h_start > -1:
        result2 += (new_h_start + new_h_streak) * 100
    else:
        new_v_start, new_v_streak = get_replacement_value(patterns_transpose[pattern_x], replacement_candidates_vertical)
        result2 += new_v_start + new_v_streak

print(result2)
