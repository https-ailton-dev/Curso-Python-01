#Criando Objetos dentro de uma Classe

    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class(instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # ====
    # Class: Frutas
    # Objects: Abacate, Banana

#criar a Classe
class Funcionarios:
    pass

#criar o Objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

#criar os parametros do usuario 1
usuario1.nome = 'Ailton'
usuario1.sobrenome = 'Lima'
usuario1.data_nascimento = '14/01/2001'

#criar os parametros do usuario 2
usuario2.nome = 'Daniel'
usuario2.sobrenome = 'Ferreira'
usuario2.data_nascimento = '16/01/2005'

print(usuario1.nome)
print()
print(usuario2.nome)
