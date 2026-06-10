import random
def coletar():
  temperaturaMonitorada = random.randrange(-20, 300, 1)
  hectaresDestruidos = random.randrange(0, 50000, 1)
  energia = random.randrange(0, 100, 1)
  dados = {"Temperatura monitorada": temperaturaMonitorada, "Hectares Desmatados": hectaresDestruidos, 
           "Energia restante": energia}
  return dados
