

class Computador:
    def __init__(self):
        self.marca = 'Asua'
        self.memoria = '8gb'
        self.placa_vidio = 'Nvidia'
    def ligado(self):
        return 'teste método'
computador1 = Computador()
print(computador1.placa_vidio)
print(computador1.ligado())

computador2 = Computador()
computador3 = Computador()

