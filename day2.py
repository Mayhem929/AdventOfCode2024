def read_input():
    with open("data/day2.txt") as file:
        data = [[int(j) for j in i.strip().split()] for i in file.readlines()]        
        
        return data

def safe(line):
    difference = [(line[j+1] - line[j]) for j in range(len(line) - 1)]

    if sum(abs(i) > 3 for i in difference):
        return False
    elif (sum(i > 0 for i in difference) == len(difference)) or sum(i < 0 for i in difference) == len(difference):
        return True

    return False


def part1():
    numbers = read_input()

    num_safe = 0
    for line in numbers:
        if safe(line):
            num_safe+=1
        
    return num_safe


def safe_with_tolerance(line):
    
    if safe(line):
        return True
    
    for i in range(len(line)):
        line_deleted = line[:i] + line[i+1:]
        if safe(line_deleted):
            return True

    return False

def part2():
    numbers = read_input()

    num_safe = 0
    for line in numbers:
        if safe_with_tolerance(line):
            num_safe+=1
        
    return num_safe


if __name__=="__main__":
    print(part1())
    print(part2())