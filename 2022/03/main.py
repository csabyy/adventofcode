def process_character(char):
    if ord(char) < ord('a'):
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1


def build_set(text):
    visited_items = set()
    for character in text:
        visited_items.add(character)
    return visited_items


def reduce_set(dictionary, text):
    reduced_set = set()
    for character in text:
        if character in dictionary:
            reduced_set.add(character)
    return reduced_set


def process_n_chunks_rec(reduced_set, lines):
    if not lines:
        return reduced_set
    reduced_set = reduce_set(reduced_set, lines[0])
    return process_n_chunks_rec(reduced_set, lines[1:])


def process_n_chunks(lines):
    visited_items = build_set(lines[0])
    reduced_set = process_n_chunks_rec(visited_items, lines[1:])
    return list(reduced_set)[0]


total = 0
total2 = 0
rows = []
for data in open("input.txt", "r"):
    row = data.strip()
    half_length = int(len(row) / 2)
    total += process_character(process_n_chunks([row[:half_length], row[half_length:]]))
    rows.append(row)
    if len(rows) % 3 == 0:
        total2 += process_character(process_n_chunks(rows))
        rows.clear()

print(total)
print(total2)
