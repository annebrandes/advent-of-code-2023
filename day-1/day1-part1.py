with open("day1-text.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        right_number = next((char for char in line if char.isdigit()), None)
        left_number = next((char for char in reversed(line) if char.isdigit()), None)
        string_local_sum = str(right_number) + str(left_number)
        local_sum = int(string_local_sum)
        sum += local_sum
    print(sum)