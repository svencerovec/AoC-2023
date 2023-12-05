from multiprocessing import Process
import multiprocessing

class Map:
    def __init__(self, name):
        self.name = name
        self.list = []

def get_min_location(i, num1, num2, maps, return_dict):
    min_location = (2**63)-1
    for j in range(num1, num1 + num2):
        location_number = j
        for map in maps:
            for item in map.list:
                if location_number >= item[1] and location_number < item[1] + item[2]:
                    location_number = location_number + item[0] - item[1]
                    break
        if location_number < min_location:
            min_location = location_number
    return_dict[i] = min_location


if __name__ == "__main__":
    file = open("test_input.txt", "r")
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

    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    min_locations = []
    jobs = []
    for i in range (0,len(seeds_list),2):
        p = Process(target=get_min_location, args=(i, seeds_list[i],seeds_list[i+1], maps, return_dict))
        jobs.append(p)
        p.start()
    for p in jobs:
        p.join()
    
    print(min(return_dict.values()))
                    
