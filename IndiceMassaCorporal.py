

# Estas funções são para calcular o Indice da Massa Corporal de uma pessoa.
# É necessário algumas informações, dependendo da idade e do sexo da pessoa.
# Porém, para os adultos e idosos, não há necessidade do sexo da pessoa, pois serve para ambos o mesmo índice.

class IMC(object):
    def __init__(self, peso, altura, sexo, idade):
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.idade = idade
        self.IMC = self.peso / (self.altura * self.altura)
        print("O IMC é: ", self.IMC)

    def criança(self):
        return "Ainda a se fazer #Criança"
        # A partir de 0 anos até 19 anos de idade
        # Fazer a função para o cálculo do IMC para crianças e adolescentes
        # Arrumar essa nova função de acordo com a Tabela do OMS

    def adulto(self):
        # Adultos (ambos sexos)

        if self.IMC < 16:
            x = "magreza Grau 1"
        elif 16 <= self.IMC < 17:
            x = "magreza grau II"
        elif 17 <= self.IMC < 18.4:
            x = "magreza grau I"
        elif 18.5 <= self.IMC < 25:
            x = "peso ideal"
        elif 25 <= self.IMC < 30:
            x = "sobrepeso"
        elif 30 <= self.IMC < 35:
            x = "obesidade grau I"
        elif 35 <= self.IMC < 40:
            x = "obesidade grau II"
        elif self.IMC >= 40:
            x = "obesidade grau III"
        return x

    def idoso(self):
        # Idosos (ambos sexos)
        if self.IMC < 23:
            x = "magro demais"
        elif 23 <= self.IMC < 28:
            x = "peso ideal"
        elif 28 <= self.IMC < 30:
            x = "sobrepeso"
        elif self.IMC >= 30:
            x = "obesidade"
        return x

    def resultado(self):
        if 0 <= self.idade < 19:
            resultado = self.criança()
        elif 19 <= self.idade < 65:
            resultado = self.adulto()
        elif self.idade >= 65:
            resultado =self.idoso()
        return print("Ele/ela está com", resultado)

