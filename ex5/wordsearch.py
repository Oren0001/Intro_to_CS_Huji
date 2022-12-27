##########################################################################
# FILE : wordsearch.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex5 2020
# DESCRIPTION: A Program that finds words in a matrix of letters.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################
import sys

DIRECTIONS = ("u", "d", "r", "l", "w", "x", "y", "z")
DIRECTION_ERROR_MSG = f"The directions must be only {DIRECTIONS}."
ARGS_ERROR_MSG = "The number of parameters is invalid."
FILE_ERROR_MSG = "The files must end with an empty line."
MATRIX_ERROR_MSG = "Each letter in the matrix must be separated by a comma."
WORD_ERROR_MSG = "Each line in the word list file must contain only one word."
NEW_LINE = "\n"


def check_input_args(args):
    """
    Checks whether or not the parameters meet the criteria.
    :param args: A list of strings that represent 4 parameters from
                 the command line.
    :return: Message error if there are errors, otherwise None.
    """
    args_result = check_args_existence(args)
    if args_result:
        return args_result
    word_result = check_word_file(args[0])
    if word_result:
        return word_result
    mat_result = check_matrix_file(args[1])
    if mat_result:
        return mat_result
    di_result = check_directions(args[3])
    if di_result:
        return di_result


def check_args_existence(args):
    if len(args) != 4:
        return ARGS_ERROR_MSG
    try:
        with open(args[0]) as word_file, open(args[1]) as matrix_file:
            pass
    except FileNotFoundError as error_msg:
        return error_msg


def check_word_file(word_file):
    """Checks if the parameter - word_file, meet the criteria.
       Returns informative message if it doesnt."""
    with open(word_file) as f:
        for line in f:
            if not line.strip().isalpha():
                return WORD_ERROR_MSG
        try:
            if line[-1:] != NEW_LINE:
                return FILE_ERROR_MSG
        except UnboundLocalError:
            return


def check_matrix_file(matrix_file):
    """Checks if the parameter - matrix_file, meet the criteria.
       Returns informative message if it doesnt."""
    with open(matrix_file) as f:
        for line in f:
            for i, char in enumerate(line.strip()):
                if not i % 2 and not char.isalpha():
                    return MATRIX_ERROR_MSG
                elif i % 2 and char != ",":
                    return MATRIX_ERROR_MSG
        try:
            if line[-1:] != NEW_LINE:
                return FILE_ERROR_MSG
        except UnboundLocalError:
            return


def check_directions(directions):
    """Checks if the parameter - directions, meet the criteria.
       Returns informative message if it doesnt."""
    for char in directions:
        if char not in DIRECTIONS:
            return DIRECTION_ERROR_MSG


def read_wordlist_file(filename):
    """
    :param filename: File that includes a list of words.
    :return: A list of words from the given file.
    """
    words = list()
    with open(filename) as f:
        for line in f:
            words.append(line.strip())
    return words


def read_matrix_file(filename):
    """
    :param filename: File that includes the matrix.
    :return: A list of lists. Each list represents a line of letters
             in the matrix.
    """
    matrix = list()
    with open(filename) as f:
        for line in f:
            matrix.append(line.strip().split(","))
    return matrix


def find_words_in_matrix(word_list, matrix, directions):
    """ Searches for the words in matrix according to the given directions.
    :param word_list: A List of words to search in the matrix.
    :param matrix: A list of lists which represents the letters matrix.
    :param directions: A string that represents the directions to search for.
    :return: A list of tuples that contain two elements: the first is a word,
            and the second is the number of times it appears in the matrix."""
    counter = dict()
    for direction in directions:
        if direction == DIRECTIONS[0]:
            handle_u_direction(word_list, matrix, counter)
        if direction == DIRECTIONS[1]:
            handle_d_direction(word_list, matrix, counter)
        if direction == DIRECTIONS[2]:
            handle_r_direction(word_list, matrix, counter)
        if direction == DIRECTIONS[3]:
            handle_l_direction(word_list, matrix, counter)
        if direction == DIRECTIONS[4]:
            handle_w_direction(word_list, matrix, counter)
        if direction == DIRECTIONS[5]:
            handle_x_direction(word_list, matrix, counter)
        if direction == DIRECTIONS[6]:
            handle_y_direction(word_list, matrix[:], counter)
        if direction == DIRECTIONS[7]:
            handle_z_direction(word_list, matrix, counter)
    return list(counter.items())


def search_word(word_list, combination, counter):
    """
    Searches for the words in the combination.
    :param word_list: A List of words to search in the combination.
    :param combination: A string that represents a line in the matrix.
    :param counter: A dictionary. The keys are words found in the matrix,
                    and the values are the number of times they appeared.
    """
    for word in word_list:
        while word in combination:
            if counter.get(word):
                counter[word] += 1
            else:
                counter[word] = 1
            combination = combination.replace(word, word[-1:], 1)


def handle_u_direction(word_list, matrix, counter):
    """Searches for the words in 'u' direction in the matrix."""
    for column in range(len(matrix[0])):
        combination = str()
        for row in range(len(matrix)-1, -1, -1):
            combination += matrix[row][column]
        search_word(word_list, combination, counter)


def handle_d_direction(word_list, matrix, counter):
    """Searches for the words in 'd' direction in the matrix."""
    for column in range(len(matrix[0])):
        combination = str()
        for row in range(len(matrix)):
            combination += matrix[row][column]
        search_word(word_list, combination, counter)


def handle_r_direction(word_list, matrix, counter):
    """Searches for the words in 'r' direction in the matrix."""
    for row in matrix:
        search_word(word_list, "".join(row), counter)


def handle_l_direction(word_list, matrix, counter):
    """Searches for the words in 'l' direction in the matrix."""
    for row in matrix:
        search_word(word_list, "".join(reversed(row)), counter)


def handle_w_direction(word_list, matrix, counter):
    """Searches for the words in 'w' direction in the matrix."""
    n = len(matrix[0])
    m = len(matrix)
    for row in range(m-1, -1, -1):
        combination = str()
        column = 0
        while row >= 0 and column <= n-1:
            combination += matrix[row][column]
            row, column = row - 1, column + 1
        search_word(word_list, combination, counter)
    for column in range(1, n):
        combination = str()
        row = m - 1
        while column <= n-1:
            combination += matrix[row][column]
            row, column = row - 1, column + 1
        search_word(word_list, combination, counter)


def handle_x_direction(word_list, matrix, counter):
    """Searches for the words in 'x' direction in the matrix."""
    reversed_matrix = list()
    for row in matrix:
        reversed_matrix.append(list(reversed(row)))
    handle_w_direction(word_list, reversed_matrix, counter)


def handle_y_direction(word_list, matrix, counter):
    """Searches for the words in 'y' direction in the matrix."""
    matrix.reverse()
    handle_w_direction(word_list, matrix, counter)


def handle_z_direction(word_list, matrix, counter):
    """Searches for the words in 'z' direction in the matrix."""
    reversed_matrix = list()
    for row in reversed(matrix):
        reversed_matrix.append(list(reversed(row)))
    handle_w_direction(word_list, reversed_matrix, counter)


def write_output_file(results, output_filename):
    """
    The function creates a file using output_filename, and will write
    in it the search results of the letters in the matrix.
    """
    last_word = results.pop()
    with open(output_filename, "w") as f:
        for result in results:
            f.write(str(result).strip("(')").replace("', ", ",") + NEW_LINE)
        f.write(str(last_word).strip("(')").replace("', ", ","))


def main():
    """Calls all the functions in this program to execute it."""
    sys.argv[4] = "".join(set(sys.argv[4]))
    test_result = check_input_args(sys.argv[1:])
    if test_result:
        print(test_result)
        return
    else:
        word_lst = read_wordlist_file(sys.argv[1])
        matrix = read_matrix_file(sys.argv[2])
        search_results = find_words_in_matrix(word_lst, matrix, sys.argv[4])
        write_output_file(search_results, sys.argv[3])


if __name__ == "__main__":
    main()
