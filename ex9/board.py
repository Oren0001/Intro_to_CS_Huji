EMPTY_CELL = "_"


class Board:
    """
    Represents the game's board.
    """
    SIDE = 7

    def __init__(self):
        """A constructor for a Board object."""
        self.__board = dict()
        for cell in self.cell_list():
            self.__board[cell] = None
        self.__cars = dict()

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board.
        """
        board = [[] for i in range(Board.SIDE)]
        for coordinate, value in self.__board.items():
            if value is None:
                temp = EMPTY_CELL
            else:
                temp = value
            board[coordinate[0]].insert(coordinate[1], temp)
        return "\n".join([" ".join(row) for row in board])

    def cell_list(self):
        """ This function returns the coordinates of cells in this board.
        :return: list of coordinates.
        """
        coordinates = [(row, col) for row in range(Board.SIDE)
                       for col in range(Board.SIDE)]
        coordinates.append((3, 7))
        return coordinates

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board.
        :return: list of tuples of the form (name, movekey, description)
                 representing legal moves.
        """
        movements = list()
        for car in self.__cars.values():
            for move, description in car.possible_moves().items():
                if not self.cell_content(car.movement_requirements(move)[0]):
                    movements.append((car.get_name(), move, description))
        return movements

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
         filled for victory.
        :return: (row,col) of goal location.
        """
        return 3, 7

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check.
        :return:The name if the car in coordinate, None if empty.
        """
        try:
            if self.__board[coordinate] is None:
                return
            return self.__board[coordinate]
        except KeyError:
            return -1

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add.
        :return: True upon success. False if failed.
        """
        for coordinate in car.car_coordinates():
            if self.cell_content(coordinate):
                return False
        self.add_car_name(car)
        self.__cars[car.get_name()] = car
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move.
        :param movekey: Key of move in car to activate.
        :return: True upon success, False otherwise.
        """
        moves = self.possible_moves()
        if moves:
            for move in moves:
                if move[0] == name and move[1] == movekey:
                    car = self.__cars[name]
                    self.remove_car_name(car)
                    car.move(movekey)
                    self.add_car_name(car)
                    return True
        return False

    def add_car_name(self, car):
        """
        Adds the car's name to specific coordinates.
        :param car: An object of type Car.
        :return: None.
        """
        for coordinate in car.car_coordinates():
            self.__board[coordinate] = car.get_name()

    def remove_car_name(self, car):
        """
        Removes the car's name from specific coordinates.
        :param car: An object of type Car.
        :return: None.
        """
        for coordinate in car.car_coordinates():
            self.__board[coordinate] = None
