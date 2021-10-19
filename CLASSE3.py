class AreaQuadrado:
    def __init__(self,lado1,lado2):
        self.l1 = lado1
        self.l2 = lado2
        print ('Método construtor ok!!!!')

    def calcula_area(self):
        area = self.l1 * self.l2
        return area
lado_1 = int(input('Digite o Primeiro lado do Quadrado..: '))
lado_2 = int(input('Digite o Segundo lado do Quadrado..: '))

quandrado_1 = AreaQuadrado(lado_1,lado_2)
area = quandrado_1.calcula_area()
print (area)