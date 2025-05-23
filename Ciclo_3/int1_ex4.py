class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def apresentar(self):
        print('Esse animal se chama', self.nome)

    def falar(self):
        print('Este animal faz algum som')

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    
    def falar(self):
        print('Auauuuu!')

class Gato(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print('Miauuuuu!')


animal1 = Cachorro('Bilu')
animal2 = Gato('Mimi')


animal1.apresentar()
animal1.falar()
animal2.apresentar()
animal2.falar()