def part1(data):
    gamma_rate = [0] * len(data[0])

    for num in data:
        num = [int(c) for c in num]
        
        for i in range(len(gamma_rate)):
            gamma_rate[i] += num[i]

    gamma_rate = "".join([str(round(num / len(data))) for num in gamma_rate])
    epsilon_rate = "".join(str(1 - int(c)) for c in gamma_rate)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line[:-1]
            data.append(line)

    print(f"Part 1: {part1(data)}")
