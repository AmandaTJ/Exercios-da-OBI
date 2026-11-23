# esse é mais tranquilo
n = int(input())
lista = []
for _ in range(n):
    r = int(input())
    if r != 0:
        lista.append(r)
    elif r == 0:
        del lista[-1]
print(sum(lista))