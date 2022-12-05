with open("4.txt") as file:
    answer1 = 0
    answer2 = 0
    for line in file:
        assignments = line.strip().split(",")
        sections = []
        for assignment in assignments:
            x, y = assignment.split("-")
            r = range(int(x), int(y) + 1)
            sections.append(list(r))

        if all(item in sections[0] for item in sections[1]) or all(item in sections[1] for item in sections[0]):
            answer1 += 1
            answer2 += 1
        elif any(item in sections[0] for item in sections[1]):
            answer2 += 1

print(answer1, answer2)