import helper
import sys
from board import Board
from car import Car

CAR_NAMES = "Y", "B", "O", "G", "W", "R"
CAR_LENGTH = range(2, 5)
ORIENTATION = (0, 1)
EXIT = "!"
ERROR_MSG = "Invalid input. Please try again."


class Game:
    """
    Runs a game of rush-hour.
    """

    DIRECTIONS = "u", "d", "r", "l"

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board.
        """
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.

        :return: None if the user wants to finish the game or the car has
                 reached the target. Otherwise, True.
        """
        while True:
            choice = input("Please enter the car's name and direction: ")
            if choice == EXIT:
                return
            if not self.check_user_input(choice) or \
                    not self.__board.move_car(choice[0], choice[2]):
                print(ERROR_MSG)
                continue
            if reach_target():
                print(self.__board)
                return
            return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while True:
            print(self.__board)
            if self.__single_turn():
                continue
            return

    def check_user_input(self, choice):
        """
        Checks if the user's input is valid or not.
        :param choice: User's input.
        :return: False if the input is invalid, otherwise True.
        """
        if choice[0] not in CAR_NAMES or choice[1] != "," \
                or choice[2] not in Game.DIRECTIONS:
            return False
        return True


def place_cars(board):
    """
    Places cars with valid parameters on the board.
    :return: True if one of the cars has already reached the target,
             otherwise None.
    """
    for key, value in helper.load_json(sys.argv[1]).items():
        if check_car_parameters(key, value[0], value[2]):
            continue
        car = Car(key, value[0], value[1], value[2])
        if board.add_car(car):
            if reach_target():
                return True


def check_car_parameters(name, length, orientation):
    """
    Checks if the car's parameters are valid or not.
    :param name: The car's name.
    :param length: The car's length.
    :param orientation: The car's orientation.
    :return: True if the parameters aren't valid, otherwise None.
    """
    if name not in CAR_NAMES or length not in CAR_LENGTH \
            or orientation not in ORIENTATION:
        return True


def reach_target():
    """
    :return: True if a car has reached the target, otherwise None.
    """
    if board.cell_content(board.target_location()):
        return True


if __name__ == "__main__":
    board = Board()
    if place_cars(board):
        print(board)
    else:
        game = Game(board)
        game.play()
