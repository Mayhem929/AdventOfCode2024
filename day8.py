def read_input():
    with open("data/day8.txt") as file:
        lines = [list(i.strip()) for i in file.readlines()]        
        return lines
    
    
def inside_mat(pos, rows, cols):
    return (0 <= pos[0] < rows and 0 <= pos[1] < cols) 


def add_antinodes(mat, pos1, pos2, total_antinodes):
    diff = (pos2[0]-pos1[0], pos2[1]-pos1[1])
    
    antinode1 = (pos2[0]+diff[0], pos2[1]+diff[1])
    antinode2 = (pos1[0]-diff[0], pos1[1]-diff[1])

    if inside_mat(antinode1, len(mat), len(mat[0])):
        total_antinodes.add(antinode1)
        if (mat[antinode1[0]][antinode1[1]] == "." or mat[antinode1[0]][antinode1[1]] == "#"):
            mat[antinode1[0]][antinode1[1]] = "#"
        

    if inside_mat(antinode2, len(mat), len(mat[0])): 
        total_antinodes.add(antinode2)
        if (mat[antinode2[0]][antinode2[1]] == "." or mat[antinode2[0]][antinode2[1]] == "#"):
            mat[antinode2[0]][antinode2[1]] = "#"


def part1():

    mat = read_input()
    frecuencies = set()

    for line in mat:
        for char in line:
            if char != ".":
                frecuencies.add(char)

    print(frecuencies)

    total_antinodes = set()

    for frec in frecuencies:

        antennas = []
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] == frec:
                    antennas.append((i,j))

        for i in range(len(antennas)):
            for j in range(i+1, len(antennas)):
                add_antinodes(mat, antennas[i], antennas[j], total_antinodes)

        
    for line in mat:
        print("".join(line))

    return len(total_antinodes)


def add_antinodes_inline(mat, pos1, pos2, total_antinodes):
    
    diff = (pos2[0]-pos1[0], pos2[1]-pos1[1])
    step = 100000000000000 # para decir que es infinito xd
    if diff[0] != 0:
        step = (diff[1]/diff[0])

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            new_diff = (i-pos1[0],j-pos1[1])
            new_step = 100000000000000
            if new_diff[0] != 0:
                new_step = (new_diff[1]/new_diff[0])

            if ((i,j) == pos1) or ((i,j) == pos2):
                total_antinodes.add((i,j))
            elif step == 100000000000000 and i==pos1[0]:
                total_antinodes.add((i,j))
                if (mat[i][j] == "."):
                    mat[i][j] = "#"
            elif step == new_step:
                total_antinodes.add((i,j))
                if (mat[i][j] == "."):
                    mat[i][j] = "#"
        

def part2():

    mat = read_input()
    frecuencies = set()

    for line in mat:
        for char in line:
            if char != ".":
                frecuencies.add(char)

    print(frecuencies)

    total_antinodes = set()

    for frec in frecuencies:

        antennas = []
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] == frec:
                    antennas.append((i,j))

        for i in range(len(antennas)):
            for j in range(i+1, len(antennas)):
                add_antinodes_inline(mat, antennas[i], antennas[j], total_antinodes)

        
    for line in mat:
        print("".join(line))

    return len(total_antinodes)


if __name__=="__main__":
    print(part1())
    print(part2())