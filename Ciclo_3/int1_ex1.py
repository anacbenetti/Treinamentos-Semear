class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print('Meu nome é {} e tenho {} anos.'.format(self.nome, self.idade))

pessoa1 = Pessoa('Ana Cecília', '21')
pessoa2 = Pessoa('Sofia', '19')

pessoa1.apresentar()
pessoa2.apresentar()