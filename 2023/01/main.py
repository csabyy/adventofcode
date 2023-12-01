numbers_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def get_first_number(line, reverse):
   chunk = ''
   for char in line:
      if char.isnumeric():
       return int(char)
      else:
         chunk = char + chunk if reverse else chunk + char
         for dictItem in numbers_dict.items():
            if dictItem[0] in chunk:
               return dictItem[1]
   return 0


total = 0
for data in open("input.txt", "r"):
   total += get_first_number(data, False) * 10 + get_first_number(data[::-1], True)


print(total)
