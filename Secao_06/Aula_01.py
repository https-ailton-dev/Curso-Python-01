#IF, ELSEIF e ELSE - Aula 1

velocidade = 50

if velocidade > 110:
    print('Acima da velocidade permitida')
    print('Por favor, reduzir sua velocidade')

elif velocidade < 60:
    print('Velocidade muito abaixo da velociade da via')
    print('Por favor aumentar a velocidade para a velociade da via')

else:
    print('Velocidade OK')