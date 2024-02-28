user_num = int(input('Por favor digite um numero: '))

par_impar = lambda x: 'Par' if x % 2 == 0 else 'Impar'

print((f'O numero {user_num} é {par_impar(user_num)}'))