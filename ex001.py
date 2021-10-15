n1 = int(input('digite uma valor '))
n2 = int(input('digite outro valor '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('a soma é {}\na multiplicacao é {}\na divisao é {:.5f}'.format(s,m,d),end=' **** ')
print('a divisao inteira é {} e a potencia é {}'.format(di,e))