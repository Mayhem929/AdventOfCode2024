import itertools
from math import log10, ceil

def foo(l):
     yield from itertools.product(*([l] * 3)) 


def read_input():
    with open("data/day7.txt") as file:
        lines = [i.strip() for i in file.readlines()]        
        return lines
    

def get_combinations(repeat=5, characters="+*."):
    return itertools.product(characters, repeat=repeat)


def part1():
    
    lines = read_input()

    total = 0
    for line in lines:
        test_value = int(line.split(":")[0])
        values = [int(i) for i in line.split(":")[1].split()]

        operators = map(''.join, get_combinations(len(values)-1, "+*"))
        
        for combination in operators:
            sum=0
            idx=0
            for j in values[1:]:
                if idx==0:
                    sum = int(values[0])
                if combination[idx] == "+":
                    sum += j
                else:
                    sum *= j

                idx+=1
                if sum == test_value:
                    total+=test_value
                    break
                elif sum > test_value:
                    break
            
            if sum == test_value:
                break
        
    return total


def part2():    
    
    lines = read_input()

    total = 0
    num=0
    for line in lines:
        test_value = int(line.split(":")[0])
        values = [int(i) for i in line.split(":")[1].split()]

        operators = map(''.join, get_combinations(len(values)-1))        
        num+=1

        for combination in operators:
            sum=0
            idx=0
            for j in values[1:]:
                if idx==0:
                    sum = int(values[0])
                if combination[idx] == "+":
                    sum += j
                elif combination[idx] == "*":
                    sum *= j
                else:
                    sum = int(str(sum) + str(j))

                idx+=1
                
                if sum > test_value:
                    break
            
            if sum == test_value:
                total+=test_value
                break
        
    return total


if __name__=="__main__":
    print(part1())
    print(part2())

