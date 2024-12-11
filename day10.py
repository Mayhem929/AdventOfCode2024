def read_input():
    with open("data/day10.txt") as file:
        lines = [[int(j) if j != '.'  else 20 for j in i.strip()] for i in file.readlines()]        
        return lines

def next_part1(pos, height, mat, visited):

    total = 0
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if len(mat) > new_pos[0] >= 0 and len(mat[0]) > new_pos[1] >= 0:
            if mat[new_pos[0]][new_pos[1]] == height + 1:
                total += next_part1(new_pos, height+1, mat, visited)

    if height == 9:
        if new_pos not in visited:
            visited.append(new_pos)
            return 1
        else:
            return 0
        
    else:
        return total


def part1():

    mat = read_input()

    total = 0

    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 0:
                visited = []
                total += next_part1((i,j), 0, mat, visited)

    return total


def next_part2(pos, height, mat):

    total = 0
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if len(mat) > new_pos[0] >= 0 and len(mat[0]) > new_pos[1] >= 0:
            if mat[new_pos[0]][new_pos[1]] == height + 1:
                total += next_part2(new_pos, height+1, mat)

    if height == 9:
        return 1
    else:
        return total


def part2():
    mat = read_input()

    total = 0

    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 0:
                visited = []
                total += next_part2((i,j), 0, mat)

    return total

if __name__=="__main__":
    print(part1())
    print(part2())
