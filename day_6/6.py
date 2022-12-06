def main():

    with open("6.txt") as file:
        stream = file.readline().strip()
        part1 = find_marker(stream, 4)
        part2 = find_marker(stream, 14)

    print(part1, part2)


def find_marker(s, length):
    for i in range(len(s) - length):
        packet = s[i:i + length]
        if length == len(set(packet)):
            return i + length


if __name__ == "__main__":
    main()