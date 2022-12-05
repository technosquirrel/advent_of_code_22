def main():

    with open("5.txt") as file:
        
        lines = file.readlines()
        stop = lines.index("\n") - 1
        stacks1 = parse_crates(lines[:stop])
        stacks2 = [x.copy() for x in stacks1]

        for line in lines[stop + 2:]:
            move_crates_1(line, stacks1)
            move_crates_2(line, stacks2)

        print_result(stacks1)
        print_result(stacks2)


def move_crates_1(instruction, stacks):

    n, x, y = parse_instruction(instruction)

    for _ in range(n):
        index = len(stacks[x]) - 1
        stacks[y].append(stacks[x][index])
        stacks[x].pop(index)


def move_crates_2(instruction, stacks):

    n, x, y = parse_instruction(instruction)

    for i in range(n, 0, -1):
        index = len(stacks[x]) - i
        stacks[y].append(stacks[x][index])

    stacks[x] = stacks[x][: -n]


def parse_crates(input):

    stacks = []
    
    for _ in range(len(input[0]) // 4):
        stacks.append([])

    for line in input:
        for i in range(1, len(line), 4):
            if not line[i].isspace():
                stack = (i - 1) // 4
                stacks[stack].append(line[i])

    for stack in stacks:
        stack.reverse()

    return stacks


def parse_instruction(line):

    split = line.strip().split(" ")
    n = int(split[1])
    x = int(split[3]) - 1
    y = int(split[5]) - 1

    return n, x, y


def print_result(list):
    for stack in list:
        print(stack[len(stack) - 1], end="")
    print()


if __name__ == "__main__":
    main()