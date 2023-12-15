def calculate_hash(item):
    current_value = 0
    for current_char in item:
        current_value = ((current_value + ord(current_char)) * 17) % 256
    return current_value


with open("input.txt", "r") as file:
    instructions = file.readline().strip().split(",")

print(sum(map(calculate_hash, instructions)))