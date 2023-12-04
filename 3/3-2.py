if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    sum_of_gear_ratios = 0
    for line_index, line in enumerate(lines):
        line = line.strip()
        current_character = 0
        while current_character < len(line):
            if line[current_character] == "*":
                number_list = []

                start_char = current_character - 1
                end_char = current_character + 1

                if start_char == -1:
                    start_char += 1
                if end_char == len(line):
                    end_char -= 1

                if line_index != 0:
                    for i in range(start_char, end_char+1):
                        if lines[line_index-1][i].isdigit():
                            start_of_num = i
                            while lines[line_index-1][start_of_num].isdigit() and start_of_num >= 0:
                                start_of_num -= 1
                            start_of_num += 1
                            j = start_of_num
                            num_str = ""
                            while lines[line_index-1][j].isdigit() and j < len(line):
                                num_str += lines[line_index-1][j]
                                j += 1
                            end_of_num = j
                            this_number = num_str + ";" + str(start_of_num) + ";" + str(end_of_num)
                            number_list.append(this_number)
                if line_index != len(lines)-1:
                    for i in range(start_char, end_char+1):
                        if lines[line_index+1][i].isdigit():
                            start_of_num = i
                            while lines[line_index+1][start_of_num].isdigit() and start_of_num >= 0:
                                start_of_num -= 1
                            start_of_num += 1
                            j = start_of_num
                            num_str = ""
                            while lines[line_index+1][j].isdigit() and j < len(line):
                                num_str += lines[line_index+1][j]
                                j += 1
                            end_of_num = j
                            this_number = num_str + ";" + str(start_of_num) + ";" + str(end_of_num)
                            number_list.append(this_number)
                if start_char != 0 and lines[line_index][start_char].isdigit():
                    start_of_num = start_char
                    while lines[line_index][start_of_num].isdigit() and start_of_num >= 0:
                        start_of_num -= 1
                    start_of_num += 1
                    j = start_of_num
                    num_str = ""
                    while lines[line_index][j].isdigit() and j < len(line):
                        num_str += lines[line_index][j]
                        j += 1
                    end_of_num = j
                    this_number = num_str + ";" + str(start_of_num) + ";" + str(end_of_num)
                    number_list.append(this_number)
                if end_char != len(line) and lines[line_index][end_char].isdigit():
                    start_of_num = end_char
                    while lines[line_index][start_of_num].isdigit() and start_of_num >= 0:
                        start_of_num -= 1
                    start_of_num += 1
                    j = start_of_num
                    num_str = ""
                    while lines[line_index][j].isdigit() and j < len(line):
                        num_str += lines[line_index][j]
                        j += 1
                    end_of_num = j
                    this_number = num_str + ";" + str(start_of_num) + ";" + str(end_of_num)
                    number_list.append(this_number)
                gear_number_set = set(number_list)
                if len(gear_number_set) == 2:
                    multiplication = 1
                    for gear_number in gear_number_set:
                        multiplication *= int(gear_number.split(";")[0])
                    sum_of_gear_ratios += multiplication
            current_character += 1
    print(sum_of_gear_ratios)
    


