class Retangulo:
    def __init__(self, h, l):
        self.altura = float(h)
        self.largura = float(l)

    def area(self):
        self.a = self.altura * self.largura
        print('A área do retâgulo é',self.a)

    def perimetro(self):
        self.p = (self.altura*2) + (self.largura*2)
        print('O perímetro é',self.p)

retangulo1 = Retangulo('3','10.5')

retangulo1.area()
retangulo1.perimetro()