from functools import cmp_to_key

def read_input():
    with open("data/day5.txt") as file:
        lines = [i.strip() for i in file.readlines()]        
        
        change = lines.index("")
        rules = lines[:change]
        updates = lines[change+1:]

        return rules, updates
    

# x is lower than y if y in ordering[x]
def ordered(x, y, ordering):

    # este caso es para el maximo ya que al no ser menor que nadie no aparece en las llaves de ordering
    if x not in ordering.keys():
        return False

    return (y in ordering[x])


def create_ordering(rules):
    ordering = {}
    for line in rules:
        rule = [int(i) for i in line.split("|")]
        small   = rule[0]
        big     = rule[1]

        if small not in ordering.keys():
            ordering[small] = []
        
        if big not in ordering[small]:
            ordering[small].append(big)

    return ordering
    

def part1():
    rules, updates = read_input()

    ordering = create_ordering(rules)

    total = 0

    for line in updates:
        update = [int(i) for i in line.split(",")]
        
        for i ,j in zip(update, update[1:]):
            if not ordered(i, j, ordering):
                break
        else:
            total += update[int(len(update)/2)]

    return total


def part2():

    rules, updates = read_input()
    ordering = create_ordering(rules)
    total = 0

    def compare(x, y):
        if x == y:
            return 0
        if x not in ordering.keys():
            return 1
        if y not in ordering[x]:
            return 1
        else:
            return -1

    for line in updates:
        update = [int(i) for i in line.split(",")]
        
        for i ,j in zip(update, update[1:]):
            if not ordered(i, j, ordering):
                break
        else: continue
        
        sorted_update = sorted(update, key=cmp_to_key(compare))
        total += sorted_update[int(len(update)/2)]

    return total


if __name__=="__main__":
    print(part1())
    print(part2())