carro_cliente = input('Digite o modelo desejado: ')

carros = ['BMW X6', 'BMW I5', 'BMW I8']

if carro_cliente.upper() in carros:
    print('Esse carro está em estoque')

else:
    print('Desculpe, esse carro não está disponível')