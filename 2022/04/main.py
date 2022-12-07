def contains(elf_one_start, elf_one_end, elf_two_start, elf_two_end):
    return elf_one_start <= elf_two_start and elf_two_end <= elf_one_end or \
           elf_two_start <= elf_one_start and elf_one_end <= elf_two_end


def overlaps(elf_one_start, elf_one_end, elf_two_start, elf_two_end):
    return elf_one_start <= elf_two_start <= elf_one_end or \
           elf_two_start <= elf_one_start <= elf_two_end


def split_section(elf):
    section = elf.split('-')
    elf_start = int(section[0])
    elf_end = int(section[1])
    return elf_start, elf_end


total = 0
total2 = 0
for data in open("input.txt", "r"):
    group = data.strip().split(',')
    elf_1_start, elf_1_end = split_section(group[0])
    elf_2_start, elf_2_end = split_section(group[1])
    total += 1 if contains(elf_1_start, elf_1_end, elf_2_start, elf_2_end) else 0
    total2 += 1 if overlaps(elf_1_start, elf_1_end, elf_2_start, elf_2_end) else 0

print(total)
print(total2)
