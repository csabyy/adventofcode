class NumberMatch:
    def __init__(self, row, start, end, value):
        self.row = row
        self.start = start
        self.end = end
        self.value = value
class SymbolMatch:
    def __init__(self, position, value):
        self.position = position
        self.value = value


star_matches = {}
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
                    symbols[line_index] = [SymbolMatch(char_count, char)]
                else:
                    symbols[line_index].append(SymbolMatch(char_count, char))
        char_count += 1
    if len(current_number) != 0:
        number_matches.append(NumberMatch(line_index, current_number_start, char_count, int(''.join(current_number))))
    line_index += 1

for number_match in number_matches:
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
            if number_match.start - 1 <= currentSymbol.position <= number_match.end and currentSymbol.value == "*":
                hash = currentSymbol.__hash__()
                if hash in star_matches:
                    star_matches[hash].append(number_match.value)
                else:
                    star_matches[hash] = [number_match.value]

result = 0
for star_match in star_matches.values():
    if len(star_match) == 2:
        result += star_match[0] * star_match[1]

print(result)
