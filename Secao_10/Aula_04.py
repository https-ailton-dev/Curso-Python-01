#Criando Construtores

    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class(instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # ====
    # Class: Frutas
    # Objects: Abacate, Banana

#criar a Classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento



#criar o Objeto
usuario1 = Funcionarios('Ailton', 'Lima', '14/01/2001')
usuario2 = Funcionarios('Daniel', 'Ferreira', '16/01/2005')
usuario3 = Funcionarios('Maria', 'Dores', '29/01/1966')

'''#criar os parametros do usuario 1
usuario1.nome = 'Ailton'
usuario1.sobrenome = 'Lima'
usuario1.data_nascimento = '14/01/2001'

#criar os parametros do usuario 2
usuario2.nome = 'Daniel'
usuario2.sobrenome = 'Ferreira'
usuario2.data_nascimento = '16/01/2005'
'''

print(usuario1.nome)
print()
print(usuario2.nome)
print()
print(usuario3.data_nascimento)