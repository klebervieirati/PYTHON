class Animal:
    def __init__(self,nome): # metodo construtor
        self.nome = nome
        print('Seu animal é um ',nome)

    def peso_animal(self,peso):
        self.peso = peso
        if (self.peso >10 ):
            print('Seu animal está acima do peso ')
        elif (self.peso > 5):
            print('Seu animal está com peso normal ')
        else:
            print ('Seu animal está magro ')

    def _aviso(self):    # metodo utilitario
        self.msg = 'Cuide bem do seu animal'
        return self.msg

    def observacao(self):
        print(self._aviso())

nome_animal = input('Informe o nome do Seu Animal ')
peso_animal = float(input('Informe o peso do animal '))


animal_1= Animal(nome_animal)
animal_1.peso_animal(peso_animal)
animal_1.observacao()
