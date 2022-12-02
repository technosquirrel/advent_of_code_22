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

# Part one solution
print(elves[0])
# Part two solution
print(sum(elves[0:3]))
