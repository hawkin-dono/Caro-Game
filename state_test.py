from caro import State
class test_state():
    def __init__(self) -> None:
        pass
    
    def test_case_1(self):
        n = 8
        game_map = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '0', 'O', 'O', 'O', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', 'X', 'X', 'X', 'X', 'X', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        move_cnt = 0
        empty_positions = set([(i, j) for i in range(n) for j in range(n)])
        for i in range(n):
            for j in range(n):
                if (game_map[j][i] != ' '):
                    move_cnt += 1
                    empty_positions.remove((i, j))
        last_move = (5, 6)
        state = State(game_map, move_cnt, empty_positions, last_move)
        res = state.check_game_end()
        
        if res == 1:
            print("End game")
        else:
            print("Continue game")
        return res
        
    def test_case_2(self):
        n = 8
        game_map = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', 'O', ' ', ' '],
                    [' ', 'X', ' ', '0', 'O', 'O', 'O', ' '],
                    [' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', 'X', 'X', 'X', ' '],
                    [' ', ' ', ' ', ' ', ' ', 'X', 'O', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ']]
        move_cnt = 0
        empty_positions = set([(i, j) for i in range(n) for j in range(n)])
        for i in range(n):
            for j in range(n):
                if (game_map[j][i] != ' '):
                    move_cnt += 1
                    empty_positions.remove((i, j))
        last_move = (5, 4)
        state = State(game_map, move_cnt, empty_positions, last_move)
        res = state.check_game_end()
        
        if res == 1:
            print("End game")
        else:
            print("Continue game")
        return res
    
    
        

def main():
    test = test_state()
    res = test.test_case_2()
    print(res)
    
    
if __name__ == "__main__":
    main()