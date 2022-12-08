def main():

    root = Node("/", "folder", None)

    with open("7.txt") as file:
        make_tree(file, root)

    totals = []
    while True:
        leaves = get_all_leaves(root)
        if not get_totals(leaves, totals):
            break

    # Part 1
    print(sum([x for x in totals if x <= 100000]))

    # Part 2
    totals.sort()
    unused_space = 70000000 - totals[len(totals) - 1]
    to_free = 30000000 - unused_space

    large_folders = [x for x in totals if x >= to_free]
    print(large_folders[0])


def make_tree(f, current_node):

    for line in f:
        if line.startswith("$ c"):
            name = line.strip().replace("$ cd ", "")
            if name == "..":
                current_node = current_node.parent
            else:
                for child in current_node.children:
                    if child.name == name:
                        current_node = child
                        break
        elif not line.startswith("$"):
            line = line.strip().split(" ")
            if line[0] == "dir":
                node = Node(line[1], "folder", current_node)
            else:
                node = Node(line[1], "file", current_node, int(line[0]))
            
            current_node.children.append(node)


def get_all_leaves(root):

    leaves = []
    current_nodes = [root]
    while True:
        new_nodes = []
        for node in current_nodes:
            children = node.children
            if children:
                new_nodes += children
            else:
                leaves.append(node)
        
        if not new_nodes:
            return leaves
        else:
            current_nodes = new_nodes


def get_totals(leaves, totals):
    for leaf in leaves:
        if leaf.type == "folder":
            totals.append(leaf.size)
        if leaf.parent:
            leaf.parent.size += leaf.size
            leaf.parent.children.remove(leaf)
        else:
            return False

    return True


class Node:
    def __init__(self, name, type, parent, size=0):
        self.name = name
        self.size = size
        self.type = type
        self.parent = parent
        self.children = []


if __name__ == "__main__":
    main()