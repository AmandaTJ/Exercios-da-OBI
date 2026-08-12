N, M, P = map(int, input().split()) # N = número de linhas, M = número de colunas, P = número de passos

pista = []

# Formação da pista e enumeração dos alunos:
for l in range(N):
    linha = []

    for c in range(M):
        linha.append(l * M + c + 1)

    pista.append(linha)

# Entrada das instruções de movimentação:
for passo in range(P):
    tipo, a, b = input().split()
    a = int(a) - 1
    b = int(b) - 1
# L = troca de linhas, C = troca de colunas
    if tipo == "L":
        pista[a], pista[b] = pista[b], pista[a]
    elif tipo == "C":
        for l in range(N):
            pista[l][a], pista[l][b] = pista[l][b], pista[l][a]

# Impressão da pista final:
for l in range(N):
    for c in range(M):
        print(pista[l][c], end=" ")
    print()