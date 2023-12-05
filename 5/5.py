class Map:
    def __init__(self, name):
        self.name = name
        self.list = []


if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    seeds_list = []
    maps = []
    sd_map = None
    for line in lines:
        if lines.index(line) == 0:
            line = line.split(" ")
            for i in range(1, len(line)):
                seeds_list.append(int(line[i]))
            continue
        if lines.index(line) == 1:
            continue
        line = line.strip()
        if line.split(" ")[1] == "map:":
            if sd_map != None:
                maps.append(sd_map)
            sd_map = Map(line.split(" ")[0])
            continue
        if len(line) != 0:
            line = line.split(" ")
            int_list = [eval(i) for i in line]
            sd_map.list.append(int_list)
    maps.append(sd_map)
    seeds = []
    for i in range (0,len(seeds_list),2):
        for j in range(seeds_list[i], seeds_list[i] + seeds_list[i+1]):
            seeds.append(j)
    location_numbers = []
    for number in seeds:
        location_number = number
        for map in maps:
            print(location_number)
            for item in map.list:
                destination_value = item[0]
                source_value = item[1]
                range = item[2]
                if location_number >= source_value and location_number < source_value + range:
                    difference = destination_value - source_value
                    location_number = location_number + difference
                    break
        location_numbers.append(location_number)
    print(min(location_numbers))
                    
