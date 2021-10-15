import pandas as pd

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    print(mes)
    vendas = pd.read_excel(f'{mes}.xlsx')
    print(vendas)