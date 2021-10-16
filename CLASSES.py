'''Classe para calcular a Area de um quarto d'''
class Area:
    def __init__(self,largura,altura): # método construtor da classe
        self.lar = largura
        self.alt = altura

    def area_quarto(self):
        area= self.alt * self.lar
        return 'A Area do Quarto é ' + str(area)

a = int(input('Digite a Altura do Quarto..: '))
l = int(input('Digite a Largura do Quarto..: '))
teste = Area(a,l)
c = teste.area_quarto()
print(c)
