import math
import re

time = 0
distance = 0
with open("input.txt", "r") as file:
    time = int("".join(re.findall("\\d+", file.readline())))
    distance = int("".join(re.findall("\\d+", file.readline())))

temp = math.sqrt(math.pow(time, 2) - 4 * distance)
x1 = (time + temp) / 2
x2 = (time - temp) / 2

result = math.floor(max(x1, x2)) - math.ceil(min(x1, x2)) + 1

print(result)
