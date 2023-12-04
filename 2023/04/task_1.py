import re

result = 0
for line in open("input.txt", "r"):
    colon_index = line.index(":")
    card_data = line[colon_index + 1:len(line)].split("|")
    winning_set = set(re.findall("\\d+", card_data[0]))
    numbers = re.findall("\\d+", card_data[1])
    hit = 0
    for nr in numbers:
        if nr in winning_set:
            hit +=1
    if hit > 0:
        result += pow(2, hit - 1)

print(result)


