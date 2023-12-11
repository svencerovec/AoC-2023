if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    galaxies = []
    universe = []
    for line in lines:
        line = line.strip()
        if "#" in line:
            universe.append(line)
        else:
            universe.append(["1000000" for i in line])
    universe = zip(*universe)
    universe = [list(x) for x in universe]
    current_universe= []
    for line in universe:
        if "#" in line:
            current_universe.append(line)
        else:
            current_universe.append(["1000000" for i in line])
    current_universe = zip(*current_universe)
    current_universe = [list(x) for x in current_universe]
    for line in current_universe:
        print(line)

    universe = current_universe
    for i, row in enumerate(universe):
        for j, c in enumerate(row):
            if c == "#":
                galaxies.append([i,j])
    print(galaxies)
    pairs = [[a,b] for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    sum_d = 0
    for a,b in pairs:
        r = [a[0], b[0]]
        c = [a[1], b[1]]
        start_row = min(r)
        end_row = max(r)
        start_ch = min(c)
        end_ch = max(c)
        for i in range(start_row, end_row):
            if universe[i][start_ch].isdigit():
                sum_d += int(universe[i][start_ch])
            else:
                sum_d += 1
        for i in range(start_ch, end_ch):
            if universe[end_row][i].isdigit():
                sum_d += int(universe[end_row][i])
            else:
                sum_d += 1
        #sum_d += max(r) - min(r) + max(c) - min(c)
    print(sum_d)
        
                