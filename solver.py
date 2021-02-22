from itertools import count

BLANK = " "


def print_puzzle(puzzle):
    for i in range(9):
        x = 0
        while x < 9:
            if x == 0:
                print("| ", end="")
            else:
                print(end=" ")
            print(puzzle[i][x], end="")
            if (x + 1) % 3 == 0 and x != 0:
                print(end=" |")
            if x % 8 == 0 and x != 0:
                print()
            x += 1


def contains_duplicate(numbers):
    for number in numbers:
        if numbers.count(number) != 1:
            return True
    return False


def row_values(puzzle, i):
    values = []
    for number in puzzle[i]:
        if number != BLANK:
            values.append(number)
    if contains_duplicate(values):
        raise Exception("Duplicate values")
    return values


def column_values(puzzle, x):
    values = []
    for i in range(9):
        value = puzzle[i][x]
        if value != BLANK:
            values.append(value)
    if contains_duplicate(values):
        raise Exception("Duplicate values")
    return values


def box_values(puzzle, i, x):
    box_y = (i // 3) * 3
    box_x = (x // 3) * 3
    values = []
    for a in range(3):
        for b in range(3):
            value = puzzle[box_y + a][box_x + b]
            if value != BLANK:
                values.append(value)
    if contains_duplicate(values):
        raise Exception("Duplicate values")
    return values


def union(row, column, box=None):
    if box is None:
        box = set()
    list_union = list(set().union(row, column, box))
    return list_union


def contrast(possible_values, diff):
    list_difference = list(set(possible_values) - set(diff))
    return list_difference


def find_possible_values(puzzle, i, x):
    possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = row_values(puzzle, i)
    column = column_values(puzzle, x)
    box = box_values(puzzle, i, x)
    possible_values = contrast(possible_values, union(row, column, box))
    if len(possible_values) == 0:
        raise NoPossibilities(possible_values)
    return possible_values


def solve_puzzle(puzzle):
    try:
        return solve(puzzle, 0, 0)
    except IncorrectVariant:
        print("No Solution")
        raise NoSolution


def solve(puzzle, i, x):
    i = i
    x = x
    while i < 9:
        while x < 9:
            if puzzle[i][x] == BLANK:
                try:
                    possible_values = find_possible_values(puzzle, i, x)
                except NoPossibilities:
                    raise IncorrectVariant(puzzle)

                for value in possible_values:
                    puzzle[i][x] = value
                    try:
                        return solve(puzzle, i, x)
                    except IncorrectVariant:
                        puzzle[i][x] = BLANK

                # except IncorrectVariant:
                #     raise NoSolution(puzzle)
                if puzzle[i][x] == BLANK:
                    raise IncorrectVariant(puzzle)

            x += 1
        x = 0
        i += 1
    return puzzle


class Solver:
    def __init__(self, puzzle):
        self.solve_puzzle(puzzle)

    def __repr__(self):
        return print_puzzle(self.puzzle)

    def __str__(self):
        return str(self.puzzle)

    def solve_puzzle(self, puzzle):
        self.puzzle = solve_puzzle(puzzle)


class NoPossibilities(Exception):
    def __init__(self, possible_values, message="Puzzle has no further possibilities"):
        self.message = message
        self.values = possible_values
        super(NoPossibilities, self).__init__(self.message)

    def __str__(self):
        return f"{print(list(self.values))} -> {self.message}"


class NoSolution(Exception):
    def __init__(self, puzzle, message="Puzzle has no solution"):
        self.message = message
        self.puzzle = puzzle
        super(NoSolution, self).__init__(self.message)

    def __str__(self):
        return f"{print_puzzle(self.puzzle)} -> {self.message}"


class IncorrectVariant(Exception):
    """Raised when the Sudoku variant is impossible"""

    def __init__(self, puzzle, message="Puzzle Variant is not solvable"):
        self.puzzle = puzzle
        self.message = message
        super(IncorrectVariant, self).__init__(self.message)

    def __str__(self):
        return f"{print_puzzle(self.puzzle)} -> {self.message}"
