# Desafios com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade log abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''

'''
    Converter as listas turno_dia, turno_noite e tem_carro em sets, 
    pois os sets são mais eficientes para operações de união, interseção e diferença.

    Utilizar operações de conjuntos (sets) para encontrar a interseção entre 
    funcionários que têm carro e trabalham durante o dia, aqueles que têm carro e 
    trabalham durante a noite, e aqueles que não têm carro.

    Exibir as três listas resultantes.    
    '''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# Converter listas em sets
turno_dia_set = set(turno_dia)
turno_noite_set = set(turno_noite)
tem_carro_set = set(tem_carro)

# Funcionários que têm carro e trabalham durante a noite
lista1 = tem_carro_set.intersection(turno_noite_set)

# Funcionários que têm carro e trabalham durante o dia
lista2 = tem_carro_set.intersection(turno_dia_set)

# Funcionários que não têm carro
lista3 = set(funcionarios).difference(tem_carro_set)

print("Lista1 (Funcionários que têm carro e trabalham durante o dia):", lista1)
print()
print("Lista2 (Funcionários que têm carro e trabalham durante a noite):", lista2)
print()
print("Lista3 (Funcionários que não têm carro):", lista3)
print()


#======================================================
                            #OU
print('Outras forma de resolver')
print()
#======================================================

# Converter listas em sets

# Funcionários que têm carro e trabalham durante a noite
lista4 = set(tem_carro).intersection(turno_noite)

# Funcionários que têm carro e trabalham durante o dia
lista5 = set(tem_carro).intersection(turno_dia)

# Funcionários que não têm carro
lista6 = set(funcionarios).difference(tem_carro)

print("Lista1 (Funcionários que têm carro e trabalham durante o dia):", lista4)
print()
print("Lista2 (Funcionários que têm carro e trabalham durante a noite):", lista5)
print()
print("Lista3 (Funcionários que não têm carro):", lista6)
print()