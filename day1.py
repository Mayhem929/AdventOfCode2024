def read_input():
    with open("data/day1.txt") as file:
        lines = [i.strip() for i in file.readlines()]        
        l = [] 
        r = []
        
        for line in lines:
            numbers = line.split()
            l.append(int(numbers[0]))
            r.append(int(numbers[1]))

        return sorted(l), sorted(r)
    
def part1():
    list1, list2 = read_input()
    return sum([abs(list2[i] - list1[i]) for i in range(len(list1))])

def part2():
    list1, list2 = read_input()    
    return sum([list2.count(list1[i]) * list1[i] for i in range(len(list1))])


if __name__=="__main__":
    print(part1())
    print(part2())