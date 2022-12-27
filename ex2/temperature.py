##########################################################################
# FILE : temperature.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Checks if at least 2 of 3 days' temperature are higher than
#              a threshold temperature.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################


def is_it_summer_yet(threshold, temp1, temp2, temp3):
    """
    :param threshold: Threshold temperature.
    :param temp1: Day 1 temperature.
    :param temp2: Day 2 temperature.
    :param temp3: Day 3 temperature.
    :return: True if at least 2 of 3 days' temperature are higher than
             the threshold temperature. Otherwise, False.
    """
    if (threshold < temp1) and (threshold < temp2):
        return True
    elif (threshold < temp2) and (threshold < temp3):
        return True
    elif (threshold < temp1) and (threshold < temp3):
        return True
    else:
        return False
