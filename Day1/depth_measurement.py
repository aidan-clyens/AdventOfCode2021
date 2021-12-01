def part2():
    data = []

    with open("input.txt", "r") as f:
        data = [int(num) for num in f.readlines()]


    prev_sliding_window = None
    counter = 0
    for i in range(len(data) - 2):
        sliding_window = data[i] + data[i+1] + data[i+2]
        
        if not prev_sliding_window == None:
            if sliding_window > prev_sliding_window:
                counter += 1

        prev_sliding_window = sliding_window

    print(f"Depth increased {counter} times")



def part1():
    with open("input.txt", "r") as f:
        prev_num = None
        counter = 0

        for num in f.readlines():
            num = int(num)

            if not prev_num == None:
                if num > prev_num:
                    counter += 1

            prev_num = num


        print(f"Depth increased {counter} times")


if __name__ == "__main__":
    print("Part 1:")
    part1()

    print("Part 2:")
    part2()
