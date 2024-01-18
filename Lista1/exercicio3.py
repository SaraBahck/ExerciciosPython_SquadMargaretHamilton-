 #funcao calcula a distancia
def calcula_unidades(distancia):
    distancia_m = distancia * 1000
    distancia_cm = distancia_m * 100
    distancia_mm = distancia_cm * 10
    return distancia_m, distancia_cm, distancia_mm

#usuario informa o km
distancia_km = float(input('Digite a quantidade de quilômetros: '))

distancia_m, distancia_cm, distancia_mm = calcula_unidades(distancia_km)

#imprime a distancia em metros, centimetros, milimetros

print( f'A distância em metros é: {distancia_m}')
print( f'A distância em centímetros é: {distancia_cm}' )
print( f'A distância em milímetros é: {distancia_mm}' )