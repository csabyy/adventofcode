def process_set(game_set, min_set):
    cube_set = game_set.split(",")

    for draw in cube_set:
        cube = draw.strip().split(" ")
        colour = cube[1]
        amount = int(cube[0])
        if min_set.get(colour) < amount:
            min_set[colour] = amount


def process_game(game):
    game_sets = game.split(";")
    min_set = {"red": 0, "green": 0, "blue": 0}
    for game_set in game_sets:
        process_set(game_set, min_set)

    return min_set.get("red") * min_set.get("blue") * min_set.get("green")


counter = 0
for line in open("input.txt", "r"):
    counter += process_game(line.split(":")[1].strip())

print(counter)
