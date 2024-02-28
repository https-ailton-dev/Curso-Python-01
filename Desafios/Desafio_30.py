user_num1 = int(input('Por favor digite o primeiro numero: '))
user_num2 = int(input('Por favor digite o segundo numero: '))

cal_multi = lambda x, y:  x * y 

print((f'A multiplicação de {user_num1} X {user_num2} é {cal_multi(user_num1, user_num2)}'))