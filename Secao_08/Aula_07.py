#Verificando itens em uma lista - Aula 07

cor_cliente = input('Digite a cor desejada: ')

cores = ['amarelo', 'verde', 'azul', 'vermelho']

#.lower = funcão transforma todas as cases em minusculas

if cor_cliente.lower() in cores:
    print('Em Estoque')

else:
    print('Não temos esta cor em estoque')