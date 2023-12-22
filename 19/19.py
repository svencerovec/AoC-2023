def is_accepted(part, wf_id, workflows):
    for workflow in workflows:
        if workflow.id == wf_id:
            for rule in workflow.rules:
                if rule == "A":
                    return 1
                if rule == "R":
                    return 0
                if ":" not in rule:
                    return is_accepted(part, rule, workflows)
                rs = rule.split(":")
                c = int(part.return_value(rule[0]))
                r = rs[1]
                if rule[1] == "<":
                    v = int(rs[0].split("<")[1])
                    if c < v:
                        if r == "A":
                            return 1
                        if r == "R":
                            return 0
                        return is_accepted(part, r, workflows)
                if rule[1] == ">":
                    v = int(rs[0].split(">")[1])
                    if c > v:
                        if r == "A":
                            return 1
                        if r == "R":
                            return 0
                        return is_accepted(part, r, workflows)      
    return 0

class Workflow:
    def __init__(self, id, rules):
        self.id = id
        self.rules = rules
class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    def return_value(self, c):
        if c == "x":
            return self.x
        if c == "m":
            return self.m
        if c == "a":
            return self.a
        if c == "s":
            return self.s

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()


    workflow_lines = []
    part_lines = [] 
    for line in lines:
        if line == "\n":
            continue
        if line.startswith("{"):
            part_lines.append(line.strip())
        else:
            workflow_lines.append(line.strip())

    workflows = []
    parts = []
    for workflow_line in workflow_lines:
        split = workflow_line.strip("}").split("{")
        workflows.append(Workflow(split[0], split[1].split(",")))

    for part_line in part_lines:
        components = part_line.strip("}").strip("{").split(",")
        x = int(components[0].split("=")[1])
        m = int(components[1].split("=")[1])
        a = int(components[2].split("=")[1])
        s = int(components[3].split("=")[1])
        parts.append(Part(x, m, a, s))

    sum = 0
    for part in parts:
        if is_accepted(part, "in", workflows):
            sum += part.x
            sum += part.m
            sum += part.a
            sum += part.s
    print(sum)