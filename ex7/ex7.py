##########################################################################
# FILE : ex7.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex7 2020
# DESCRIPTION: Practice recursion.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################

BRACKETS = "()"
FULL = "*"
EMPTY = "."


def print_to_n(n):
    """Gets the integer number n, and prints all the integer numbers
       from 1 to n in an ascending order."""
    if n < 1:
        return
    print_to_n(n-1)
    print(n)


def digit_sum(n):
    """Gets non-negative integer number, and returns the sum of it's digits"""
    if n == 0:
        return 0
    return (n % 10) + digit_sum(n // 10)


def is_prime(n):
    """Gets an integer number n, and returns True if it is prime.
       Otherwise, False."""
    if n < 2:
        return False
    return has_divisor_smaller_than(n, int(n**0.5))


def has_divisor_smaller_than(n, i):
    """
    Checks if i divides n.
    :param n: Integer number.
    :param i: Divisor.
    :return: True if n is prime. Otherwise, False.
    """
    if i < 2:
        return True
    if n % i == 0:
        return False
    return has_divisor_smaller_than(n, i-1)


def play_hanoi(hanoi, n, src, dst, temp):
    """
    Solves the game 'Hanoi towers'.
    :param hanoi: The graphical game that the changes are made in.
    :param n: An integer number which represents the disks.
    :param src: Represents the pole which we want to move the disks from.
    :param dst: Represents the pole which we want to move the disks to.
    :param temp: Represents the third pole.
    """
    if n < 1:
        return
    if n == 1:
        hanoi.move(src, dst)
        return
    play_hanoi(hanoi, n - 1, src, temp, dst)
    hanoi.move(src, dst)
    play_hanoi(hanoi, n - 1, temp, dst, src)


def print_sequences(char_list, n):
    """
    Prints all the possible combinations of length n from char_list.
    :param char_list: A list of chars.
    :param n: Non-negative integer that represents the length of the
              possible sequences.
    """
    seq = [0]*n
    print_sequences_helper(char_list, n, seq, 0, 0)


def print_sequences_helper(char_list, n, seq, seq_idx, char_idx):
    """
    :param char_list: A list of chars.
    :param n: A non-negative integer that represents the length of the
              possible sequences.
    :param seq: A list of length n that will contain the sequences.
    :param seq_idx: Represents the current index of seq.
    :param char_idx: Represents the current index of char_list.
    """
    if n == 0:
        print("")
        return
    if n == seq_idx:
        print("".join(seq))
        return
    for char_idx in range(len(char_list)):
        seq[seq_idx] = char_list[char_idx]
        print_sequences_helper(char_list, n, seq, seq_idx+1, char_idx+1)


def print_no_repetition_sequences(char_list, n):
    """
    Prints all the possible combinations of length n from char_list,
    without repeating the same char in the combination.
    :param char_list: A list of chars.
    :param n: Non-negative integer that represents the length of the
              possible sequences.
    """
    no_repetition_helper(char_list, n, 0, len(char_list))


def no_repetition_helper(char_list, n, start, end):
    """
    :param char_list: A list of chars.
    :param n: A non-negative integer that represents the length of the
              possible sequences.
    :param start: Represents the current index of char_list.
    :param end: The length of char_list.
    """
    if n == 0:
        print("")
        return
    if start == n:
        print("".join(char_list[:n]))
        return
    for i in range(start, end):
        char_list[start], char_list[i] = char_list[i], char_list[start]
        no_repetition_helper(char_list, n, start+1, end)
        char_list[start], char_list[i] = char_list[i], char_list[start]


def parentheses(n):
    """Gets a non-negative integer number - n, and returns a list with all
    the strings with n pairs of legitimate parentheses."""
    if n <= 1:
        return [""] if n == 0 else [BRACKETS]
    result = parentheses(n - 1)
    temp = set()
    for item in result:
        for idx in range(len(item)//2 + 1):
            temp.add(item[:idx] + BRACKETS + item[idx:])
    return list(temp)


def flood_fill(image, start):
    """
    Switches char "." with "*" from the start point.
    :param image: A list of lists that contain the chars "*" and ".".
    :param start: A tuple of two integers - the first represents the indexes
                  of image, and the second represents the indexes of the
                  inner lists.
    """
    image[start[0]][start[1]] = FULL
    if image[start[0] - 1][start[1]] == EMPTY:
        flood_fill(image, (start[0] - 1, start[1]))
    if image[start[0] + 1][start[1]] == EMPTY:
        flood_fill(image, (start[0] + 1, start[1]))
    if image[start[0]][start[1] + 1] == EMPTY:
        flood_fill(image, (start[0], start[1] + 1))
    if image[start[0]][start[1] - 1] == EMPTY:
        flood_fill(image, (start[0], start[1] - 1))
