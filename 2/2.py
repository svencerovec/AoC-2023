if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()

    max_red = 12
    max_green = 13
    max_blue = 14
    sum_of_correct_indexes = 0
    sum_of_powers = 0

    for line in lines:
        line = line.strip("\n")
        current_red = 0
        current_green = 0
        current_blue = 0

        current_red_max = 1
        current_green_max = 1
        current_blue_max = 1
        error = False
        
        split_by_colon = line.split(":")
        index = split_by_colon[0].split(" ")[1]
        contents = split_by_colon[1].split(";")
        for round in contents:
            reveals = round.split(",")
            for reveal in reveals:
                reveal_split = reveal.split(" ")
                count = reveal_split[1]
                color = reveal_split[2]
                if color == "blue":
                    if int(count) > max_blue:
                        error = True
                    if int(count) > current_blue_max:
                        current_blue_max = int(count)
                if color == "red":
                    if int(count) > max_red:
                        error = True
                    if int(count) > current_red_max:
                        current_red_max = int(count) 
                if color == "green":
                    if int(count) > max_green:
                        error = True
                    if int(count) > current_green_max:
                        current_green_max = int(count)
        if not error:
            sum_of_correct_indexes += int(index)
        sum_of_powers += current_blue_max * current_green_max * current_red_max
    print(sum_of_correct_indexes)
    print(sum_of_powers)