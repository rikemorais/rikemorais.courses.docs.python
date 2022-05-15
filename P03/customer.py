class Customer:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def nome(self, name):
        self.__name = name
