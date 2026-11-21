N = int(input())

cidades = []

for i in range(N + 1):
    cidades.append([])

for i in range(N - 1):
    A, B = map(int, input().split())
    cidades[A].append(B)
    cidades[B].append(A)

def busca(inicio):
    visitado = [False] * (N + 1)
    distancia = [0] * (N + 1)
    fila = [inicio]
    visitado[inicio] = True
    while len(fila) > 0:
        atual = fila[0]
        fila.pop(0)
        for vizinho in cidades[atual]:
            if visitado[vizinho] == False:
                visitado[vizinho] = True
                distancia[vizinho] = distancia[atual] + 1
                fila.append(vizinho)
    maior = 0
    cidade = inicio
    for i in range(1, N + 1):
        if distancia[i] > maior:
            maior = distancia[i]
            cidade = i
    return cidade, maior

A, distancia = busca(1)
B, resposta = busca(A)

print(resposta)