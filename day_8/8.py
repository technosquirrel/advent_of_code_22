from numpy import prod

def main():

    forest = []
    with open("8.txt") as file:
        populate_forest(forest, file)

    # Part 1
    check_forest(forest)
    total_seen = count_trees(forest)

    print(total_seen)

    # Part 2
    highest_score = 0

    for i in range(len(forest)):
        for j in range(len(forest[0])):
            highest_score = calculate_score(i, j, forest[i][j].height, forest, highest_score)

    print(highest_score)


def populate_forest(forest, f):
     
    for line in f:
        trees = []
        for x in line.strip():
            trees.append(Tree(int(x)))
        forest.append(trees)


def check_tree(tallest_tree, tree):
    if tree.height > tallest_tree:
        tree.seen = True
        return tree.height
    else:
        return tallest_tree


def check_forest(forest):

    # Check left -> right and right -> left
    for i in range(len(forest)):
        tallest_tree_left = -1
        tallest_tree_right = - 1
        for j in range(len(forest[0])):
            tallest_tree_left = check_tree(tallest_tree_left, forest[i][j])
            tallest_tree_right = check_tree(tallest_tree_right, forest[i][len(forest[0]) - 1 - j])
    
    # Check top -> bottom and bottom -> top
    for j in range(len(forest[0])):
        tallest_tree_top = -1
        tallest_tree_bottom = -1
        for i in range(len(forest)):
            tallest_tree_top = check_tree(tallest_tree_top, forest[i][j])
            tallest_tree_bottom = check_tree(tallest_tree_bottom, forest[len(forest) - 1 - i][j])


def count_trees(forest):
    total = 0
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if forest[i][j].seen:
                total += 1

    return total


def calculate_score(i, j, height, forest, highest_score):
    
    score = [0, 0, 0, 0]

    tracker = j
    stop = False
    while tracker > 0 and not stop:
        tracker = tracker - 1
        score[0] += 1
        if forest[i][tracker].height >= height:
            stop = True

    tracker = j
    stop = False
    while tracker < len(forest[0]) - 1 and not stop:
        tracker = tracker + 1
        score[1] += 1
        if forest[i][tracker].height >= height:
            stop = True

    tracker = i
    stop = False
    while tracker > 0 and not stop:
        tracker = tracker - 1
        score[2] += 1
        if forest[tracker][j].height >= height:
            stop = True

    tracker = i
    stop = False
    while tracker < len(forest) - 1 and not stop:
        tracker = tracker + 1
        score[3] += 1
        if forest[tracker][j].height >= height:
            stop = True

    total = prod(score)

    if total > highest_score:
        return total
    else:
        return highest_score


class Tree:
    def __init__(self, height):
        self.height = height
        self.seen = False


if __name__ == "__main__":
    main()