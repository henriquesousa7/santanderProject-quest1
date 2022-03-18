from Animal import Animal


class Cat(Animal):

    __instance = None

    @staticmethod
    def get_instance():
        if Cat.__instance is None:
            Cat()
        return Cat.__instance

    def __init__(self):
        if Cat.__instance is None:
            Cat.__instance = self
        else:
            raise Exception("Instância dessa classe ja existe")

    def sound(self):
        print("Miau")