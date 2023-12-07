from hand import Hand, get_rank


def get_card_value(card):
    if card == "A":
        return "E"
    if card == "K":
        return "D"
    if card == "Q":
        return "C"
    if card == "J":
        return "1"
    if card == "T":
        return "A"
    return card


def rank_hand(hand):
    card_map = {}
    hand_value = ""
    max_key = None
    max_value = 0
    for card in hand.cards:
        hand_value += get_card_value(card)
        if card in card_map:
            card_map[card] = card_map.get(card) + 1
        else:
            card_map[card] = 1
        if card != "J" and max_value < card_map[card]:
            max_value = card_map[card]
            max_key = card
    if max_key and "J" in card_map:
        jokers = card_map.get("J")
        card_map[max_key] += jokers
        card_map.pop("J")
    hand.set_rank(get_rank(card_map))
    hand.set_hand_value(int(hand_value, 16))


hands = []
with open("input.txt", "r") as file:
    for _, line in enumerate(file, start=1):
        line_data = line.split(" ")
        hand = Hand(line_data[0].strip(), int(line_data[1]))
        rank_hand(hand)
        hands.append(hand)

result = 0
for index, hand in enumerate(sorted(hands)):
    result += hand.bid * (index + 1)

print(result)
