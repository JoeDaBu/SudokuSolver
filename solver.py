def print_puzzle(puzzle):
    for i in range(9):
        x = 0
        while x<9:
            if x == 0:
                print("| ", end="")
            else:
                print(end=" ")
            print(puzzle[i][x], end="")
            if (x+1) % 3 == 0 and x != 0:
                print(end=" |")
            if x % 8 == 0 and x != 0:
                print()
            x += 1

x = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
print_puzzle(x)

class Solver:
    def __init__(self,puzzle):
        self.solve_puzzle(puzzle)
    def __repr__(self):
        return print_puzzle(self.puzzle)
    def solve_puzzle(self, puzzle):
        self.puzzle = puzzle




