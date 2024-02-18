#Argumentos Default e Non-default - Aula 05

def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vindas('Marcos')