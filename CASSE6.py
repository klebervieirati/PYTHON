class Carro():
    def __init__(self,marca,cor,ano,inicial,final):
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.i = inicial
        self.f = final

    def calc_ano_fabrica(self):
        tempouso = 2021 - self.ano
        print('CARRO COM {} ANOS DE USO '.format(tempouso))
    def calc_kilometragem(self):
        kilometragem = self.f - self.i
        print('SEU CARRO RODOU {} QUILOMETROS '.format(kilometragem))
    def dados_carro(self):
        print('CARRO DE MARCA.....:{} '.format(self.marca))
        print('CARRO DE COR ......:{} '.format(self.cor))
        print('CARRO FABRICADO EM.:{} '.format(self.ano))

def linha():
    print('-' * 20)

m = input('DIGITE A MARCA DO CARRO...............: ')
c = input('DIGITE A COR DO CARRO.................: ')
a = int(input('DIGITE O ANO DE FABRICAÇÃO........: '))
i = float(input('DIGITE A QUILOMETRAGEM INICIAL..: '))
f = float(input('DIGITE A QUILOMETRAGEM FINAL....: '))

                               # objeto instanciado e passado os parametros para classe
carro_1 = Carro(m,c,a,i,f)
                              # métodos instaciados apartir do objeto (carro_1),que seram impressos na tela
linha()
carro_1.dados_carro()
linha()
carro_1.calc_ano_fabrica()
linha()
carro_1.calc_kilometragem()
linha()


#print('CARRO COM {} ANOS DE USO '.format(carro_1.calc_ano_fabrica()))
#print('SEU CARRO RODOU {} QUILOMETROS '.format(carro_1.calc_kilometragem()))
