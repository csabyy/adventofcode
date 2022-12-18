import math
import re
from heapq import heappop, heappush
from collections import deque


class Monkey:
    def __init__(self):
        self.items = deque()
        self.test = None
        self.test_true = None
        self.test_false = None
        self.transformation = None
        self.inspected_items = 0


def parse_integers(txt):
    return list(map(int, re.findall("\\d+", txt)))


def parse_operation_rec(tokens, x):
    if "*" in tokens:
        multiply_index = tokens.index("*")
        return parse_operation_rec(tokens[0:multiply_index], x) * parse_operation_rec(tokens[multiply_index+1:], x)
    if "+" in tokens:
        add_index = tokens.index("+")
        return parse_operation_rec(tokens[0:add_index], x) + parse_operation_rec(tokens[add_index + 1:], x)
    if len(tokens) == 1:
        if tokens[0].isnumeric():
            return int(tokens[0])
        if tokens[0] == "old":
            return x


def parse_operation(txt):
    tokens = re.findall("\\S+", txt)
    equal_index = tokens.index('=')
    return lambda x: parse_operation_rec(tokens[equal_index+1:], x)


def play_rounds(number_of_rounds, worry_relief=1):
    lcm = 1  # Least Common Multiple
    for mon in monkeys:
        lcm = math.lcm(lcm, mon.test)
    for _ in range(number_of_rounds):
        for mon in monkeys:
            while len(mon.items) > 0:
                current_item = mon.items.popleft()
                transformed = int(mon.transformation(current_item) / worry_relief) % lcm
                next_monkey_index = mon.test_true if transformed % mon.test == 0 else mon.test_false
                monkeys[next_monkey_index].items.append(transformed)
                mon.inspected_items += 1


def get_monkey_business():
    inspected_items = []
    for mon in monkeys:
        heappush(inspected_items, mon.inspected_items * (-1))
    return heappop(inspected_items) * heappop(inspected_items)


monkeys = []
monkey = None

for data in open("input.txt", "r"):
    line = data.strip()
    if line.startswith("Monkey"):
        monkey = Monkey()
        monkeys.append(monkey)
    if line.startswith("Starting items"):
        for item in parse_integers(line):
            monkey.items.append(item)
    elif line.startswith("Operation"):
        monkey.transformation = parse_operation(line)
    elif line.startswith("Test: divisible by"):
        monkey.test = parse_integers(line).pop()
    elif line.startswith("If true:"):
        monkey.test_true = parse_integers(line).pop()
    elif line.startswith("If false:"):
        monkey.test_false = parse_integers(line).pop()


# play_rounds(20, 3)
# print(get_monkey_business())
play_rounds(10000)
print(get_monkey_business())
