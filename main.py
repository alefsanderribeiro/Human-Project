import Humano as hm


sexo = ["Masculino", "Feminino"]

pessoa = ["Alefsander", sexo[0], (1994, 10, 23), 1.74, 75]
# As informações na ordem são: nome, genero, data_nascimento, altura, peso):

# Forneceça a data_nascimento na forma de: (ano, mês, dia)
pessoa1 = hm.Humano(pessoa[0], pessoa[1], pessoa[2], pessoa[3], pessoa[4])

pessoa2 = hm.Humano("Geissilaine", sexo[1], (1998, 7, 19), 1.78, 70)
pessoa3 = hm.Humano("Edsandra", sexo[1], (1977, 12, 16), 1.65, 65)
#pessoa4 = hm.Humano("Alefsander", "Masculino", 2015, 1.74, 75)
#pessoa5 = hm.Humano("Alefsander", "Masculino", 2015, 1.74, 75)

#print(pessoa1)


pessoa1.massa_corporal()
#pessoa1.geracao()

"""
print(pessoa1.altura)
print(pessoa1.data_nascimento)
print(pessoa1.idade)
print(pessoa1.nome)

pessoa2.massa_corporal()
pessoa2.geracao()

print(pessoa2.altura)
print(pessoa2.data_nascimento)
print(pessoa2.idade)
print(pessoa2.nome)

calculo = hm.calcular_diferenca_idade(pessoa1.data_nascimento, pessoa2.data_nascimento)
print("a diferença é ", calculo)

resultado = hm.calcular_diferenca_idade2(pessoa1.data_nascimento, pessoa2.data_nascimento)
print(resultado)


calculo2 = hm.calcular_idade(pessoa1.data_nascimento)

print("a diferença é ", calculo2)




#datadif = datetime.timedelta((datetime.date(pessoa1[2,0], pessoa1[2,1], pessoa1[2,2]) - (pessoa2[2,0], pessoa2[2,1], pessoa2[2,2])))

#print(datadif)

"""
