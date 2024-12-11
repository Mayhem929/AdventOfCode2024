def read_input():
    with open("data/day11.txt") as file:
        lines = [int(i) for i in file.readline().split()]        
        return lines


def step(stone):

    new_stones = []

    if stone == 0:
        new_stones.append(1)
    elif len(str(stone))%2 == 0:
        new_stones.append(int(str(stone)[:int(len(str(stone))/2)]))
        new_stones.append(int(str(stone)[int(len(str(stone))/2):]))
    else:
        new_stones.append(stone*2024)

    return new_stones

    
def blink(stones):
    new_stones = []

    for stone in stones:
        new_stones += step(stone)

    return new_stones

def part1():

    stones = read_input()

    for blink_num in range(25):
        stones = (blink(stones))
        # print("After", blink_num+1, "blink:", len(stones))

    return len(stones)



def blink_map(stone_map: dict):
    
    new_stone_map = stone_map.copy()

    for stone in stone_map.keys():
        new_stones = step(stone)

        new_stone_map[stone] -= stone_map[stone]
        for new_stone in new_stones:
            if new_stone in new_stone_map.keys():
                new_stone_map[new_stone] += stone_map[stone]
            else:
                new_stone_map[new_stone] = stone_map[stone]

    return new_stone_map


def part2():

    stones = read_input()

    prev_len = 1
    curr_len = 1
    stone_map = dict()

    curr_len = len(stones)

    for stone in stones:
        if stone not in stone_map.keys():
            stone_map[stone] = 1
        else:
            stone_map[stone] += 1

    for blink_num in range(75):
        stone_map = blink_map(stone_map)
        curr_len = sum(stone_map.values())
        # print("After", blink_num+1, "blinks:", curr_len)

    return curr_len


if __name__=="__main__":
    print(part1())
    print(part2())