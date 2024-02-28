def fatorial(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * fatorial(n-1)
    

num1 = int(input('Por favor digite o primeiro numero: '))

print(f'O fatorial de {num1} é {fatorial(num1)}')