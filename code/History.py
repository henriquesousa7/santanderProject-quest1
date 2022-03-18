class History():

    __instance = None

    @staticmethod
    def get_instance():
        if History.__instance is None:
            History()
        return History.__instance

    def __init__(self):
        if History.__instance is None:
            History.__instance = self
            self._arrayHistory = []
        else:
            raise Exception("Instância dessa classe ja existe")

    @property
    def arrayHistory(self):
        return self._arrayHistory

    def appendHistory(self, value):
        self._arrayHistory.append(value)
