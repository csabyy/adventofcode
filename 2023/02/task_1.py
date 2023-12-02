limit = {"red": 12, "green": 13, "blue": 14 }


def process_set(game_set):
    cube_set = game_set.split(",")
    for draw in cube_set:
        cube = draw.strip().split(" ")
        colour = cube[1]
        amount = int(cube[0])
        if limit.get(colour) < amount:
            return False
    return True


def process_game(game):
    game_sets = game.split(";")
    for game_set in game_sets:
        if not process_set(game_set):
            return False
    return True


counter = 0

line_number = 0
for line in open("input.txt", "r"):
    line_number += 1
    if process_game(line.split(":")[1].strip()):
        counter += line_number

print(counter)
