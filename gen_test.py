from random import randint
X = 'X'
O = 'O'
SPACE = ' '

ZZZ = 5 ##############
def print_state(state: list[list]):
    for row in state:
        print(row)

def main():
    n = 15          #size of the board
    move_cnt = 50
    game_map = [[SPACE for i in range(n)] for j in range(n)]
    empty_positions = [(i, j) for i in range(n) for j in range(n)]
    
    for i in range(move_cnt):
        l = len(empty_positions)
        position = empty_positions[randint(0, l - 1)]
        x, y = position
        game_map[x][y] = X if i % 2 == 0 else O
        empty_positions.remove(position)
    
    print_state(game_map)
    print(empty_positions)
    
if __name__ == "__main__":
    main()