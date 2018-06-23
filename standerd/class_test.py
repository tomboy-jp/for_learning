class names():

    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input_name):
        self.__name = input_name

first = names("tom")
first.name
first.name = "bob"
