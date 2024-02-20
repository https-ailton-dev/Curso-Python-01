#Criando a sua primeira classe

    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class(instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # ====
    # Class: Frutas
    # Objects: Abacate, Banana

class Funcionarios:
    nome = 'Ailton'
    sobrenome = 'Lima'
    data_nascimento = '14/01/2001'

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)