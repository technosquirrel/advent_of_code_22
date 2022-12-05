def main():

    with open("3.txt") as file:
        total1 = 0
        total2 = 0
        i = 0
        bags = []

        for line in file:
            line = line.strip()

           # Part 1
            split = len(line) // 2
            dupe1 = [c for c in line[:split] if c in line[split:]]
            total1 += find_priority(dupe1[0])

            # Part2
            bags.append(line)
            if i < 2:
                i += 1
            else:
                dupe2 = [c for c in bags[0] if c in bags[1] and c in bags[2]]
                total2 += find_priority(dupe2[0])
                bags = []
                i = 0

    print(total1)
    print(total2)

def find_priority(c):
    x = ord(c)
    if c.isupper():
        return x - 38
    else:
        return x - 96


if __name__ == "__main__":
    main()