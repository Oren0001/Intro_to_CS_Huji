class Car:
    """
    Represents all the cars from the json file.
    """

    VERTICAL = 0
    HORIZONTAL = 1
    DIRECTIONS = "u", "d", "r", "l"
    UP, DOWN, RIGHT, LEFT = DIRECTIONS

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object.
        :param name: A string representing the car's name.
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)
                         location.
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL).
        """
        self.__length = length
        self.__orientation = orientation
        self.__name = name
        self.__location = location

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in.
        """
        coordinates = list()
        if self.__orientation == Car.VERTICAL:
            coordinates = [(self.__location[0]+i, self.__location[1])
                           for i in range(self.__length)]
        elif self.__orientation == Car.HORIZONTAL:
            coordinates = [(self.__location[0], self.__location[1]+j)
                           for j in range(self.__length)]
        return coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
                 permitted by this car.
        """
        movements = dict()
        if self.__orientation == Car.VERTICAL:
            movements["u"] = "Able to move upwards."
            movements["d"] = "Able to move downwards."
        elif self.__orientation == Car.HORIZONTAL:
            movements["r"] = "Able to move right."
            movements["l"] = "Able to move left."
        return movements

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
                 this move to be legal.
        """
        if movekey == Car.UP:
            return [(self.__location[0] - 1, self.__location[1])]
        elif movekey == Car.DOWN:
            return [(self.__location[0] + self.__length, self.__location[1])]
        elif movekey == Car.RIGHT:
            return [(self.__location[0], self.__location[1] + self.__length)]
        elif movekey == Car.LEFT:
            return [(self.__location[0], self.__location[1] - 1)]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise.
        """
        if self.possible_moves().get(movekey):
            row, col = self.__location
            if movekey == Car.UP:
                self.__location = (row - 1, col)
            if movekey == Car.DOWN:
                self.__location = (row + 1, col)
            if movekey == Car.RIGHT:
                self.__location = (row, col + 1)
            if movekey == Car.LEFT:
                self.__location = (row, col - 1)
            return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
