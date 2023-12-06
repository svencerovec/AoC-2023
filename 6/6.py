import numpy
if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    times = lines[0].strip().split(" ")
    distances = lines[1].strip().split(" ")
    times = [eval(i) for i in times if i.isnumeric()]
    distances = [eval(i) for i in distances if i.isnumeric()]

    number_of_wins = []
    for i in range(0, len(times)):
        wins = 0
        for j in range(0, times[i]):
            if j * (times[i] - j) > distances[i]:
                wins += 1
        number_of_wins.append(wins)
    print(numpy.prod(number_of_wins))
    times = [str(i) for i in times]
    distances = [str(i) for i in distances]
    
    time_of_single_race = int("".join(times))
    distance_of_single_race = int("".join(distances))

    

    wins = 0
    for i in range(0, time_of_single_race):
        if i * (time_of_single_race - i) > distance_of_single_race:
            wins += 1
    print(wins)