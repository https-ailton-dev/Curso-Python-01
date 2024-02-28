cidade_cliente = str(input('Digite o nome de uma Cidade: '))

cidade_tuple = ('Santo André', 'São Caetano do Sul', 'Diadema')


if cidade_cliente in cidade_tuple:
    print('A cidade está na lista')

else:
    print('A cidade não está na lista')