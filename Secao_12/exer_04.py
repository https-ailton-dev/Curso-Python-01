# Calculo de IMC

'''
Qual é a sua Altura em cm:
Qual é o seu peso em kg:
'''

# Menos que 18,5 - Magreza
# Entre 18,5 e 24,9 - Normal
# Entre 25,0 e 29,9 - Sobrepeso
# Entre 30,0 e 39,9 - Obesidade
# Maior que  40,0 - Obesidade grave

altura = float(input("Digite a sua altura (em cm): "))
peso = float(input("Digite o seu peso (em kg): "))

def imc():
    total = peso / ((altura / 100) ** 2)
    return total

if imc() < 18.5:
    print(f'O valor do seu IMC é: {imc()}')
    print('Magreza')

elif 18.5 <= imc() < 24.9:
    print(f'O valor do seu IMC é: {imc()}')
    print('Normal')

elif 25.0 <= imc() < 29.9:
    print(f'O valor do seu IMC é: {imc()}')
    print('Sobrepeso')

elif 30.0 <= imc() < 39.9:
    print(f'O valor do seu IMC é: {imc()}')
    print('Obesidade')

elif imc() >= 40.0:
    print(f'O valor do seu IMC é: {imc()}')
    print('Obesidade grave')



