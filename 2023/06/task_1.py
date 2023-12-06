import re

time_list = []
distance_list = []
with open("input.txt", "r") as file:
    time_list = re.findall("\\d+", file.readline())
    distance_list = re.findall("\\d+", file.readline())

result = None
counter = 0
while counter < len(time_list):
    time = int(time_list[counter])
    distance = int(distance_list[counter])
    index = 1
    round_combinations = 0
    while index < time:
        if (time - index) * index > distance:
            round_combinations += 1
        index += 1
    result = result * round_combinations if result else round_combinations
    counter += 1

print(result)