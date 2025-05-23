class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)

    def media(self):
        self.m = float((self.nota1 + self.nota2)/2)
        print('A média do aluno {} é {}'.format(self.nome,self.m))

    def aprovado(self):
        if self.m >= 6:
            print('Aprovado!')
        
        else:
            print('Reprovado :(')


aluno1 = Aluno('Rafaela','4','6.5')
aluno2 = Aluno('Pedrinho','8','6.7')

aluno1.media(), aluno1.aprovado()
aluno2.media(), aluno2.aprovado()
