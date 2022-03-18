from Cat import Cat
from Dog import Dog
from History import History

if __name__ == "__main__":

    dog = Dog()
    cat = Cat()
    history = History()

    while True:

        option = int(input("Digite o valor [1-Gato, 2-Cachorro, 4-Histórico, {QUALQUER OUTRO VALOR}-Sair]: "))

        if option == 1:
            cat.sound()
            history.appendHistory("1 Miau")
        elif option == 2:
            dog.sound()
            history.appendHistory("2 Auau")
        elif option == 3:
            print(history.arrayHistory)
        else:
            print("Saindo...")
            break

    # Teste Singleton

    # dog2 = Dog()  # Exception sera printado na tela
    # dog3 = Dog.get_instance()

    # print(dog)  # Primeira variavel instanciada
    # print(dog2)  # Segunda variavel instanciada
    # print(dog3)  # Segunda variavel instanciada
