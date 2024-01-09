class Expression:
    def __init__(self, is_less_than, key_to_compare, value_to_compare):
        self.is_less_than = is_less_than
        self.key_to_compare = key_to_compare
        self.value_to_compare = value_to_compare


def negate_expression(expression):
    return Expression(not expression.is_less_than,
                      expression.key_to_compare,
                      expression.value_to_compare - 1 if expression.is_less_than else expression.value_to_compare + 1)


def parse_condition(condition_raw):
    is_less_than = False
    split_index = condition_raw.find(">")
    if split_index == -1:
        split_index = condition_raw.find("<")
        is_less_than = True
    key_to_compare = condition_raw[:split_index]
    value_to_compare = int(condition_raw[split_index + 1:])
    return Expression(is_less_than, key_to_compare, value_to_compare)


def parse_workflow_payload(workflow_payload_raw):
    condition_end_index = workflow_payload_raw.find(":")
    if condition_end_index == -1:
        return workflow_payload_raw
    condition = parse_condition(workflow_payload_raw[:condition_end_index])
    condition_true_expression_index = workflow_payload_raw.find(",")
    condition_true = workflow_payload_raw[condition_end_index + 1:condition_true_expression_index]
    condition_else_expression = parse_workflow_payload(workflow_payload_raw[condition_true_expression_index + 1:])
    return condition, condition_true, condition_else_expression


def parse_workflow(workflow_raw):
    key_end_index = workflow_raw.index("{")
    workflow_key = workflow_raw[:key_end_index]
    workflow_payload = parse_workflow_payload(workflow_raw[key_end_index + 1:-1])
    return workflow_key, workflow_payload


def parse_ratings(ratings_raw):
    rating_items = ratings_raw[1:-1].split(",")
    current_item = {}
    for rating_item in rating_items:
        rating_item_parts = rating_item.split("=")
        current_item[rating_item_parts[0]] = int(rating_item_parts[1])
    return current_item


should_populate_workflows = True
workflows = {}
ratings = []
with open("input.txt", "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            should_populate_workflows = False
            continue
        if should_populate_workflows:
            parsed_workflow = parse_workflow(line.strip())
            workflows[parsed_workflow[0]] = parsed_workflow[1]
        else:
            ratings.append(parse_ratings(line.strip()))


def create_optimised_tree_rec(current_workflow_item, condition_accumulator, results):
    condition = current_workflow_item[0]
    true_branch = current_workflow_item[1]
    false_branch = current_workflow_item[2]

    if true_branch == "A":
        results.append(condition_accumulator + [condition])
    if false_branch == "A":
        results.append(condition_accumulator + [negate_expression(condition)])
    if true_branch == "A" and false_branch == "A":
        return "A"
    if true_branch == "R" and false_branch == "R":
        return "R"

    if true_branch != "A" and true_branch != "R":
        workflow_item = true_branch if type(true_branch) == tuple else workflows[true_branch]
        true_branch = create_optimised_tree_rec(workflow_item, condition_accumulator + [condition], results)

    if false_branch != "A" and false_branch != "R":
        workflow_item = false_branch if type(false_branch) == tuple else workflows[false_branch]
        false_branch = create_optimised_tree_rec(workflow_item, condition_accumulator + [negate_expression(condition)],
                                                 results)

    return condition, None if (not true_branch or true_branch == "R") else true_branch, None if (
            not false_branch or false_branch == "R") else false_branch


def process_rating(current_workflow_item, current_rating):
    if type(current_workflow_item) != tuple:
        current_item = current_workflow_item
        if current_item == "A":
            return True
        if current_item == "R":
            return False
        return process_rating(workflows[current_item], current_rating)
    if len(current_workflow_item) == 3:
        condition = current_workflow_item[0]
        actual_rating = current_rating[condition.key_to_compare]
        other_rating = condition.value_to_compare
        result = actual_rating < other_rating if condition.is_less_than else actual_rating > other_rating
        if result:
            return process_rating(current_workflow_item[1], current_rating)
        return process_rating(current_workflow_item[2], current_rating)


def get_rating_value(rating):
    return sum(rating.values())


result = 0
for current_rating in ratings:
    if process_rating(workflows["in"], current_rating):
        result += get_rating_value(current_rating)
print(result)

expressions_list = []
create_optimised_tree_rec(workflows["in"], [], expressions_list)


def get_result(min_value, max_value):
    merged_map_list = []
    for expressions in expressions_list:
        merged_map = {}
        for expression in expressions:
            if expression.key_to_compare in merged_map:
                current_min, current_max = merged_map[expression.key_to_compare]
                if expression.is_less_than:
                    merged_map[expression.key_to_compare] = (
                        current_min, min(current_max, expression.value_to_compare - 1))
                else:
                    merged_map[expression.key_to_compare] = (max(current_min, expression.value_to_compare), current_max)
            else:
                if expression.is_less_than:
                    merged_map[expression.key_to_compare] = (min_value, expression.value_to_compare - 1)
                else:
                    merged_map[expression.key_to_compare] = (expression.value_to_compare, max_value)
        merged_map_list.append(merged_map)
    return merged_map_list


result_list = get_result(0, 4_000)

letters = ["x", "m", "a", "s"]
r = 0
for result in result_list:
    combinations = 1
    for letter in letters:
        if letter in result:
            letter_min, letter_max = result[letter]
            combinations *= (letter_max - letter_min)
        else:
            combinations *= 4000
    r += combinations

print(r)
