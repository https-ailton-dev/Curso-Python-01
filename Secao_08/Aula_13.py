#Funções em sets

    #Similar a listas
    #Evita itens duplicados
    #Não utiliza index

list1 = [1, 2, 3, 5, 6]

s1 = {1, 2, 3, 5, 6}

print(list1)
print(s1)

print(type(list1))
print(type(s1))

s2 = {1, 2, 3, 5, 6}
s2.update([7, 8, 9, 10])
s2.remove(10)
s2.discard(9)

print(s2)