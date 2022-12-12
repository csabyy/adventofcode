from heapq import heappop, heappush
from enum import Enum


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4


class Tree:
    def __init__(self, size, row_index, column_index):
        self.size = size
        self.row_index = row_index
        self.column_index = column_index
        self.is_visible = False
        self.score = 1
        self.scores_counter = 0

    def __lt__(self, other):
        return self.size < other.size


visible_counter = 0
max_score = 0


def set_visible(tree):
    global visible_counter
    if not tree.is_visible:
        visible_counter += 1
        tree.is_visible = True


def set_score(tree, score):
    global max_score
    tree.scores_counter += 1
    tree.score *= score
    if tree.scores_counter == 4:
        max_score = max(max_score, tree.score)


def get_relevant_index(tree, direction):
    if direction == Direction.TOP or direction == Direction.BOTTOM:
        return tree.row_index
    return tree.column_index


def get_visible_tree_score(tree, length, direction):
    if direction == Direction.RIGHT or direction == Direction.BOTTOM:
        return length - 1 - get_relevant_index(tree, direction)
    return get_relevant_index(tree, direction)


def rearrange_heap(visible_candidates, current_tree, direction):
    while len(visible_candidates) > 0 and current_tree.size >= visible_candidates[0].size:
        tree_to_remove = heappop(visible_candidates)
        score = abs(get_relevant_index(tree_to_remove, direction) - get_relevant_index(current_tree, direction))
        set_score(tree_to_remove, score)
    heappush(visible_candidates, current_tree)


def process_result(visible_trees, length, direction):
    for visible_tree in visible_trees:
        set_visible(visible_tree)
        set_score(visible_tree, get_visible_tree_score(visible_tree, length, direction))


def walk_forest():
    matrix_length = len(forest)
    bottom_visible_trees = [[] for _ in range(matrix_length)]
    top_visible_trees = [[] for _ in range(matrix_length)]
    row_counter = 0
    while row_counter < matrix_length:
        row = forest[row_counter]
        column_counter = 0
        reverse_row_counter = matrix_length - row_counter - 1
        right_row = []
        left_row = []
        while column_counter < len(row):
            reverse_col_counter = len(row) - column_counter - 1
            current_tree = forest[row_counter][column_counter]
            current_tree_rev = forest[reverse_row_counter][reverse_col_counter]

            rearrange_heap(top_visible_trees[reverse_col_counter], current_tree_rev, Direction.TOP)
            rearrange_heap(left_row, current_tree_rev, Direction.LEFT)
            rearrange_heap(bottom_visible_trees[column_counter], current_tree, Direction.BOTTOM)
            rearrange_heap(right_row, current_tree, Direction.RIGHT)

            column_counter += 1
        row_counter += 1
        process_result(left_row, len(row), Direction.LEFT)
        process_result(right_row, len(row), Direction.RIGHT)
    for top_visible_tree_col in top_visible_trees:
        process_result(top_visible_tree_col, matrix_length, Direction.TOP)
    for bottom_visible_tree_col in bottom_visible_trees:
        process_result(bottom_visible_tree_col, matrix_length, Direction.BOTTOM)


forest = []
for row_index, data in enumerate(open("input.txt", "r")):
    forest_row = []
    for column_index, size in enumerate([*data.strip()]):
        forest_row.append(Tree(int(size), row_index, column_index))
    forest.append(forest_row)

walk_forest()
print(visible_counter)
print(max_score)

