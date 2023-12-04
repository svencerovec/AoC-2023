file = open("test_input.txt", "r")
lines = file.readlines()
for line_id, line in enumerate(lines):
    line_id += 1
    print(line)