def read_input():
    with open("data/day6.txt") as file:
        lines = [list(i.strip()) for i in file.readlines()]        
        return lines
    
    
def next_pos(curr_row, curr_col, direction):
    if direction == 0:
        return curr_row-1, curr_col
    if direction == 1:
        return curr_row, curr_col+1
    if direction == 2:
        return curr_row+1, curr_col
    if direction == 3:
        return curr_row, curr_col-1


def check_if_cycle(init_row, init_col, mat):

    curr_row = init_row
    curr_col = init_col
    direction = 0
    visited_nodes = set()

    while len(mat)-1 > curr_row > 0 and len(mat[0])-1 > curr_col > 0:
        if (curr_row, curr_col, direction) in visited_nodes:
            return True # Cycle found
        else:
            visited_nodes.add((curr_row, curr_col, direction))
        
        next_row, next_col = next_pos(curr_row, curr_col, direction)
        while mat[next_row][next_col] == "#":
            direction = (direction+1)%4
            next_row, next_col = next_pos(curr_row, curr_col, direction)
        
        curr_row = next_row
        curr_col = next_col

def part1():

    mat = read_input()

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '^':
                init_row = i
                init_col = j

    curr_row = init_row
    curr_col = init_col
    direction = 0
    visited_nodes = {}

    while len(mat)-1 > curr_row > 0 and len(mat[0])-1 > curr_col > 0:
        next_row, next_col = next_pos(curr_row, curr_col, direction)
        while mat[next_row][next_col] == "#":
            direction = (direction+1)%4
            next_row, next_col = next_pos(curr_row, curr_col, direction)
        
        mat[curr_row][curr_col] = "X"
        curr_row = next_row
        curr_col = next_col

    mat[curr_row][curr_col] = "X"

    return sum([i.count("X") for i in mat]) 


def part2():

    mat = read_input()

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '^':
                init_row = i
                init_col = j

    total = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == ".":
                mat[i][j] = "#"
                if check_if_cycle(init_row, init_col, mat):
                    total += 1
                mat[i][j] = "."
    
    return total


if __name__=="__main__":
    print(part1())
    print(part2())