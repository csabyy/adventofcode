import re

# map for storing scratch cards: card number - amount
extra_scratchcard = {}


result = 0
current_card = 0
for line in open("input.txt", "r"):
    colon_index = line.index(":")
    card_data = line[colon_index + 1:len(line)].split("|")
    winning_set = set(re.findall("\\d+", card_data[0]))
    numbers = re.findall("\\d+", card_data[1])
    hit = 0
    current_tickets = extra_scratchcard.get(current_card)
    increment_value = current_tickets + 1 if current_tickets is not None else 1
    for nr in numbers:
        if nr in winning_set:
            hit += 1
            increment_card_index = current_card + hit
            if increment_card_index in extra_scratchcard:
                extra_scratchcard[increment_card_index] += increment_value
            else:
                extra_scratchcard[increment_card_index] = increment_value
    current_card += 1

for extra_card in extra_scratchcard.values():
    result += extra_card

print(result + current_card)


