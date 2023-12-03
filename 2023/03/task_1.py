class NumberMatch:
    def __init__(self, row, start, end, value):
        self.row = row
        self.start = start
        self.end = end
        self.value = value


def has_symbol_around(number_match):
    lines_to_check = [number_match.row]
    if number_match.row != 0:
        lines_to_check.append(number_match.row - 1)
    if number_match.row != line_index:
        lines_to_check.append(number_match.row + 1)
    for line in lines_to_check:
        if line not in symbols:
            continue
        currentSymbols = symbols[line]
        for currentSymbol in currentSymbols:
            if number_match.start - 1 <= currentSymbol <= number_match.end:
                return True
    return False



number_matches = []
symbols = {}
line_index = 0
for line in open("input.txt", "r"):
    current_number = []
    current_number_start = 0
    char_count = 0
    for char in line.strip():
        if char.isnumeric():
            if len(current_number) == 0:
                current_number_start = char_count
            current_number.append(char)
        else:
            if len(current_number) != 0:
                number_matches.append(NumberMatch(line_index, current_number_start, char_count, int(''.join(current_number))))
                current_number.clear()

            if char != '.':
                if line_index not in symbols:
                    symbols[line_index] = [char_count]
                else:
                    symbols[line_index].append(char_count)
        char_count += 1
    if len(current_number) != 0:
        number_matches.append(NumberMatch(line_index, current_number_start, char_count, int(''.join(current_number))))
    line_index += 1

result = 0
for number_match in number_matches:
    if has_symbol_around(number_match):
        result += number_match.value

print(result)
