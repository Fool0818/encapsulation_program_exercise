class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self):
        self.__speed = Fan.SLOW
        self.__on = False
        self.__radius = 5.0
        self.__color = "blue"

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed

    def getOn(self):
        return self.__on

    def setOn(self, on):
        self.__on = on

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color