from Animal import Animal


class Dog(Animal):

    __instance = None

    @staticmethod
    def get_instance():
        if Dog.__instance is None:
            Dog()
        return Dog.__instance

    def __init__(self):
        if Dog.__instance is None:
            Dog.__instance = self
        else:
            raise Exception("Instância dessa classe ja existe")

    def sound(self):
        print("Auau")
