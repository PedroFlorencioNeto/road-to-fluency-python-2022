# ------------------------------------- #
#  Orientação a Objetos em Python
#
# por: Pedro Florencio de Almeida Neto
# ------------------------------------- #

class ControleRemoto:
    # Método construtor e atributos
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def escolher_canal(self, canal:int):
        print('Estou no canal {}'.format(canal))
    
    def avancar_canal(self):
        print('avancei um canal...')
    
    def voltar_canal(self):
        print('retornei um canal...')

# Instanciando objeto
controle_lg = ControleRemoto('LG 49 Polegadas', 'Sala')

# Utilizando os 3 métodos
controle_lg.escolher_canal(5)

controle_lg.avancar_canal()

controle_lg.voltar_canal()

# Verificando os atributos
print(controle_lg.televisao)

print(controle_lg.comodo)
