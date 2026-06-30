INF = 10**18

N, M = map(int, input().split())
A = list(map(int, input().split()))

v1 = [A[0], M - A[0]]  #valor anterior/inicial/final
somaf = [v1[0], v1[1]] # soma final

for i in range(1, N):
    v2 = [A[i], M - A[i]] #valor atual
    somap = [INF, INF] #soma possivel para valor atual

    for i in range(2):
        if somaf[i] == INF:
            continue

        for c in range(2):
            if v1[i] <= v2[c]: # se valor anterior for menor ou igual ao valor atual, podemos somar
                somap[c] = min(somap[c], somaf[i] + v2[c]) # escolhe o menor valor possivel para a soma dos valores

    somaf = somap # atribui a soma total para a soma do valor atual
    v1 = v2 # atribui o valor atual para o valor anterior/final

resposta = min(somaf)

if resposta == INF:
    print(-1)
else:
    print(resposta)