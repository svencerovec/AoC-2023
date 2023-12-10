if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()

    graph = {}
    for i in range(len(lines)):
        if i == 0:
            instructions = lines[i].strip()
            continue
        if i == 1:
            continue
        key, pair = lines[i].strip().replace(" ", "").split("=")
        pair = pair.strip("(").strip(")").split(",")
        graph[key] = pair

    current_position = "AAA"
    num_steps = 0
    while 1:
        for c in instructions:
            if c == "L":
                current_position = graph[current_position][0]
            if c == "R":
                current_position = graph[current_position][1]
            num_steps += 1
            print(current_position)
            if current_position == "ZZZ":
                break
        if current_position == "ZZZ":
            break
    print(num_steps)
            
