def sum_set(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def get_divisors(number):
    divisors = []
    divisor = 1
    while divisor <= number // 2:
        if number % divisor == 0:
            divisors.append(divisor)
        divisor += 1
    return divisors

def process_interval_2(min_value, max_value, invalid_ids, all_divisors):
    if min_value > max_value:
        return
    min_value_length = len(str(min_value))
    divisors = get_divisors(min_value_length) if all_divisors else ([] if min_value_length % 2 == 1 else [min_value_length // 2])
    for divisor in divisors:
        first_chunk = int(str(min_value)[:divisor])
        number_to_check = int(str(first_chunk) * (min_value_length // divisor))
        while number_to_check <= max_value:
            if min_value <= number_to_check:
                invalid_ids.add(number_to_check)
            first_chunk_length = len(str(first_chunk))
            first_chunk += 1
            if first_chunk_length != len(str(first_chunk)):
                break
            number_to_check = int(str(first_chunk) * (min_value_length // divisor))
    process_interval_2(pow(10, min_value_length), max_value, invalid_ids, all_divisors)

invalid_ids_1 = set()
invalid_ids_2 = set()
with open("input.txt", "r") as file:
    for line in file:
        ranges = line.split(",")
        for range in ranges:
            rangeElements = range.split("-")
            process_interval_2(int(rangeElements[0]), int(rangeElements[1]), invalid_ids_1, False)
            process_interval_2(int(rangeElements[0]), int(rangeElements[1]), invalid_ids_2, True)


print(sum_set(invalid_ids_1))
print(sum_set(invalid_ids_2))
