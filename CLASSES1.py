class Calculadora:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

    def calcular(self):
        total = self.n1 * self.n2
        return total
a = int(input('Digite o Primeiro Número..: '))
b = int(input('Digite o Seguando Número..: '))
numeros = Calculadora (a,b)
res = numeros.calcular()
print ('A multiplicação entre {} e {} é {}'.format (a,b,res))