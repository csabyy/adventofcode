class Expression:
    def __init__(self, is_less_than, key_to_compare, value_to_compare):
        self.is_less_than = is_less_than
        self.key_to_compare = key_to_compare
        self.value_to_compare = value_to_compare


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
