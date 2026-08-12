D = int(input()) # distancia da escola na avenida
anda = 0
pontos = [0, 400, 800, 1200, 1600, 2000]
for m in pontos:
    if D < pontos[1]:
        anda = D
    elif D == pontos[1] or D == pontos[2] or D == pontos[3] or D == pontos[4] or D == pontos[5]:
        anda = 0
    elif D > pontos[1] and D < pontos[2]:
        anda = min(D - pontos[1], pontos[2] - D)
    elif D > pontos[2] and D < pontos[3]:
        anda = min(D - pontos[2], pontos[3] - D)
    elif D > pontos[3] and D < pontos[4]:
        anda = min(D - pontos[3], pontos[4] - D)
    elif D > pontos[4] and D < pontos[5]:
        anda = min(D - pontos[4], pontos[5] - D)
print(anda)