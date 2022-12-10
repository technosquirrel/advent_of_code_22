cycle = 1
x = 1
y = 1
signal_strengths_total = 0
screen = []

with open("10.txt") as file:
    for line in file:            
        if line.startswith("n"):
            i = 1
        else:
            i = 2
        for _ in range(i):
            if (cycle + 20) % 40 == 0:
                signal_strengths_total += x * cycle
            elif (cycle - 1) % 40 == 0:
                if y != 1:
                    y += 40

            if y - 1 <= cycle - 1 <= y + 1:
                screen.append("#")
            else:
                screen.append(".")
            cycle += 1

        if i == 2:
            _, n = line.strip().split(" ")
            x += int(n)
            y += int(n)          

print(signal_strengths_total)
for i in range(len(screen)):
    print(screen[i], end="")
    if (i + 1) % 40 == 0:
        print()