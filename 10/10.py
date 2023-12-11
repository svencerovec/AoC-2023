if __name__ == "__main__":
    file = open("test_input.txt", "r")
    lines = file.readlines()
    start = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                start.append(i)
                start.append(j)
    not_end = True
    positions= lines
    position = start
    visited = []
    while not_end:
        not_end = False
        possible_moves = []
        current_char =positions[position[0]][position[1]] 
        if current_char == "S":
            if position[0]-1 >= 0 and positions[position[0]-1][position[1]] in ["|", "F", "7"]:
                possible_moves.append([position[0]-1, position[1]])
            if position[0]+1 < len(positions) and positions[position[0]+1][position[1]] in ["|", "J", "L"]:
                possible_moves.append([position[0]+1, position[1]])
            if position[1]-1 >= 0 and positions[position[0]][position[1]-1] in ["-", "F", "L"]:
                possible_moves.append([position[0], position[1]-1])
            if position[1]+1 < len(positions[0]) and positions[position[0]][position[1]+1] in ["-", "J", "7"]:
                possible_moves.append([position[0], position[1]+1])
        if current_char == "F":
            possible_moves = [[position[0] + 1 ,position[1]],[position[0], position[1] + 1]]
        if current_char == "|":
            possible_moves = [[position[0] + 1, position[1]],[position[0] - 1, position[1]]]
        if current_char == "-":
            possible_moves = [[position[0], position[1] - 1], [position[0], position[1] + 1]]
        if current_char == "7":
            possible_moves = [[position[0] + 1, position[1]], [position[0], position[1] - 1]]
        if current_char == "L":
            possible_moves = [[position[0] - 1, position[1]], [position[0], position[1] + 1]]
        if current_char == "J":
            possible_moves = [[position[0] - 1, position[1]], [position[0], position[1] - 1]]
        for possible_move in possible_moves:
            if possible_move not in visited:
                if possible_move[0] >= 0 and possible_move[0] < len(positions):
                    if possible_move[1] >= 0 and possible_move[1] < len(positions[0]):
                        visited.append(possible_move)
                        position = possible_move
                        not_end = True
                        break
    print(visited)
    print(len(visited)/2)
    
    marked = []
    for line in lines:
        t = []
        for c in line:
            t.append(c)
        marked.append(t)
    #for x,y in visited:
    #    marked[x][y] = 'X'

    for i, line in enumerate(marked):
        for j, char in enumerate(line):
            if [i,j] not in visited:
                marked[i][j] = "O"
    for line in marked:
        print(line)

