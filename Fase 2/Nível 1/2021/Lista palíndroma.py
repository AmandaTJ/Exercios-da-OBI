n = int(input())
lista = list(map(int, input().split()))
contagem = 0
p = 0
u = n - 1
while p < u:
    if lista[p] == lista[u]:
        p += 1
        u -= 1
    elif lista[p] < lista[u]:
        lista[p + 1] += lista[p]
        p += 1
        contagem += 1
    else:
        lista[u - 1] += lista[u]
        u -= 1
        contagem += 1

print(contagem)