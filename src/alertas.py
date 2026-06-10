def avaliar(dados):
  counter = 0
  aval = []
  for d in dados:
    if(counter == 0):
      if(d > 50):
        aval.append("Alerta - Temperatura Extrema, contatar corpo de bombeiros")
      else:
        aval.append("Temperatura normal")
    elif(counter == 1):
      if(d > 2000):
        aval.append("Alerta - Desmatamento excessivo, contatar policia")
      else:
        aval.append("Desmatamento não muito grande")
    counter = counter + 1
  return aval    
