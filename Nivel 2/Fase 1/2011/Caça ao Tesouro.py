# matriz no sabado é de lascar
n, k = map(int, input().split()) # n é a dimensão do quadrado e k o númeor de pistas
pistas = []
for i in range(k):
    x, y, d = map(int, input().split()) # x e y são as coordenadas e d é a quantidade de passos do capitão
    pistas.append((x, y, d))

pr = 0 # possiveis respostas de coordenadas das pistas
rx = -1 # resposta coordenada x
ry = -1 # resposta coordenada y

# criação da matriz de n x n
for i in range(n):
    for j in range(n):
        validade = True
        for x, y, d in pistas:
            distancia = abs(i - x) + abs(j - y)
            if distancia != d:
                validade = False
                break
        if validade:
            pr += 1
            rx = i
            ry = j
if pr == 1:
    print(rx, ry)
else:
    print(-1, -1)