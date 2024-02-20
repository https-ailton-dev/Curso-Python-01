#Adicionando mais funções a classe

#criar a Classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome



#criar o Objeto
usuario1 = Funcionarios('Ailton', 'Lima', '14/01/2001')
usuario2 = Funcionarios('Daniel', 'Ferreira', '16/01/2005')
usuario3 = Funcionarios('Maria', 'Dores', '29/01/1966')


#print(usuario1.nome + ' ' + usuario1.sobrenome)

print(usuario1.nome_completo())

print(Funcionarios.nome_completo(usuario2))


