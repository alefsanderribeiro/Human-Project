

# Adultos (ambos sexos)
def IMC_Adulto(x):
    if x < 16:
        return "magreza grau III"
    elif 16 <= x < 17:
        return "magreza grau II"
    elif 17 <= x < 18.4:
        return "magreza grau I"
    elif 18.5 <= x < 25:
        return "peso ideal"
    elif 25 <= x < 30:
        return "sobrepeso"
    elif 30 <= x < 35:
        return "obesidade grau I"
    elif 35 <= x < 40:
        return "obesidade grau II"
    elif x >= 40:
        return "obesidade grau III"

# Idosos (ambos sexos)

def IMC_Idoso(x):
    if x < 23:
        return "magro demais"
    elif 23 <= x < 28:
        return "peso ideal"
    elif 28 <= x < 30:
       return "sobrepeso"
    elif x >= 30:
        return "obesidade"
