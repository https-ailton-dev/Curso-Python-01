def potencia(base, expoente=2):
    return base ** expoente

num1 = int(input('Por favor digite o numero para base: '))
num2 = (input('Por favor digite o expoente: '))

if num2:
    print(f'O resultado é: {potencia(num1, int(num2))}')

else:
    print(f'O resultado é: {potencia(num1)}')    