user_num = float(input('Por favor digite um numero: '))

def dobro(num):
    return num * 2
    

def quadrado(num):
    return dobro(num) ** 2
    
print(f'o quadrado do dobro de {user_num} é {quadrado(user_num)}')