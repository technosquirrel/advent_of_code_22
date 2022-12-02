scores = {
    "A X": [4, 3],
    "A Y": [8, 4],
    "A Z": [3, 8],
    "B X": [1, 1],
    "B Y": [5, 5],
    "B Z": [9, 9],
    "C X": [7, 2],
    "C Y": [2, 6],
    "C Z": [6, 7],
}

total1 = 0
total2 = 0

with open("2.txt") as file:
    for line in file:
        line = line.strip()
        total1 += scores[line][0]
        total2 += scores[line][1]

# Part one solution
print(total1)
# Part two solution
print(total2)
