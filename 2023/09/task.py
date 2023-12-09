import re


def process_line_rec(data_line):
    if len(data_line) == 0 or all(item == 0 for item in data_line):
        return 0

    new_line = []
    counter = 0
    while counter < len(data_line) - 1:
        new_line.append(data_line[counter + 1] - data_line[counter])
        counter += 1

    return data_line[len(data_line) - 1] + process_line_rec(new_line)


result1 = 0
result2 = 0
with open("input.txt", "r") as file:
    for line in file:
        data_line = list(map(int, re.findall("-?\\d+", line)))
        result1 += process_line_rec(data_line)
        result2 += process_line_rec(data_line[::-1])

print(result1)
print(result2)
