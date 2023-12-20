from Modules import Module, FlipFlop, Conjunction
from collections import deque, Counter
import numpy
import math

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()

    modules = {}
    broadcaster_modules = []
    for line in lines:
        split_line = line.strip().split(" -> ")
        destinations = split_line[1].split(", ")
        if line[0] == "b":
            broadcaster_modules = destinations
        if line[0] == "%":
            modules[split_line[0][1:]] = FlipFlop(split_line[0][1:], destinations)
        if line[0] == "&":
            modules[split_line[0][1:]] = Conjunction(split_line[0][1:], destinations)

    for module in modules:
        if isinstance(modules[module], Conjunction):
            for module_2 in modules:
                if module_2 != module and module in modules[module_2].destination_modules:
                    modules[module].memory[module_2] = 0

    module_to_check = [modules[module] for module in modules if "rx" in modules[module].destination_modules][0]
    senders_to_module = [modules[module].id for module in modules if module_to_check.id in modules[module].destination_modules]
    senders_to_check = {id: 0 for id in senders_to_module}
    lcm_list = []
    low = 0
    high = 0
    num = 0
    while True:
        num += 1
        low += 1
        queue = deque()
        for module_id in broadcaster_modules:
            queue.append([module_id, 0, "b"])
            low += 1
        found = False
        while queue:
            current = queue.popleft()
            module_id = current[0]
            pulse_type = current[1]
            sender = current[2]
            if module_id in modules.keys():
                module = modules[module_id]
                if module.id == module_to_check.id and pulse_type == 1:
                    senders_to_check[sender] += 1
                    if senders_to_check[sender] == 1:
                        lcm_list.append(num)
                    if all(n >= 1 for n in senders_to_check.values()):
                        found = True
                        break
                if isinstance(module, FlipFlop):
                    if pulse_type == 0:
                        module.flip()
                        for destination in module.destination_modules:
                            queue.append([destination, module.switch, module.id])
                            if module.switch == 1:
                                high += 1
                            else:
                                low += 1
                if isinstance(module, Conjunction):
                    module.memory[sender] = pulse_type
                    send = 1
                    if all(v == 1 for v in module.memory.values()):
                        send = 0
                    for destination in module.destination_modules:
                        queue.append([destination, send, module.id])
                        if send == 1:
                            high += 1
                        else:
                            low += 1
        if found:
            break
    #print(low)
    #print(high)
    #print(low*high)
    r = 1
    for v in lcm_list:
        r = math.lcm(r, v)
    print(r)

