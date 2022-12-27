##########################################################################
# FILE : ex8.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex8 2020
# DESCRIPTION: Solve nonogram.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################
import copy


def get_row_variations(row, blocks):
    """
    Gets a line from the nonogram board and it's constraints, and returns
    all the possible paintings according to the constrains.
    :param row: A list of numbers: 0, 1 and -1. It represents a partial
                painting of a row.
    :param blocks: A list of non-negative integers.
    :return: A list of all the possible paintings.
    """
    paint_options = []
    if row.count(1) + row.count(-1) < sum(blocks) or blocks == list():
        return paint_options
    row_copy = row[:]
    temp = row[:]
    return variations_helper(row_copy, blocks, 0, temp, paint_options)


def variations_helper(row, blocks, blocks_idx, temp, paint_options):
    """ Helps execute the function get_row_variations.
    :param blocks_idx: The current index of blocks.
    :param temp: A shallow copy of row.
    :param paint_options: A list of all the possible paintings.
    :return: paint_options. """
    if -1 not in temp:
        constraints = find_line_constraints(temp)
        if constraints == blocks:
            paint_options.append(temp[:])
            return paint_options
    if temp.count(1) > sum(blocks): return paint_options
    if blocks_idx == len(blocks): blocks_idx -= 1
    for idx in range(len(row)):
        if temp[idx] == 1 and\
                temp[:idx + 1].count(1) == sum(blocks[:blocks_idx + 1]):
            blocks_idx += 1
        elif temp[idx] == -1:
            row = temp[:]
            temp = paint_unknown_square(idx, blocks, blocks_idx, temp)
            variations_helper(row, blocks, blocks_idx+1, temp, paint_options)
            if len(row[idx:]) < sum(blocks[blocks_idx:]): return paint_options
            temp = row[:]
            temp[idx] = 0
            variations_helper(row, blocks, blocks_idx, temp, paint_options)
    return paint_options


def find_line_constraints(row):
    """Gets a row of the nonogram board which contains only 1 and 0,
       and returns a list of it's constraints."""
    row = str(row).strip("[]").replace(", ", "").split("0")
    return [len(i) for i in row if i.isdigit()]


def paint_unknown_square(idx, blocks, blocks_ind, row):
    """ Switches -1 to 1 or 0 according to the constraints.
    :param idx: The current index of row.
    :param blocks: A list of non-negative integers.
    :param blocks_ind: The current index of blocks.
    :param row: A list of numbers: 0, 1 and -1. It represents a partial
                painting of a row.
    :return: An updated row according to the constraints. """
    if blocks_ind == len(blocks):
        row[idx] = 1
    else:
        for i in range(blocks[blocks_ind]):
            start = idx + 1 - blocks[blocks_ind] + i
            end = idx + 1 + i
            if row[start:end].count(1) + row[start:end].count(-1) == \
                    blocks[blocks_ind]:
                for j in range(start, end):
                    row[j] = 1
                if end < len(row) and row[end] == -1:
                    row[end] = 0
                break
            else:
                row[idx] = 1
    return row


def get_intersection_row(rows):
    """Gets a list of rows, and returns the common constraint to them all."""
    n = len(rows)
    if n == 1:
        return rows[0]
    res = list()
    for element in range(len(rows[0])):
        for idx in range(0, n - 1):
            if rows[idx][element] != rows[idx+1][element]:
                res.append(-1)
                break
        else:
            res.append(rows[idx][element])
    return res


def solve_easy_nonogram(constraints):
    """
    Solves an easy nonogram game.
    :param constraints: A list of two lists - the first represents the
                        constraints of the rows, and the second represents
                        the constraints of the columns.
    :return: If possible, a list of lists that represents the solved
             board of nonogram. Otherwise, None.
    """
    if constraints[0] == list() or constraints[1] == list():
        return list()
    board = create_board(constraints)
    return infer_from_constraints(board, constraints)


def create_board(constraints):
    """Creates a nonogram board according to the constraints.
       Returns a list of lists that represent the nonogram board."""
    board = list()
    for row in range(len(constraints[0])):
        board.append([])
        for column in range(len(constraints[1])):
            board[row].append(-1)
    return board


def infer_from_constraints(board, constraints):
    """
    Paints each square of the board according to the constraints,
    and overlap in the rows and columns.
    :param board: A list of lists that represent the nonogram board.
    :param constraints: A list of two lists - the first represents the
                        constraints of the rows, and the second represents
                        the constraints of the columns.
    :return: If possible, a solved board of nonogram. Otherwise, None.
    """
    rows = len(board)
    columns = len(board[0])
    board = overlap_options(board, constraints, rows, columns)
    return execute_constraints(board, constraints, rows, columns)


def overlap_options(board, constraints, rows, columns):
    """ Paints each square of the board according to the overlap
     in the rows and columns.
    :param rows: The number of rows in the board.
    :param columns: The number of columns in the board.
    :return: An updated board. """
    try:
        for row in range(rows):
            row_cons = constraints[0][row]
            if len(row_cons) > 0 and max(row_cons) > columns/2:
                for overlap in range(columns-max(row_cons), max(row_cons)):
                    board[row][overlap] = 1
        for column in range(columns):
            column_cons = constraints[1][column]
            if len(column_cons) > 0 and max(column_cons) > rows/2:
                for overlap in range(rows-max(column_cons), max(column_cons)):
                    board[overlap][column] = 1
        return board
    except:
        return


def execute_constraints(board, constraints, rows, columns):
    """ Paints each square of the board according to the constraints.
    :param rows: The number of rows in the board.
    :param columns: The number of columns in the board.
    :return: An updated board. """
    try:
        cons_sum = 0
        for constraint in constraints[0]:
            cons_sum += sum(constraint)
        while True:
            row_change = execute_row_constraints(board, constraints, rows)
            board = copy.deepcopy(row_change)
            column_change, counter = \
                execute_column_constraints(board, constraints, rows, columns)
            if counter == cons_sum or row_change == column_change:
                return column_change
    except:
        return


def execute_row_constraints(board, constraints, rows):
    """ Paints each square of the board according to the row constraints.
    :param rows: The number of rows in the board.
    :return: An updated board. """
    try:
        for row in range(rows):
            paint_options = get_row_variations(board[row], constraints[0][row])
            if paint_options == list():
                pass
            else:
                intersection_row = get_intersection_row(paint_options)
                board[row] = intersection_row
        return board
    except:
        return


def execute_column_constraints(board, constraints, rows, columns):
    """ Paints each square of the board according to the column constraints.
    :param rows: The number of rows in the board.
    :param columns: The number of columns in the board.
    :return: A tuple of two items - the first is an updated board,
             and the second is the sum of the values in the board."""
    try:
        counter = 0
        for column in range(columns):
            temp_column = list()
            for row in range(rows):
                temp_column.append(board[row][column])
            paint_options = get_row_variations(temp_column,
                                               constraints[1][column])
            if paint_options == list():
                pass
            else:
                intersection_column = get_intersection_row(paint_options)
                for row in range(rows):
                    board[row][column] = intersection_column[row]
                    counter += board[row][column]
        return board, counter
    except:
        return


def solve_nonogram(constraints):
    """
    Solves all nonogram games.
    :param constraints: A list of two lists - the first represents the
                        constraints of the rows, and the second represents
                        the constraints of the columns.
    return: A list of lists that represents the solved nonogram boards.
    """
    solved = list()
    board = create_board(constraints)
    solve_nonogram_helper(board, constraints, solved, 0)
    return solved


def solve_nonogram_helper(board, constraints, solved, idx):
    """ Helps execute the function solve_nonogram.
    :param board: A list of lists that represent the nonogram board.
    :param constraints: A list of two lists - the first represents the
                        constraints of the rows, and the second represents
                        the constraints of the columns.
    :param solved: A list that contains all the solved boards.
    :param idx: The current index of the board. """
    board = infer_from_constraints(board, constraints)
    if idx == len(board):
        solved.append(board)
        return
    if sum(board[idx]) == sum(constraints[0][idx]):
        solved.append(board)
        return
    row_variations = get_row_variations(board[idx], constraints[0][idx])
    for variation in row_variations:
        temp = copy.deepcopy(board)
        board[idx] = variation
        solve_nonogram_helper(board, constraints, solved, idx+1)
        board = temp
    return


def count_row_variation(length, blocks):
    """Gets a length of a row and a list of non-negative integers,
       and returns the number of possible paintings of the row. """
    lst = [-1]*length
    counter = [0]
    count_variation_helper(lst, blocks, 0, counter, 0, length)
    return counter[0]


def count_variation_helper(lst, blocks, blocks_idx, counter, start, end):
    """ Helps execute the function count_row_variations.
    :param lst: A list that contains only -1 and 1.
    :param blocks: A list of non-negative integers.
    :param blocks_idx: The current index of blocks.
    :param counter: A list that contains the number of possible
                    paintings of the row.
    :param start: The current index of lst.
    :param end: The length of lst. """
    if lst.count(1) == sum(blocks):
        counter[0] += 1
        return
    if blocks_idx == len(blocks) or start >= end:
        return
    for idx in range(start, end):
        temp = lst[:]
        try:
            for i in range(idx, idx + blocks[blocks_idx]):
                lst[i] = 1
        except IndexError:
            return
        count_variation_helper(lst, blocks, blocks_idx + 1, counter,
                               idx + blocks[blocks_idx] + 1, end)
        lst = temp


def count_row_variations(length, blocks, row=None):
    if row is None:
        return count_row_variation(length, blocks)
