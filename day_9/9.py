import math

mappings= {
    "U" : [0, 1],
    "D" : [0, -1],
    "R" : [1, 0],
    "L" : [-1, 0],
}


def main():

    rope1 = make_rope()
    rope2 = make_rope(10)

    traversed1 = set()
    traversed2 = set()

    instructions = []
    with open("9.txt") as file:
        for line in file:
            direction, steps = line.strip().split(" ")
            instructions.append({"direction" : direction, "steps" : int(steps)})
    
    for instruction in instructions:
        move_rope(instruction, rope1, traversed1)
        move_rope(instruction, rope2, traversed2)
  
    print(len(traversed1))
    print(len(traversed2))


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_rope(length=2):
    rope = []
    for _ in range(length):
        rope.append(Coords(0, 0))
    return rope


def move_rope(instruction, rope, t):
    for _ in range(instruction["steps"]):
        rope[0].x += mappings[instruction["direction"]][0]
        rope[0].y += mappings[instruction["direction"]][1]

        for i in range(1, len(rope)):
            move_knot(rope[i - 1], rope[i])

        t.add(pos_to_str(rope[len(rope) - 1]))


def move_knot(previous, this):
    x_dif = previous.x - this.x
    y_dif = previous.y - this.y

    if abs(x_dif) > 1 or abs(y_dif) > 1:
        if x_dif > 0:
            this.x += math.ceil(x_dif / 2)
        else:
            this.x += math.floor(x_dif / 2)
        if y_dif > 0:
            this.y += math.ceil(y_dif / 2)
        else:
            this.y += math.floor(y_dif / 2)


def pos_to_str(tail):
    return f"{tail.x}{tail.y}"


if __name__ == "__main__":
    main()