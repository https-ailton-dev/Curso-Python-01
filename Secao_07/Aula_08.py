#Vários argumentos xargs nomeando parametros - Aula 08

#criar uma função que armazena numeros e strings (dados)

def agencia(**carro):
    return carro


print(agencia(marca='Gol', cor='Branca', motor=1.0))
print(agencia(marca='Polo', cor='Verde', motor=1.6))
print(agencia(marca='Gol', cor='Preto'))
print(agencia(marca='Voyagem', cor='cinza', motor=1.0, placa=12345))