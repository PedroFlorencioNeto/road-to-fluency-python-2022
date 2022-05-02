# ------------------------------------- #
#  Orientação a Objetos em Python
#
# por: Pedro Florencio de Almeida Neto
# ------------------------------------- #

# Para criar uma classe, convencionalmente utiliza-se letra maiúscula
class MinhaClasse:

    # Método construtor: É o que define a classe    
    def __init__(self, atributo2):
        self.meu_atributo = 'Olá, Mundo!'
        self.meu_atributo2 = atributo2

    def escreve_na_tela(self):
        print('Este método printa esta mensagem')
    
    def multiplica(self, num, mult):
        return num * mult

# Instanciando um objeto
meu_objeto = MinhaClasse('meu atributo')

# Chamando primeiro método do objeto
meu_objeto.escreve_na_tela()

# Chamando segundo método do objeto
multiplicacao = meu_objeto.multiplica(5,2)
print(multiplicacao)

# Acessando ao atributo
print(meu_objeto.meu_atributo2)
