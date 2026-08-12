K, N = map(int, input().split()) # K = tamanho do alfabeto e N = tamanho da mensagem

alfabeto = list(input())
mensagem = list(input())

presente = 0

for letra in mensagem:
    if letra in alfabeto:
        presente += 1

if presente == N:
    print("S")
else:
    print("N")