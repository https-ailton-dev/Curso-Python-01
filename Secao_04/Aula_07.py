# Utilizando Formated Strings - Aula 7

nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + '[' + profissao + ']'

texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'

print(texto)
print(texto2)

# O Marcos Silva é um excelente [Programador]
