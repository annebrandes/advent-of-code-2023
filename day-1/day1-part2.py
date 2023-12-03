with open("day1-text.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        for index, char in enumerate(line): 
            if char == "o":
                if line[index:index+3] == "one":
                    right_number = 1
                    break
            if char == "t":
                if line[index:index+3] == "two":
                    right_number = 2
                    break
                if line[index:index+5] == "three":
                    right_number = 3
                    break
            if char == "f":
                if line[index:index+4] == "four":
                    right_number = 4
                    break
                if line[index:index+4] == "five":
                    right_number = 5
                    break
            if char == "s":
                if line[index:index+3] == "six":
                    right_number = 6
                    break
                if line[index:index+5] == "seven":
                    right_number = 7
                    break
            if char == "e":
                if line[index:index+5] == "eight":
                    right_number = 8
                    break
            if char == "n":
                if line[index:index+4] == "nine":
                    right_number = 9
                    break
            if char.isdigit():
                right_number = char
                break
        for index, char in enumerate(line[::-1]):
            if char == "e":
                if line[::-1][index:index+3] == "eno":
                    left_number = 1
                    break
                if line[::-1][index:index+5] == "eerht":
                    left_number = 3
                    break
                if line[::-1][index:index+4] == "evif":
                    left_number = 5
                    break
                if line[::-1][index:index+4] == "enin":
                    left_number = 9
                    break
            if char == "o":
                if line[::-1][index:index+3] == "owt":
                    left_number = 2
                    break
            if char == "r":
                if line[::-1][index:index+4] == "ruof":
                    left_number = 4
                    break
            if char == "x":
                if line[::-1][index:index+3] == "xis":
                    left_number = 6
                    break
            if char == "n":
                if line[::-1][index:index+5] == "neves":
                    left_number = 7
                    break
            if char == "t":
                if line[::-1][index:index+5] == "thgie":
                    left_number = 8
                    break
            if char.isdigit():
                left_number = char
                break
        string_local_sum = str(right_number) + str(left_number)
        local_sum = int(string_local_sum)
        print(local_sum)
        sum += local_sum
    print(sum)