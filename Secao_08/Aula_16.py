#Atualizando itens no dicionário

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

aluno['nome'] = 'José'

print(aluno)


aluno1 = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

aluno1.update({'nome': 'José', 'nota_final': 'B'}) 

print(aluno1)


aluno2 = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

aluno2.update({'endereçço': 'Rua A'}) 

print(aluno2)


aluno2 = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

print(aluno2.get('endereço', 'Não existe'))


aluno3 = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

del aluno3['idade']

print(aluno3)