def aggregate_numbers(numbers, operation):
    result = numbers[0]
    for number in numbers[1:]:
        if operation == "+":
            result += number
        else:
            result *= number
    return result


def process_matrix(map_matrix, operations):
    result = 0
    column_index = 0
    while len(operations) > column_index:
        row_index = 0
        section_sum = int(map_matrix[0][column_index])
        while len(map_matrix) - 1 > row_index:
            if operations[column_index] == "+":
                section_sum += int(map_matrix[row_index + 1][column_index])
            else:
                section_sum *= int(map_matrix[row_index + 1][column_index])
            row_index += 1
        result += section_sum
        column_index += 1
    return result


def process_matrix_2(matrix, max_line_length):
    result = 0
    column_index = 0
    operation = None
    numbers = []
    while column_index < max_line_length:
        number_digits = []
        is_separator = True
        row_index = 0
        while row_index < len(matrix):
            current_line = matrix[row_index]
            if len(current_line) <= column_index:
                row_index += 1
                continue
            current_char = current_line[column_index]
            if not current_char.isspace():
                is_separator = False
            if current_char.isdigit():
                number_digits.append(current_char)
            elif current_char == "+" or current_char == "*":
                operation = current_char
            row_index += 1
        if len(number_digits) > 0:
            numbers.append(int("".join(number_digits)))
        if is_separator:
            result += aggregate_numbers(numbers, operation)
            numbers = []
            operation = None
        column_index += 1
    return result


def process_input_1():
    with open("input.txt", "r") as file:
        matrix = []
        operations = []
        for line in file:
            row = []
            for data in line.split():
                if data == "+" or data == "*":
                    operations.append(data)
                else:
                    row.append(data)
            if len(row) > 0:
                matrix.append(row)
        return matrix, operations


def process_input_2():
    max_length = 0
    with open("input.txt", "r") as file:
        matrix = []
        for line in file:
            matrix.append(line)
            if len(line) > max_length:
                max_length = len(line)
    return matrix, max_length


(number_matrix_1, operations_1) = process_input_1()
print(process_matrix(number_matrix_1, operations_1))

(number_matrix_2, max_length_2) = process_input_2()
print(process_matrix_2(number_matrix_2, max_length_2))
