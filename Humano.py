import datetime
import IndiceMassaCorporal as IM


class Humano(object):

    def __init__(self, nome, genero, data_nascimento, altura, peso):
        self.nome = nome
        self.genero = genero
        self.altura = altura
        self.peso = peso
        self.data_nascimento = datetime.date(data_nascimento[0], data_nascimento[1], data_nascimento[2])
        self.idade = calcular_idade(self.data_nascimento)

    def __str__(self):
        return f"O nosso Humano tem o nome de {self.nome}, " \
               f"que nasceu no dia {self.data_nascimento}, " \
               f"com o genero {self.genero}, " \
               f"a sua altura é de {self.altura} " \
               f" e o peso de {self.peso}Kg."

    def nome(self):
        return self.nome

    def altura(self):
        return self.altura

    def peso(self):
        return self.peso

    def data_nascimento(self):
        return self.data_nascimento

    def idade(self):
        return self.idade

    def geracao(self):
        if datetime.date(1965, 1, 1) <= self.data_nascimento <= datetime.date(1981, 12, 31):
            print(f"{self.nome} é da Geração X")
        elif datetime.date(1982, 1, 1) <= self.data_nascimento <= datetime.date(1994, 12, 31):
            print(f"{self.nome} é da Geração Y")
        elif datetime.date(1995, 1, 1) <= self.data_nascimento <= datetime.date(2010, 12, 31):
            print(f"{self.nome} é da Geração Z")
        elif self.data_nascimento >= datetime.date(2011, 1, 1):
            print(f"{self.nome} é da Geração Alpha")

    def massa_corporal(self):

        IMC = IM.IMC(self.peso, self.altura, self.genero, self.idade)
        IMC.resultado()





# Essa função serve para calcular a idade de uma pessoa (viva hoje), somente preciso da data de nascimento dela
def calcular_idade(data_nascimento):
    idade = int((datetime.date.today() - data_nascimento).days / 365.2425)
    return idade


# Essa função serve para calcular a diferença de uma idade para outra.

def calcular_diferenca_idade(data_primeira_idade, data_segunda_idade):
    idade = int((data_segunda_idade - data_primeira_idade).days)
    return idade


def calcular_diferenca_idade2(data_primeira_idade, data_segunda_idade):
    resultado = (data_segunda_idade - data_primeira_idade)
    return resultado
