#A Amigos
#N Filas
#M Assentos por fila
A, N, M = map(int, input().split())

resposta = -1

for fila in range(N, 0, -1):
    assento = list(map(int, input().split()))
    S = 0
    for assento in assento:
        if assento == 0:
            S += 1

            if S >= A:
                resposta = fila
                break
        else:
            S = 0

print(resposta)