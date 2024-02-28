capitais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Portugal': 'Lisboa',
    'Alemanha': 'Berlim',
    'Chile': 'Santiago'
}

pais_usuario = input('Digite o País desejado: ')

if pais_usuario in capitais:
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}')

else:
    print('Desculpe, não temos informações sobre esse País')