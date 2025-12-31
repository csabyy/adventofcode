def read_input(filename):
    with open(filename, "r") as file:
        boxes = []
        areas = []
        current_box = []

        for line in file:
            if "#" in line or "." in line:
                current_box.append(line.strip())
            elif line.strip() == "" and len(current_box) > 0:
                boxes.append(current_box)
                current_box = []
            elif "x" in line:
                dimensions, amounts = line.split(":")
                areas.append(([int(x) for x in dimensions.split("x")], [int(x) for x in amounts.strip().split(" ")]))
    return boxes, areas


def calculate_area(boxes):
    areas = []
    for box in boxes:
        area = 0
        for box_line in box:
            for box_item in box_line:
                if box_item == "#":
                    area += 1
        areas.append(area)
    return areas


def calculate_required_area(boxes_area, required_boxes):
    required_area = 0
    for box_index, required_box in enumerate(required_boxes):
        required_area += boxes_area[box_index] * required_box
    return required_area


def main():
    boxes, areas = read_input("input.txt")
    boxes_area = calculate_area(boxes)

    possible_areas = 0
    for area in areas:
        if area[0][0] * area[0][1] >= calculate_required_area(boxes_area, area[1]):
            possible_areas += 1
    print(possible_areas)

if __name__ == "__main__":
    main()
