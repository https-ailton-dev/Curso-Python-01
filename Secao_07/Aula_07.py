#Vários argumentos xargs com números - Aula 07

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


x = soma(2,3,4,5,6,7)
print(x)
