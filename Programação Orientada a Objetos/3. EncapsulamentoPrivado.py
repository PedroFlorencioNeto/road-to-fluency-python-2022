# ------------------------------------- #
#  Orientação a Objetos em Python
#
# por: Pedro Florencio de Almeida Neto
# ------------------------------------- #

class Pessoa:
    def __init__(self, nome: str, idade:int, cpf:str):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf # Priva o atributo, mas a classe tem acesso
    
    def correr(self):
        print('{} está correndo...'.format(self.nome))

    def __apresentar_documento(self): # Priva o método
        print(self.cpf)
    
Pedro = Pessoa('Pedro',25,'12345678912')

# Tentando acessar ao CPF
print(Pedro.__apresentar_documento())