if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    start = ()
    map = [list(line.strip()) for line in lines]

    empty_map = []        

    for i in range(64):
        locations = []
        for r in range(len(map)):
            for c in range(len(map[0])):
                if map[r][c] == "S" or map[r][c] == "O":
                    locations.append((r,c))

        for r,c in locations:
            map[r][c] = "."
        for r,c in locations:
            if r != 0 and map[r-1][c] != "#":
                map[r-1][c] = "O"
            if c != 0 and map[r][c-1] != "#":
                map[r][c-1] = "O"
            if r != len(map) - 1 and map[r+1][c] != "#":
                map[r+1][c] = "O"
            if c != len(map[0]) - 1 and map[r][c+1] != "#":
                map[r][c+1] = "O"
    n = 0
    for r in map:
        for c in r:
            if c == "O":
                n += 1
    print(n)
                    
