#Adicionando o Else e Finally

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
finally:
    print('mensagem teste')
    
'''
else:
    print('Valor aceito')
    resultado = valor * 2
    print(resultado)
'''

print('Mais codigo')