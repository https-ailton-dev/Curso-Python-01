# Desafios com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve retornar na tela a mensagem 'Você necessita de x latas de tintas'
'''

rendimento = float(input("Digite o rendimento da tinta (em metros quadrados por lata): "))
altura = float(input("Digite a altura da parede (em metros): "))
largura = float(input("Digite a largura da parede (em metros): "))

def calcular_tinta():
    area_parede = altura * largura
    quantidade_tinta = area_parede / rendimento
    return quantidade_tinta

print("Você necessita de", calcular_tinta(), "latas de tinta.")