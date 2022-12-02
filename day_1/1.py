with open("1.txt") as file:
    elves = []
    elf = 0
    for line in file:
        line = line.strip()
        if line:
            elf += int(line)
        else:
            elves.append(elf)
            elf = 0
            
elves = sorted(elves, reverse=True)
print(elves[0])
print(sum(elves[0:3]))