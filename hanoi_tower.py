
def move(towers, from_tower, dest_tower):
    disk = towers[from_tower].pop()
    towers[dest_tower].append(disk)
    return towers

def print_towers(towers):
    for i in range(3, 0, -1):
        for tower in towers:
            if len(tower) >= i:
                print(tower[i - 1], end='  ')
            else:
                print('|', end='  ')
        print()
    print('-------')
    
def solve_tower_of_hanoi(towers, n, start_tower, dest_tower, aux_tower):
    if n == 0:
        return
    solve_tower_of_hanoi(towers, n - 1, start_tower, aux_tower, dest_tower)
    move(towers, start_tower, dest_tower)
    print_towers(towers)
    solve_tower_of_hanoi(towers, n - 1, aux_tower,  dest_tower, start_tower)
if __name__ == "__main__":
    towers = [[3, 2, 1], [], []]
    print_towers(towers)
    solve_tower_of_hanoi(towers, 3, 0, 2 , 1)