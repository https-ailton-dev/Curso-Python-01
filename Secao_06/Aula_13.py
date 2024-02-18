#Criando condições com While Loop - Aula 13

#Publicar um produto com comissão de 10% se for acima de R$20

valor = int(input('Digite o valor do seu Produto em R$: '))

while valor > 20:
    valor = (valor*0.10) + valor
    print(f'O valor corrigido do seu produto será de R${valor}')
    break