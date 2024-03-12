from random import randint
X = 'X'
O = 'O'
SPACE = ' '

ZZZ = 5 ##############

def is_empty_position(game_map: list[list], x: int, y: int) -> bool:
    if x < 0 or x >= len(game_map) or y < 0 or y >= len(game_map):
        return False
    if game_map[x][y] == SPACE:
        return True
        return False
    
def print_state(state: list[list]):
    print('[', end='')
    for row in state:
        print(row, end= '')
        print(',')
    print(']')

def main():
    n = 8          #size of the board
    move_cnt = 20
    game_map = [[SPACE for i in range(n)] for j in range(n)]
    empty_positions = set()
    
    
    
    i, j = randint(0, n - 1), randint(0, n - 1)
    game_map[i][j] = X
    for x in range(max(i - 2, 0), min(i + 3, len(game_map))):
        for y in range(max(j - 2, 0), min(j + 3, len(game_map))):
            if is_empty_position(game_map, x, y):
                empty_positions.add((x, y))
                
    for k in range(move_cnt - 1):
        l = len(empty_positions)
        position = empty_positions.pop()
        i, j = position
        game_map[i][j] = X if i % 2 == 0 else O
        
        for x in range(max(i - 1, 0), min(i + 2, len(game_map))):
            for y in range(max(j - 1, 0), min(j + 2, len(game_map))):
                if is_empty_position(game_map, x, y):
                    empty_positions.add((x, y))
        try:
            empty_positions.remove(position)
        except:
            pass
        
    
    
    print_state(game_map)
    # print(empty_positions)
    
if __name__ == "__main__":
    main()