import sys


class Folder:
    def __init__(self, parent, children, size):
        self.parent = parent
        self.children = children
        self.size = size


root = Folder(None, {}, 0)
current_folder = root


def update_size(folder, size):
    folder.size += size
    if folder.parent is not None:
        update_size(folder.parent, size)


def process_ls(row_props):
    name = row_props[1]
    if row_props[0] == "dir":
        current_folder.children[name] = Folder(current_folder, {}, 0)
    else:
        size = int(row_props[0])
        update_size(current_folder, size)


def process_cd(dir_to_navigate):
    if dir_to_navigate == "/":
        return root
    if dir_to_navigate == "..":
        return current_folder.parent
    return current_folder.children[dir_to_navigate]


def sum_size(folder, limit):
    folder_size_sum = 0
    if folder.size < limit:
        folder_size_sum += folder.size
    for sub_folder in folder.children.values():
        folder_size_sum += sum_size(sub_folder, limit)
    return folder_size_sum


def folder_size_to_delete(folder, extra_space_needed):
    minimum_dir_size = sys.maxsize
    if folder.size >= extra_space_needed:
        minimum_dir_size = min(minimum_dir_size, folder.size)
        for sub_folder in folder.children.values():
            minimum_dir_size = min(minimum_dir_size, folder_size_to_delete(sub_folder, extra_space_needed))
    return minimum_dir_size


is_processing_ls = False
for data in open("input.txt", "r"):
    tokens = data.strip().split(' ')
    if tokens[0] == "$" and tokens[1] == "ls":
        is_processing_ls = True
    elif tokens[0] == "$" and tokens[1] == "cd":
        is_processing_ls = False
        current_folder = process_cd(tokens[2])
    elif is_processing_ls:
        process_ls(tokens)


print(sum_size(root, 100000))
print(folder_size_to_delete(root, root.size + 30000000 - 70000000))
