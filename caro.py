
"""
Input:

- n: số nguyên dương là kích thước bàn cờ (10 < n < 20)

- m: số nguyên là tổng số nước mà 2 người chơi đã đi ( m >= 0)

- m cặp số nguyên (x, y) tiếp theo là tọa độ lần lượt của các nước đi của hai người chơi (0 <= x, y <= n-1)

Output:

- Cặp số x, y là tọa độ nước đi tiếp theo của máy
"""


import time
### Define the constants

X = 'X'
O = 'O'
SPACE = ' '

TARGET = 5 ##############

    
class State():
    def __init__(self, game_map: list[list], move_cnt: int, empty_positions: set[tuple[int, int]]= None, last_move: tuple[int, int] = (-1, -1)) -> None:
        """
        Args:
            game_map (list[list]): map of the game
            move_cnt (int): number of moves haved been done
            empty_positions (set[tuple[int, int]], optional): set of empty_position. Defaults to None.
            last_move (tuple[int, int], optional): the last move. Defaults to (-1, -1).
        """
        
        self.game_map = game_map
        self.move_cnt = move_cnt
        
        if empty_positions is None:
            self.empty_positions = self.get_target_empty_positions()
        else:
            self.empty_positions = empty_positions
        self.last_move = last_move
        
    def print_state(self):
        size = len(self.game_map)
        print("     ", end = "")
        
        for i in range(size):
            if i < 10:
                print(i, end = "    ")
            else:
                print(i, end = "   ")
            
        print()
            
        for i in range(size):
            if i < 10:
                print(f'{i}', end = "   ")
            else:
                print(f'{i}', end = "  ")
            print(self.game_map[i])
     
    @staticmethod       
    def get_symbol(move_cnt) -> str:
        return ((move_cnt + 1) % 2) * X + (move_cnt % 2) * O
    
    def is_empty_position(self, x: int, y: int) -> bool:
        if x < 0 or x >= len(self.game_map) or y < 0 or y >= len(self.game_map):
            return False
        if self.game_map[x][y] == SPACE:
            return True
        return False
    
    def get_target_empty_positions(self) -> set[tuple[int, int]]:
        empty_positions = set()
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map)):
                if self.game_map[i][j] == SPACE:
                    continue
                for x in range(max(i - 1, 0), min(i + 2, len(self.game_map))):
                    for y in range(max(j - 1, 0), min(j + 2, len(self.game_map))):
                        if self.is_empty_position(x, y):
                            empty_positions.add((x, y))
        return empty_positions
    
        
    
    def check_row_end(self) -> bool:
        """_summary_
        check if the game is ended by row
        
        Returns:
            bool: True if the game is ended by row, False otherwise
        """
        
        count = 0
        row, col = self.last_move
        y1 = max(row - (TARGET - 1), 0)
        y2 = min(row + (TARGET - 1), len(self.game_map) - 1)

        for y in range(y1, y2 + 1):
            if self.game_map[row][y] == self.game_map[row][col]:
                count += 1
            else:
                count = 0

            if (count >= TARGET):
                return True

        return False

    def check_column_end(self) -> bool:
        """_summary_
        check if the game is ended by column
        
        Returns:
            bool: True if the game is ended by column, False otherwise
        """
        count = 0
        row, col = self.last_move
        x1 = max(col - (TARGET - 1), 0)
        x2 = min(col + (TARGET - 1), len(self.game_map) - 1)
        
        for x in range(x1, x2 + 1):
            if self.game_map[x][col] == self.game_map[row][col]:
                count += 1
            else: 
                count = 0

            if (count >= TARGET):
                return True

        return False

    def check_diagonal_first(self) -> bool:
        """_summary_
        check if the game is ended by diagonal \
        
        Returns:
            bool: True if the game is ended by diagonal, False otherwise
        """
        count = 0
        row, col = self.last_move
        x1, x2, y1, y2 = 0, 0, 0, 0
        if (row <= col):
            x1 = max(row - (TARGET - 1), 0)
            y1 = col - (row - x1)
            y2 = min(col + (TARGET - 1), len(self.game_map) - 1)
            x2 = row + (y2 - col)
        else:
            y1 = max(col - (TARGET - 1), 0)
            x1 = row - (col - y1)
            x2 = min(row + (TARGET - 1), len(self.game_map) - 1)
            y2 = col + (x2 - row)

        y = y1
        for x in range(x1, x2 + 1):
            if self.game_map[x][y] == self.game_map[row][col]:
                count += 1
            else:
                count = 0
            y += 1
            
            if count >= TARGET:
                return True        

        return False

    def check_diagonal_second(self) -> bool:
        """_summary_
        check if the game is ended by diagonal /
        
        Returns:
            bool: True if the game is ended by diagonal, False otherwise
        """
        count = 0
        row, col = self.last_move
        x1, x2, y1, y2 = 0, 0, 0, 0
        if (row <= len(self.game_map) - 1 - col):
            x1 = max(row - (TARGET - 1), 0)
            y2 = col + (row - x1)
            y1 = max(col - (TARGET - 1), 0)
            x2 = row + (col - y1)
        else:
            y2 = min(col + (TARGET - 1), len(self.game_map) - 1)
            x1 = row - (y2 - col)
            x2 = min(row + (TARGET - 1), len(self.game_map) - 1)
            y1 = col - (x2 - row)

        y = y2
        for x in range(x1, x2 + 1):
            if self.game_map[x][y] == self.game_map[row][col]:
                count += 1
            else:
                count = 0
            y -= 1

            if count >= TARGET:
                return True
            
        return False

    def check_game_end(self) -> bool:
        """
        check if the game is ended by row, column or diagonal
        
        Returns:
            bool: True if the game is ended, False otherwise
        """
        
        # if self.check_column_end():
        #     print("Column end")
        # elif self.check_row_end():
        #     print("Row end")
        # elif self.check_diagonal_first():
        #     print("Diagonal first end")
        # elif self.check_diagonal_second():
        #     print("Diagonal second end")
            
        return (self.check_row_end() or
                self.check_column_end() or
                self.check_diagonal_first() or
                self.check_diagonal_second())         

        
        
    
class Solver():
    def __init__(self) -> None:
        pass

    def minimax(self, state: State, depth: int, alpha = -float("inf"), beta = float("inf")) -> int:
        """
        MiniMax algorithm with alpha-beta pruning

        Args:
            state (State): the state of the game
            depth (int): the depth of the tree
            alpha (int, optional): Defaults to -float("inf").
            beta (int, optional): Defaults to float("inf").
            
        Returns:
            int: the value of the move 
        """
        
        score = 0
        if (state.last_move != (-1, -1)):
            game_ended = state.check_game_end()
            score = game_ended * 100 * (1 - 2*(depth % 2)) 
            # print(score)
            # print_state(state)

        if (score == 100):
            return 100
        
        if (score == -100):
            return -100
        
        if (depth > 3):
            return 0
        
        if (depth % 2 == 0):
            best = float("inf")
            empty_positions_copy = state.empty_positions.copy()
            while len(empty_positions_copy) > 0:
                
                empty_position = empty_positions_copy.pop()
                empty_positions_tmp = state.empty_positions.copy()
                last_move_tmp = state.last_move
                i, j = empty_position
                for x in range(max(i - 1, 0), min(i + 2, len(state.game_map))):
                    for y in range(max(j - 1, 0), min(j + 2, len(state.game_map))):
                        if state.is_empty_position(x, y):
                            state.empty_positions.add((x, y))
                            
                state.empty_positions.remove(empty_position)
                state.game_map[empty_position[0]][empty_position[1]] = State.get_symbol(state.move_cnt)
                state.move_cnt += 1
                state.last_move = empty_position
                
                best = min(best, self.minimax(state, depth + 1, alpha, beta))
                
                state.empty_positions = empty_positions_tmp
                state.game_map[empty_position[0]][empty_position[1]] = SPACE
                state.move_cnt -= 1
                state.last_move = last_move_tmp
                
                beta = min(beta, best)
                if (alpha >= beta):
                    break
            if (best == float("inf")):
                return 0
            return best
        else:
            best = -float("inf")
            empty_positions_copy = state.empty_positions.copy()
            while len(empty_positions_copy) > 0:
                
                empty_position = empty_positions_copy.pop()
                empty_positions_tmp = state.empty_positions.copy()
                last_move_tmp = state.last_move
                i, j = empty_position
                for x in range(max(i - 1, 0), min(i + 2, len(state.game_map))):
                    for y in range(max(j - 1, 0), min(j + 2, len(state.game_map))):
                        if state.is_empty_position(x, y):
                            state.empty_positions.add((x, y))
                            
                state.empty_positions.remove(empty_position)
                state.game_map[empty_position[0]][empty_position[1]] = State.get_symbol(state.move_cnt)
                state.move_cnt += 1
                state.last_move = empty_position
                
                best = max(best, self.minimax(state, depth + 1, alpha, beta))

                state.empty_positions = empty_positions_tmp
                state.game_map[empty_position[0]][empty_position[1]] = SPACE
                state.move_cnt -= 1
                state.last_move = last_move_tmp
                
                alpha = max(alpha, best)
                if (alpha >= beta):
                    break
            if (best == -float("inf")):
                return 0
            return best 
        
    def solve(self, state: State) -> tuple[int, int]:
        """
        Args:
            state (State): the state of the game
            
        Return:  the best move for the current state
        """
        best_move = (-1, -1)
        best_val = -float("inf")

        empty_positions_copy = state.empty_positions.copy()
        while len(empty_positions_copy) > 0:
            empty_position = empty_positions_copy.pop()
            empty_positions_tmp = state.empty_positions.copy()
            last_move_tmp = state.last_move
            i, j = empty_position
            for x in range(max(i - 1, 0), min(i + 2, len(state.game_map))):
                for y in range(max(j - 1, 0), min(j + 2, len(state.game_map))):
                    if state.is_empty_position(x, y):
                        state.empty_positions.add((x, y))
                        
            state.empty_positions.remove(empty_position)
            state.game_map[empty_position[0]][empty_position[1]] = State.get_symbol(state.move_cnt)
            state.move_cnt += 1
            state.last_move = empty_position
                
            move_val = self.minimax(state, 0)
            
            state.empty_positions = empty_positions_tmp
            state.game_map[empty_position[0]][empty_position[1]] = SPACE
            state.move_cnt -= 1
            state.last_move = last_move_tmp
            
            if (move_val > best_val):
                best_val = move_val
                best_move = empty_position
            if best_val > 0:
                break

        # print(best_val)

        return best_move         

class CaroGame():
    def __init__(self, n: int= None, game_map: list[list] = None, move_cnt: int = None, last_move: tuple[int, int] = (-1, -1)):
        """_summary_

        Args:
            n (int, optional): Size of the game. Defaults to None.
            game_map (list[list], optional): map of the game. Defaults to None.
            move_cnt (int, optional): number of moves haved been done. Defaults to None.
            empty_positions (set[tuple[int, int]], optional): set of empty_position. Defaults to None.
        
        Returns:
            None
        """
        if n is None:
            self.state = self.input_caro_board()
        else:
            self.state = State(game_map= game_map, move_cnt= move_cnt, empty_positions= None, last_move= last_move)
            self.state.print_state()
        self.solver = Solver()

        res = self.solver.solve(self.state)
        print(res)
        x, y = res
        self.state.game_map[x][y] = State.get_symbol(self.state.move_cnt)
        self.state.print_state()
        
        # return res
    
        
    def input_caro_board(self):
        """_summary_
        get size, number of moves haved been done and position of each moves
        if the input is invalid, ask the user to retype the input or exit

        Returns:
            State: the state of the game
        """
        try: 
            n = int(input("size of the caro game: "))            #size of the board
            move_cnt = int(input("number of moves haved been done: "))
            game_map = [[SPACE for i in range(n)] for j in range(n)]
            
            for i in range(move_cnt):
                x, y = list(map(int, input("Enter the position of the move (input's format: x, y): ").split(', ')))
                game_map[x][y] = State.get_symbol(i)               # start move is X
                if i == move_cnt -1:
                    last_move = (x, y)
                
            state = State(game_map= game_map, move_cnt= move_cnt, empty_positions = None, last_move=last_move)
            state.print_state()
            
        except Exception:
            print("Invalid input")
            print("Choose to retype the input or exit, type 'r' or 'e' respectively")
            choice = input()
            if choice == 'r':
                return self.input_caro_board()
            else: 
                exit()
            
        return state
    


def main():
    begin = time.time()
    n = 15
    game_map = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', 'O', 'X', 'X', 'O', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'O', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'O', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                ]
    
    move_cnt = 15
                
    last_move = (8, 6)
    
    game = CaroGame(n, game_map, move_cnt, last_move)
    
    end = time.time()
    print(end - begin)
    
    
if __name__ == "__main__":
    main()