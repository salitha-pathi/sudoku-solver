numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_row_values(row_id, table):
    return [int(x.value) for x in table[row_id]]


def get_column_values(col_id, table):
    column = []
    for row_id in range(9):
        column.append(int(table[row_id][col_id].value))
    return column

def get_cage_values(row_id, col_id, table):
    cage_row_id = row_id // 3
    cage_col_id = col_id // 3

    my_cage_values = []
    for _row_id in range(cage_row_id*3, cage_row_id*3+3):
        for _col_id in range(cage_col_id*3, cage_col_id*3+3):
            my_cage_values.append(int(table[_row_id][_col_id].value))
    return  my_cage_values


def solve(table):
    for row_id in range(9):
        for col_id in range(9):
            if table[row_id][col_id].is_solved: continue
            row_values = get_row_values(row_id, table)
            col_values = get_column_values(col_id, table)
            cage_values = get_cage_values(row_id, col_id, table)

            existing_impossibilities = row_values + col_values + cage_values

            possibilities = [x for x in numbers if x not in existing_impossibilities]
            table[row_id][col_id].set(possibilities)
    return table


def is_solved(table):
    for row_id in range(9):
        for col_id in range(9):
            if not table[row_id][col_id].is_solved: return False

    return True
