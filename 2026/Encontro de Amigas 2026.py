A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())
C1 = int(input())
C2 = int(input())
inicio = max(A1, B1, C1)
fim = min(A2, B2, C2)

if inicio > fim:
    print(0)
else:
    print(fim - inicio + 1)