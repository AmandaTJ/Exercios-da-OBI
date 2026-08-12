N = int(input())

sequencia = []
distintos = []
maior = 0

for i in range(N):
    sequencia.append(int(input()))

for num in sequencia:

    while num in distintos:
        distintos.pop(0)

    distintos.append(num)

    if len(distintos) > maior:
        maior = len(distintos)

print(maior)