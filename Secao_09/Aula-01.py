#Trabalhando com o Try e Except com uma lista

#Erros
    # Excelentes para teste
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try: 
    letras = ['a', 'b', 'c']
    print(letras[3])

except IndexError:
    print('Index não existe')

