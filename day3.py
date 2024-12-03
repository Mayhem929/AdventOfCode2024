import re

def read_input():
    with open("data/day3.txt") as file:
        return [i.strip() for i in file.readlines()]

def part1():
    lines = read_input()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", "".join(lines))
    
    result = 0
    for match in matches:
        factors = re.findall(r"\d{1,3}", match)
        result += (int(factors[0]) * int(factors[1]))

    return result


def part2():
    lines = read_input()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", "".join(lines))
    
    result = 0
    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled == True:
            factors = re.findall(r"\d{1,3}", match)
            result += (int(factors[0]) * int(factors[1]))

    return result


if __name__=="__main__":
    print(part1())
    print(part2())