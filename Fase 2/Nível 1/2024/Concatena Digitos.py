N, Q = map(int, input().split()) # N = numero de digitos e Q = quantidade de perguntas

digitos = list(map(int, input().split()))

somas = [0] * (N + 1) # soma acumulada dos digitos

for i in range(1, N + 1):
    somas[i] = somas[i - 1] + somas[i - 1]

for _ in range(Q):
    L, R = map(int, input().split())

    quantidade = R - L + 1
    soma = somas[R] - somas[L - 1]

    potencial = soma * 11 * (quantidade - 1)

    print(potencial)