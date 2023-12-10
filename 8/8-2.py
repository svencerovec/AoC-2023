import math
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

    current_positions = []
    for key in list(graph.keys()):
        if key[2] == "A":
            current_positions.append(key)

    num_steps = 0
    loops = []
    for current_position in current_positions:
        found_loop = False
        while 1:
            for c in instructions:
                if c == "L":
                    current_position = graph[current_position][0]
                if c == "R":
                    current_position = graph[current_position][1]
                num_steps += 1
                if current_position[2] == "Z":
                    loops.append(num_steps)
                    found_loop = True
                    num_steps = 0
                    break
            if found_loop:
                break
    print(loops)

    r = loops[0]
    for steps in loops:
        r = math.lcm(r, steps)
        #r = r * steps // math.gcd(r, steps)
    print(r)
            
