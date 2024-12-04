def read_input():
    with open("data/day4.txt") as file:
        lines = [i.strip() for i in file.readlines()]        
        return lines
    

def check_xmas(mat, i, j):
    checks = 0
    if i + 3 < len(mat):
        if mat[i+1][j] == 'M' and mat[i+2][j] == 'A' and mat[i+3][j] == 'S':
           checks += 1
    if i - 3 >= 0:
        if mat[i-1][j] == 'M' and mat[i-2][j] == 'A' and mat[i-3][j] == 'S':
            checks += 1
    if j + 3 < len(mat[0]):
        if mat[i][j+1] == 'M' and mat[i][j+2] == 'A' and mat[i][j+3] == 'S':
            checks += 1
    if j - 3 >= 0:
        if mat[i][j-1] == 'M' and mat[i][j-2] == 'A' and mat[i][j-3] == 'S':
            checks += 1
    if i + 3 < len(mat) and j + 3 < len(mat[0]):
        if mat[i+1][j+1] == 'M' and mat[i+2][j+2] == 'A' and mat[i+3][j+3] == 'S':
            checks += 1
    if i - 3 >= 0 and j - 3 >= 0:
        if mat[i-1][j-1] == 'M' and mat[i-2][j-2] == 'A' and mat[i-3][j-3] == 'S':
            checks += 1
    if i + 3 < len(mat) and j - 3 >= 0:
        if mat[i+1][j-1] == 'M' and mat[i+2][j-2] == 'A' and mat[i+3][j-3] == 'S':
            checks += 1
    if i - 3 >= 0 and j + 3 < len(mat[0]):
        if mat[i-1][j+1] == 'M' and mat[i-2][j+2] == 'A' and mat[i-3][j+3] == 'S':
            checks += 1    

    return checks


def part1():
    
    mat = read_input()
    total = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 'X':
                total += check_xmas(mat, i, j)
                    
    return total


def check_mas(mat, i, j):
    total = 0

    if mat[i+1][j+1] == 'S' and mat[i-1][j-1] == 'M' and mat[i-1][j+1] == 'S' and mat[i+1][j-1] == 'M':
        total += 1
    if mat[i-1][j-1] == 'S' and mat[i+1][j+1] == 'M' and mat[i+1][j-1] == 'S' and mat[i-1][j+1] == 'M':
        total += 1
    if mat[i+1][j+1] == 'S' and mat[i-1][j-1] == 'M' and mat[i-1][j+1] == 'M' and mat[i+1][j-1] == 'S':
        total += 1
    if mat[i-1][j-1] == 'S' and mat[i+1][j+1] == 'M' and mat[i+1][j-1] == 'M' and mat[i-1][j+1] == 'S':
        total += 1

    return total


def part2():

    mat = read_input()
    total = 0

    for i in range(1, len(mat)-1):
        for j in range(1, len(mat[0])-1):
            if mat[i][j] == 'A':
                total += check_mas(mat, i, j)            

    return total


if __name__=="__main__":
    print(part1())
    print(part2())