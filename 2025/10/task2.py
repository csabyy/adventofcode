from common import *


def apply_button_to_current_joltage_state(current_state, button_to_apply):
    new_current_state = current_state.copy()
    for btn in button_to_apply:
        new_current_state[btn] -= 1
    return new_current_state


def filter_buttons_by_joltage(buttons, current_state):
    forbidden = {i for i, value in enumerate(current_state) if value <= 0}
    return [btn for btn in buttons if forbidden.isdisjoint(btn)]


def filter_button(buttons, include, exclude):
    return [btn for btn in buttons if include in btn and exclude not in btn]


def find_button_press(current_state, config_value):
    allowed_buttons = filter_buttons_by_joltage(config_value.button_config, current_state)

    result = None
    for diff_joltage_a_index, diff_joltage_a_value in enumerate(current_state):
        offset = diff_joltage_a_index + 1
        for diff_joltage_b_index, diff_joltage_b_value in enumerate(current_state[offset:]):
            filtered_button = []
            if diff_joltage_b_value > diff_joltage_a_value:
                filtered_button = filter_button(allowed_buttons, diff_joltage_b_index + offset, diff_joltage_a_index)
            elif diff_joltage_b_value < diff_joltage_a_value:
                filtered_button = filter_button(allowed_buttons, diff_joltage_a_index, diff_joltage_b_index + offset)
            if len(filtered_button) == 1:
                return filtered_button
            if len(filtered_button) > 0 and (result is None or len(filtered_button) < len(result)):
                result = filtered_button

    if result is not None:
        return result

    return allowed_buttons


def process_joltages_rec(initial_state, config_value):
    work_items = [initial_state]
    visited_states = set()
    while len(work_items) > 0:
        current_work_item = work_items.pop(0)
        for btn in current_work_item[1]:
            new_state = apply_button_to_current_joltage_state(current_work_item[0], btn)
            serialised_new_state = ".".join(str(x) for x in new_state)
            if serialised_new_state in visited_states:
                continue
            visited_states.add(serialised_new_state)

            if all(elem == 0 for elem in new_state):
                return current_work_item[2]

            work_items.append((new_state, find_button_press(new_state, config_value), current_work_item[2] + 1))


def process_joltages(config_values):
    result = 0
    for confix_ix, config_value in enumerate(config_values):
        current_state = config_value.joltage_config
        sub_total = process_joltages_rec((current_state, find_button_press(current_state, config_value), 1),
                                         config_value)
        print(confix_ix + 1, sub_total)
        result += sub_total
    return result


def main():
    print(process_joltages(load_config_from_file("input.txt")))


if __name__ == "__main__":
    main()

# 1 66
# 2 252
# 3 88
# 4 274
# 5 215
# 6 98
# 7 43
# 8 29
# 9 332
# 10 60
# 11 47
# 12 76
# 13 155
# 14 82
# 15 53
# 16 33
# 17 35
# 18 77
# 19 54
# 20 113
# 21 105
# 22 84
# 23 66
# 24 61
# 25 220
# 26 162
# 27 102
# 28 146
# 29 31
# 30 230
# 31 122
# 32 129
# 33 107
# 34 81
# 35 83
# 36 86
# 37 117
# 38 42
# 39 258
# 40 109
# 41 93
# 42 54
# 43 208
# 44 144
# 45 276
# 46 54
# 47 53
# 48 83
# 49 200
# 50 195
# 51 71
# 52 126
# 53 73
# 54 92
# 55 217
# 56 35
# 57 89
# 58 93
# 59 61
# 60 77
# 61 48
# 62 45
# 63 81
# 64 23
# 65 59
# 66 60
# 67 70
# 68 159
# 69 20
# 70 49
# 71 20
# 72 167
# 73 64
# 74 57
# 75 85
# 76 5
# 77 92
# 78 272
# 79 59
# 80 94
# 81 59
# 82 109
# 83 69
# 84 22
# 85 73
# 86 36
# 87 25
# 88 180
# 89 25
# 90 77
# 91 204
# 92 114
# 93 231
# 94 96
# 95 69
# 96 199
# 97 56
# 98 174
# 99 66
# 100 70
# 101 118
# 102 172
# 103 63
# 104 98
# 105 59
# 106 46
# 107 22
# 108 94
# 109 35
# 110 103
# 111 67
# 112 228
# 113 68
# 114 23
# 115 40
# 116 76
# 117 159
# 118 82
# 119 56
# 120 83
# 121 51
# 122 46
# 123 37
# 124 51
# 125 70
# 126 242
# 127 40
# 128 27
# 129 264
# 130 157
# 131 226
# 132 42
# 133 192
# 134 52
# 135 207
# 136 75
# 137 106
# 138 115
# 139 93
# 140 123
# 141 94
# 142 87
# 143 53
# 144 162
# 145 87
# 146 98
# 147 104
# 148 219
# 149 52
# 150 58
# 151 94
# 152 51
# 153 235
# 154 225
# 155 204
# 156 53
# 157 74
# 158 89
# 159 76
# 160 188
# 161 58
# 162 76
# 163 103
# 164 83
# 165 17
# 166 107
# 167 96
# 168 51
# 169 54
# 170 63
# 171 161
# 172 44
# 17424
