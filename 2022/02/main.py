#   A   B   C
# X 3   1   6  +1
# Y 6   3   1  +2
# Z 1   6   3  +3
score_map = {
    'X': {"extra": 1, "points": [3, 0, 6]},
    'Y': {"extra": 2, "points": [6, 3, 0]},
    'Z': {"extra": 3, "points": [0, 6, 3]}
}

#   A       B       C
# X 0 (3)   0 (1)   0 (2)
# Y 3 (1)   3 (2)   3 (3)
# Z 6 (2)   6 (3)   6 (1)
score_map2 = {
    'X': {"extra": 0, "points": [3, 1, 2]},
    'Y': {"extra": 3, "points": [1, 2, 3]},
    'Z': {"extra": 6, "points": [2, 3, 1]}
}

opponent_coordinates = {
    'A': 0,
    'B': 1,
    'C': 2
}


def get_round_points(opponent, own, source_map):
    current_choice = source_map[own]
    return current_choice["extra"] + current_choice["points"][opponent]


total = 0
for data in open("input.txt", "r"):
    total += get_round_points(opponent_coordinates[data[0]], data[2], score_map)

print(total)
