from solver import row_values, box_values, column_values

def valid_puzzle(puzzle):
    for i in range(9):
        x = 0
        while x < 9:
            try:
                if puzzle[i][x] == None:
                    return False
            except Exception:
                return False
            x += 1
    return True

def array_same(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in array1:
        if i not in array2:
            return False
    return True

def validate_sol(puzzle):
    base = row_values(puzzle,0)
    for i in range(9):
        x = 0
        while x < 9:
            if not (array_same(base,row_values(puzzle,i)) and
                    array_same(box_values(puzzle,i,x),base) and
                    array_same(base,column_values(puzzle,x))):
                return False
            x += 1
    return True