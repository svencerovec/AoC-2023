def find_next(array):
    new_array = []
    if not all(v == 0 for v in array):
        for i in range(len(array)-1):
            new_array.append(array[i+1] - array[i])
        return find_next(new_array) + array[-1]
    return 0

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()

    arrays_of_nums = []
    for line in lines:
        line = line.strip()
        arrays_of_nums.append([int(i) for i in line.split(" ")])
    sum = 0
    #for array in arrays_of_nums:
    #    sum += find_next(array)
    for array in arrays_of_nums:
        sum += find_next(array[::-1])
    print(sum)