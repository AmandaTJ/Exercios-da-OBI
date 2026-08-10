n, m = map(int, input().split()) # quantidade de linhas e quantidade de colunas respectivamente
bandeija = []

for i in range(n):
    linha = list(map(int, input().split()))
    bandeija.append(linha)

# p1 = quantidade de gotas para a possibilidade em que a bandeija começa com par. Ex.: par, impar, par, impar...
# p2 = quantidade de gotas para a possibilidade em que a bandeija começa com impar. Ex.: impar, par, impar, par...

p1 = 0
p2 = 0

g = 0 # quantidade de gotas em cada cokkie

for i in range(n):
    for j in range(m):
        g = bandeija[i][j]

        #possibilidade 1: bandeija começa com par
        if (i + j) % 2 == 0: # posição par
            if g % 2 != 0: # se a quantidade de gotas for impar, adiciona uma gota para que fique par
                p1 += 1
        else: # posição impar
            if g % 2 == 0: # se a quantidade de gotas for par, adiciona uma gota para que fique impar
                p1 += 1
        #possibilidade 2: bandeija começa com impar
        if (i + j) % 2 == 0: # posição par
            if g % 2 == 0: # se a quantidade de gotas for par, adiciona uma gota para que fique impar
                p2 += 1
        else: # posição impar
            if g % 2 != 0: # se a quantidade de gotas for impar, adiciona uma gota para que fique par
                p2 += 1

print(min(p1, p2))

# Impressão da bandeija com a quantidade de gotas ajustada para que fique alternada entre par e impar

for i in range(n):
    for j in range(m):
        if p1 <= p2:
            if (i + j) % 2 == 0: # posição par
                if bandeija[i][j] % 2 != 0: # se a quantidade de gotas for impar, adiciona uma gota para que fique par
                    bandeija[i][j] += 1
            else: # posição impar
                if bandeija[i][j] % 2 == 0: # se a quantidade de gotas for par, adiciona uma gota para que fique impar
                    bandeija[i][j] += 1
        else:
            if (i + j) % 2 == 0: # posição par
                if bandeija[i][j] % 2 == 0: # se a quantidade de gotas for par, adiciona uma gota para que fique impar
                    bandeija[i][j] += 1
            else: # posição impar
                if bandeija[i][j] % 2 != 0: # se a quantidade de gotas for impar, adiciona uma gota para que fique par
                    bandeija[i][j] += 1

# Impressão da bandeija com a quantidade de gotas ajustada para que fique alternada entre par e impar

for linha in bandeija:
    print(*linha)