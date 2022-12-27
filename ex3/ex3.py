##########################################################################
# FILE : ex3.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex3 2020
# DESCRIPTION: Loops.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################

EMPTY_INPUT = ""


def input_list():
    """The function gets numbers from the user, and returns a list
    that contains the numbers and their sum at the end."""
    result = list()
    sum_all = 0
    while True:
        user_input = input()
        if user_input == EMPTY_INPUT:
            break
        result.append(float(user_input))
        sum_all += float(user_input)
    result.append(sum_all)
    return result


def inner_product(vec_1, vec_2):
    """The function gets two lists of numbers, and returns
    their inner product."""
    result = 0
    if len(vec_1) != len(vec_2):
        return
    for index in range(len(vec_1)):
        result += vec_1[index] * vec_2[index]
    return result


def sequence_monotonicity(sequence):
    """The function gets a list of numbers, and returns
    the type of monotonicity it has."""
    result = [True, True, True, True]
    for index in range(1, len(sequence)):
        if result[0] and sequence[index-1] > sequence[index]:
            result[0] = False
        if result[1] and sequence[index-1] >= sequence[index]:
            result[1] = False
        if result[2] and sequence[index-1] < sequence[index]:
            result[2] = False
        if result[3] and sequence[index-1] <= sequence[index]:
            result[3] = False
    return result


def monotonicity_inverse(def_bool):
    """The function gets 4 boolean values, and returns a list
    of numbers which represent the type of monotonicity."""
    if def_bool == [True, True, False, False]:
        return [3, 5.55, 20, 100]
    elif def_bool == [True, False, False, False]:
        return [5.55, 5.55, 20, 100]
    elif def_bool == [True, False, True, False]:
        return [20, 20, 20, 20]
    elif def_bool == [False, False, True, True]:
        return [100, 20, 5.55, 3]
    elif def_bool == [False, False, True, False]:
        return [100, 20, 5.55, 5.55]
    elif def_bool == [False, False, False, False]:
        return [5.55, 3, 100, 20]
    else:
        return


def primes_for_asafi(n):
    """The function gets non-negative integer number - n, and returns
    a list with the first n prime numbers."""
    result = list()
    is_prime = 2
    while len(result) < n:
        for divisor in range(2, int(is_prime**0.5)+1):
            if is_prime % divisor == 0:
                break
        else:
            result.append(is_prime)
        is_prime += 1
    return result


def sum_of_vectors(vec_lst):
    """The functions gets a list of vectors, and returns their sum."""
    if len(vec_lst) == 0:
        return
    result = list()
    for vec_ind in range(len(vec_lst[0])):
        sum_all = 0
        for lst_ind in range(len(vec_lst)):
            sum_all += vec_lst[lst_ind][vec_ind]
        result.append(sum_all)
    return result


def num_of_orthogonal(vectors):
    """The function gets a list of vectors, and returns the
    number of pairs of vectors that perpendicular to each other."""
    result = 0
    n = len(vectors)
    for vec_1 in range(n - 1):
        for vec_2 in range(vec_1 + 1, n):
            if inner_product(vectors[vec_1], vectors[vec_2]) == 0:
                result += 1
    return result
