#For Loop | Criando um Retangulo - Aula 9

'''
Criar um retangulo de 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()