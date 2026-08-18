N = int(input())

for l in range(N):
    for c in range(N):
        cima = l
        esquerda = c
        baixo = N - 1 - l
        direita = N - 1 - c

        valor = min(cima, esquerda, baixo, direita) + 1

        print(valor, end=" ")

    print()

