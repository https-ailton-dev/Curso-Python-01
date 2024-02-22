# Desafios com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em Celsius) do steak, ele retorna o ponto de cozimento em portugues.
O usuário deverá fornecer a temperatura.

Temperaturas
48°C - Selada
54°C - Ao ponto para Mal
60°C - Ao ponto
65°C - Ao ponto para Bem
71°C - Bem passada
'''


temperatura = int(input('Digite a temperatura: '))

if temperatura < 48:
    print('Cozinhar por mais alguns minutos')

elif 48 <= temperatura < 54:
    print('Selada')

elif 54 <= temperatura < 60:
    print('Ao ponto para Mal')

elif  60 <= temperatura < 65:
    print('Ao ponto')

elif 65 <= temperatura < 71:
    print('Ao ponto para Bem')

elif temperatura == 71:
    print('Bem passada')

else:
    print('O alimento passou do ponto recomendado')

