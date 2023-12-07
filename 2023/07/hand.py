class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.bucket = 0
        self.rank = 0
        self.hand_value = 0

    def set_rank(self, rank):
        self.rank = rank

    def set_hand_value(self, hand_value):
        self.hand_value = hand_value

    def __eq__(self, other):
        return self.rank == other.rank and self.hand_value == other.hand_value

    def __lt__(self, other):
        return self.rank < other.rank or self.rank == other.rank and self.hand_value < other.hand_value


five_of_a_kind = 6
four_of_a_kind = 5
full_house = 4
three_of_a_kind = 3
two_pair = 2
one_pair = 1
high_card = 0


def get_rank(card_map):
    if len(card_map.items()) == 5:
        return high_card
    if len(card_map.items()) == 4:
        return one_pair
    if len(card_map.items()) == 3:
        if any(elem == 3 for elem in card_map.values()):
            return three_of_a_kind
        return two_pair
    if len(card_map.items()) == 2:
        if any(elem == 4 for elem in card_map.values()):
            return four_of_a_kind
        return full_house
    return five_of_a_kind
