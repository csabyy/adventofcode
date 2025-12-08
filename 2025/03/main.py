def process_line(line, required_digits):
    if required_digits == 0:
        return 0

    max_number = 0
    max_index = 0
    trimmed_line = line.strip()

    for index, char in enumerate(trimmed_line[:len(trimmed_line) - required_digits + 1]):
        current = int(char)
        if current > max_number:
            max_number = current
            max_index = index
    return max_number * pow(10, required_digits - 1) + process_line(line[(max_index + 1):], required_digits - 1)

result1 = 0
result2 = 0
with open("input.txt", "r") as file:
    for line in file:
        result1 += process_line(line, 2)
        result2 += process_line(line, 12)

print(result1)
print(result2)