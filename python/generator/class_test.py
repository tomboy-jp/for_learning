class naming():

    count = 0

    def __init__(self, input_name):
        self.__name = input_name
        naming.count += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input_name):
        self.__name = input_name

    @classmethod
    def cnt(cls):
        print("names:{}".format(cls.count))

    @staticmethod
    def hello():
        print("goodbye")

his = naming("james")
his.name
his.name = "bob"
his.name

her = naming("anna")
her.name

naming.cnt()

naming.hello()
