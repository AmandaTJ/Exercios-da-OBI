C = int(input()) # quantidade de combustivel que o carro gasta por km
D = int(input()) # distancia restante do aeroporto
T = int(input()) # combuctivel restante

compra = max(0, D / C - T) # seleciona o maior valor

print(f"{compra:.1f}")