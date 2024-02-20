#Calculando a idade do funcionário


from datetime import datetime

#criar a Classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        #self.ano_nascimento = int(2024 - self.ano_nascimento)
        #return self.ano_nascimento
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento



#criar o Objeto
usuario1 = Funcionarios('Ailton', 'Lima', 2001)
usuario2 = Funcionarios('Daniel', 'Ferreira', 2005)
usuario3 = Funcionarios('Maria', 'Dores', 1966)


#print(usuario1.nome + ' ' + usuario1.sobrenome)

#print(usuario1.nome_completo())

print(Funcionarios.idade_funcionario(usuario3))
