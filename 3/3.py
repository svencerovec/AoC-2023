if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    sum_of_numbers = 0
    for line_index, line in enumerate(lines):
        line = line.strip()
        current_character = 0
        while current_character < len(line):
            if line[current_character].isdigit():
                num_string = line[current_character]
                start_char = current_character - 1
                current_character += 1

                while current_character < len(line) and line[current_character].isdigit():
                    num_string += line[current_character]
                    current_character += 1

                end_char = current_character + 1
                
                symbol_exists = False
                if line_index != 0:
                    for i in range(start_char, end_char):
                        if lines[line_index-1][i] not in ["0","1","2","3","4","5","6","7","8","9","."] and i < len(line):
                            symbol_exists = True
                            break
                if line_index != len(lines)-1:
                    for i in range(start_char, end_char):
                        if lines[line_index+1][i] not in ["0","1","2","3","4","5","6","7","8","9","."] and i < len(line):
                            symbol_exists = True
                            break
                if start_char != -1 and lines[line_index][start_char] not in ["0","1","2","3","4","5","6","7","8","9","."]:
                    symbol_exists = True
                if end_char-1 < len(line) and lines[line_index][end_char-1] not in ["0","1","2","3","4","5","6","7","8","9","."]:
                    symbol_exists = True
                if symbol_exists:
                    sum_of_numbers += int(num_string)
                    print(num_string)
            current_character += 1
    print(sum_of_numbers)
    


