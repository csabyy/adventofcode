class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"


knots = [Point(0, 0) for _ in range(9)]
knot = Point(0, 0)
head_position = Point(0, 0)
visited_points = set()
visited_points2 = set()


def get_vector_from_direction(direction):
    if direction == 'D':
        return Point(0, -1)
    if direction == 'U':
        return Point(0, 1)
    if direction == 'R':
        return Point(1, 0)
    return Point(-1, 0)


def move_head(position, adjustment):
    position.x += adjustment.x
    position.y += adjustment.y


def move_tail(tail, head, adjustment):
    if abs(tail.x - head.x) <= 1 and abs(tail.y - head.y) <= 1:
        return Point(0, 0)
    if abs(adjustment.x) > 0 and abs(adjustment.y) > 0:
        if tail.y == head.y:
            tail.x += adjustment.x
            return Point(tail_movement.x, 0)
        if tail.x == head.x:
            tail.y += adjustment.y
            return Point(0, tail_movement.y)
        tail.y += adjustment.y
        tail.x += adjustment.x
        return adjustment
    old_tail_x = tail.x
    old_tail_y = tail.y
    tail.x = head.x - adjustment.x
    tail.y = head.y - adjustment.y
    return Point(tail.x - old_tail_x, tail.y - old_tail_y)


for data in open("input.txt", "r"):
    row = data.strip().split(' ')
    movement = get_vector_from_direction(row[0])
    for _ in range(int(row[1])):
        move_head(head_position, movement)

        # part 1
        move_tail(knot, head_position, movement)
        visited_points.add(knot.__str__())

        # part 2
        tail_movement = move_tail(knots[0], head_position, movement)
        knots_counter = 0
        while knots_counter < len(knots) - 1:
            if tail_movement.x == 0 and tail_movement.y == 0:
                break
            tail_movement = move_tail(knots[knots_counter + 1], knots[knots_counter], tail_movement)
            knots_counter += 1
        visited_points2.add(knots[len(knots) - 1].__str__())

print(len(visited_points))
print(len(visited_points2))
