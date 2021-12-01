with open ("input.txt", "r") as f:
    prev_num = None
    counter = 0

    for num in f.readlines():
        num = int(num)

        if not prev_num == None:
            if num > prev_num:
                counter += 1

        prev_num = num


    print(f"Depth increased {counter} times")
