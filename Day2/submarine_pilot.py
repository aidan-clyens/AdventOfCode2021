def part2(data):
    depth = 0
    pos = 0
    aim = 0

    for line in data:
        direction = line[0]
        val = int(line[1])

        if direction == "forward":
            pos += val
            depth += aim * val
        elif direction == "up":
            aim -= val
        elif direction == "down":
            aim += val

    return depth * pos


def part1(data):
    depth = 0
    pos = 0

    for line in data:
        direction = line[0]
        val = int(line[1])

        if direction == "forward":
            pos += val
        elif direction == "up":
            depth -= val
        elif direction == "down":
            depth += val

    return depth * pos


if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        data = [line.split() for line in f.readlines()]


    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

