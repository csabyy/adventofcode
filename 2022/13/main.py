import re


def get_array_index(row):
    start_index_count = 0
    for idx, char in enumerate(row):
        if char == '[':
            start_index_count += 1
        elif char == ']':
            start_index_count -= 1
            if start_index_count == -1:
                return idx


def process_line_rec(row, current_array):
    if len(row) == 0:
        return current_array
    if row[0] == '[':
        end_index = get_array_index(row[0 + 1:])
        current_array.append(process_line_rec(row[1:end_index+1], []))
        return process_line_rec(row[end_index+1:len(row)], current_array)
    current_number = re.findall("^\\d+", row)
    if len(current_number) > 0:
        current_array.append(int(current_number[0]))
        return process_line_rec(row[len(current_number[0]):len(row)], current_array)
    return process_line_rec(row[1:len(row)], current_array)


def compare_packets_rec(packet_a, packet_b):
    if len(packet_a) == 0:
        if len(packet_b) > 0:
            return True
        if len(packet_b) == 0:
            return None
    if len(packet_b) == 0:
        return False
    if type(packet_a[0]) == int:
        if type(packet_b[0]) == int:
            if packet_a[0] < packet_b[0]:
                return True
            elif packet_a[0] > packet_b[0]:
                return False
            else:
                return compare_packets_rec(packet_a[1:], packet_b[1:])
        new_packet_a = [[packet_a[0]]] + packet_a[1:]
        new_packet_b = packet_b
    elif type(packet_b[0]) == int:
        new_packet_a = packet_a
        new_packet_b = [[packet_b[0]]] + packet_b[1:]
    else:
        new_packet_a = packet_a[0]
        new_packet_b = packet_b[0]
    comp_arr = compare_packets_rec(new_packet_a, new_packet_b)
    if comp_arr is not None:
        return comp_arr
    return compare_packets_rec(packet_a[1:], packet_b[1:])


def find_packet_location(packets, packet):
    counter = 0
    for packets_pair in packets:
        for p in packets_pair:
            if compare_packets_rec(p, packet):
                counter += 1
    return counter


def count_pairs(packets):
    sum_match = 0
    for idx, p in enumerate(packets):
        if compare_packets_rec(p[0], p[1]):
            sum_match += idx + 1
    return sum_match


packets = []
packets_pair = []
packets.append(packets_pair)
for data in open("input.txt", "r"):
    line = data.strip()
    if line:
        packets_pair.append(process_line_rec(line[1:len(line)-1], []))
    else:
        packets_pair = []
        packets.append(packets_pair)


print(count_pairs(packets))
print((find_packet_location(packets, [[2]]) + 1) * (find_packet_location(packets, [[6]]) + 2))
