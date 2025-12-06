MAX_ROTATION = 100
INITIAL_POSITION = 50

position = INITIAL_POSITION
zero_count = 0
rotation_count = 0

with open("input.txt", "r") as file:
    for line in file:
        direction = line[0]
        rotation = int(line[1:])

        rotation_count += rotation // MAX_ROTATION
        rotation %= MAX_ROTATION

        old_position = position

        if direction == "L":
            position -= rotation
            if position < 0:
                position = MAX_ROTATION + position
                if old_position != 0:
                    rotation_count += 1
            elif rotation != 0 and position == 0:
                rotation_count += 1
        else:
            position += rotation
            if rotation != 0 and position == 0:
                rotation_count += 1
            elif position >= MAX_ROTATION:
                position %= MAX_ROTATION
                rotation_count += 1

        if position == 0:
            zero_count += 1

print(zero_count)
print(rotation_count)