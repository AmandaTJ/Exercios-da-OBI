n, m, k = map(int, input().split()) # n = numero de colunas, m = numero de linhas, k = numero de cameras 

# Criação da matriz

observada = [[False] * n for _ in range(m)]

# Lê as câmeras
for _ in range(k):
    c, l, direcao = input().split() # c = coluna da camera, l = linha da camera e direcao = direcao em que a camera foi instalada

# necessario, pois os indicies se iniciam no 0
    c = int(c) - 1
    l = int(l) - 1

    # A própria célula da câmera é observada
    observada[l][c] = True

    if direcao == "N":
        for i in range(l - 1, -1, -1):
            observada[i][c] = True

    elif direcao == "S":
        for i in range(l + 1, m):
            observada[i][c] = True

    elif direcao == "L":
        for j in range(c + 1, n):
            observada[l][j] = True

    elif direcao == "O":
        for j in range(c - 1, -1, -1):
            observada[l][j] = True


# Se a entrada ou a saída estiver sendo observada,
# não existe caminho seguro
if observada[0][0] or observada[m - 1][n - 1]:
    print("N")

else:
    visitado = [[False] * n for _ in range(m)]

    fila = [(0, 0)]
    visitado[0][0] = True

    pos = 0

    while pos < len(fila):
        l, c = fila[pos]
        pos += 1

        # Norte
        if l > 0:
            if not observada[l - 1][c] and not visitado[l - 1][c]:
                visitado[l - 1][c] = True
                fila.append((l - 1, c))

        # Sul
        if l < m - 1:
            if not observada[l + 1][c] and not visitado[l + 1][c]:
                visitado[l + 1][c] = True
                fila.append((l + 1, c))

        # Oeste
        if c > 0:
            if not observada[l][c - 1] and not visitado[l][c - 1]:
                visitado[l][c - 1] = True
                fila.append((l, c - 1))

        # Leste
        if c < n - 1:
            if not observada[l][c + 1] and not visitado[l][c + 1]:
                visitado[l][c + 1] = True
                fila.append((l, c + 1))

    if visitado[m - 1][n - 1]:
        print("S")
    else:
        print("N")