def number_of_jumps(letters, line, window_max, window_min):
    jumps = 0
    index = window_max
    while index > (window_min + jumps):
        letter = line[index]
        if letter in letters:
            dictionary_letter_position = letters[letter]
            if dictionary_letter_position > index:
                return index - window_min
            if index > dictionary_letter_position > window_min:
                jumps = dictionary_letter_position - window_min
        letters[letter] = index
        index -= 1
    return jumps


def process_line(line, window_size):
    window_max = window_size - 1
    letters = {}
    while window_max < len(line):
        jumps = number_of_jumps(letters, line, window_max, window_max - window_size)
        if jumps == 0:
            return window_max
        window_max += jumps
    return 0


for data in open("input.txt", "r"):
    print(process_line(data.strip(), 4) + 1)
    print(process_line(data.strip(), 14) + 1)
