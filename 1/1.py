number_dict = {
        "zero" : "0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }

def replace_first(line):
    position_dict = {
        line.find("zero") : "zero",
        line.find("one") : "one",
        line.find("two") : "two",
        line.find("three") : "three",
        line.find("four") : "four",
        line.find("five") : "five",
        line.find("six") : "six",
        line.find("seven") : "seven",
        line.find("eight") : "eight",
        line.find("nine") : "nine",
    }
    found_positions = []

    for position, number in position_dict.items():
        if position != -1:
            found_positions.append(position)
    first_position = min(found_positions, default = -1)
    if first_position != -1:
        line = line.replace(position_dict.get(first_position), number_dict.get(position_dict.get(first_position)), 1)
    return line

def replace_last(line):
    r_position_dict = {
        line.rfind("zero") : "zero",
        line.rfind("one") : "one",
        line.rfind("two") : "two",
        line.rfind("three") : "three",
        line.rfind("four") : "four",
        line.rfind("five") : "five",
        line.rfind("six") : "six",
        line.rfind("seven") : "seven",
        line.rfind("eight") : "eight",
        line.rfind("nine") : "nine"
    }

    r_found_positions = []

    for position, number in r_position_dict.items():
        if position != -1:
            r_found_positions.append(position)
    
    last_position = max(r_found_positions, default = -1)

    if last_position != -1:
        line = replace_last_occurence(line, r_position_dict.get(last_position), number_dict.get(r_position_dict.get(last_position)))
    return line

def replace_last_occurence(string, old, new):
    new_list = string.rsplit(old, 1)
    return new.join(new_list)



file = open('input.txt', 'r')
sum = 0
lines = file.readlines()
for line in lines:
    first_line = replace_first(line)
    for i in range(0,len(first_line)):
        if first_line[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            first_digit = first_line[i]
            break
    second_line = replace_last(line)
    for i in range(len(second_line)-1,-1,-1):
        if second_line[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            second_digit = second_line[i]
            break
    print(first_digit + second_digit)
    sum += int(first_digit + second_digit)
print(sum)


