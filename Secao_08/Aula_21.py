#Função Map em uma lista

#https://docs.python.org/3/library/functions.html

    # Muito utilizado com listas
    # Aplicar ma função a um Itarable, por item. (list, tuple, dic, etc.)

list1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

list2 = map(multi, list1)

print(list(list2))