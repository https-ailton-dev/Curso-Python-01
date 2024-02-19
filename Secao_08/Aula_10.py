#Entendendo sobre Tuples

    #Tuples 

    # Armazenar mais de uma informações em variáveis
    # Manter a sequencia dos dados em uma variável
    # Não podem ser alteradas

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']

cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

cores_tuple.append('Roxo')

print(cores_tuple)

'''
cores_tuple.append('Roxo')
    ^^^^^^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'

'''